import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit, cross_val_score
from sklearn.linear_model import LinearRegression
from datetime import datetime

# Can use CSV for any city
file_path = 'DallasWeather40Years.csv'
data = pd.read_csv(file_path)

data['dt_iso'] = data['dt_iso'].str.replace(' UTC', '', regex=False)
data['dt_iso'] = pd.to_datetime(data['dt_iso'], errors='coerce')

data['year'] = data['dt_iso'].dt.year

constant_columns = [col for col in data.columns if data[col].nunique() == 1]
data = data.drop(columns=constant_columns)


cleaned_file_path = 'cleaned_weather_data.csv'
data.to_csv(cleaned_file_path, index=False)

# Filter data for a specific date
def filter_data_for_date(data, month, day):
    return data[(data['dt_iso'].dt.month == month) & (data['dt_iso'].dt.day == day)]

# Preprocess data and train the models for each feature
def train_models(data):
    numeric_data = data.select_dtypes(include=[np.number])
    numeric_data.fillna(numeric_data.mean(), inplace=True)
    
    features = ['year', 'temp', 'visibility', 'dew_point', 'feels_like', 'pressure', 'humidity', 'wind_speed', 'clouds_all']
    models = {}
    
    if any(col not in numeric_data.columns for col in features):
        print("One or more features are missing from the data after removing constant columns.")
        return models
    
    X = numeric_data[features]
    
    for feature in features[1:]:  
        y = numeric_data[feature]
        
        # Train a linear regression model
        model = LinearRegression()
        model.fit(X, y)
        models[feature] = model
    
    return models

# Predict weather for a specific date
def predict_weather_for_date(models, data, year, month, day):
    filtered_data = filter_data_for_date(data, month, day)
    if filtered_data.empty:
        return None
    
    features = ['year', 'temp', 'visibility', 'dew_point', 'feels_like', 'pressure', 'humidity', 'wind_speed', 'clouds_all']
    prediction = {}
    
    prediction_features = filtered_data[features].mean().to_frame().T
    prediction_features['year'] = year
    for feature in features[1:]:
        if feature in models:
            model = models[feature]
            predicted_value = model.predict(prediction_features)[0]
            prediction[feature] = predicted_value
        else:
            prediction[feature] = np.nan
    
    return prediction

# Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    # Load cleaned dataset
    cleaned_file_path = 'cleaned_weather_data.csv'
    data = pd.read_csv(cleaned_file_path)

    data['dt_iso'] = pd.to_datetime(data['dt_iso'], errors='coerce')
    
    # Ask user
    user_input = input("Enter a date (YYYY-MM-DD): ")
    try:
        target_date = datetime.strptime(user_input, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        input("Press Enter to exit...")
        return
    
    year = target_date.year
    month = target_date.month
    day = target_date.day
    
    # Filter data for the specific date
    filtered_data = filter_data_for_date(data, month, day)
    
    if filtered_data.empty:
        print(f"No historical data available for {target_date.strftime('%B %d')}.")
        input("Press Enter to exit...")
        return
    
    models = train_models(filtered_data)
    predicted_features = predict_weather_for_date(models, data, year, month, day)
    
    if predicted_features is not None:
        predicted_features['temp'] = kelvin_to_fahrenheit(predicted_features['temp'])
        predicted_features['dew_point'] = kelvin_to_fahrenheit(predicted_features['dew_point'])
        predicted_features['feels_like'] = kelvin_to_fahrenheit(predicted_features['feels_like'])
        
        print(f'Predicted weather for {target_date.strftime("%B %d, %Y")}:')
        print(f'Temperature: {predicted_features["temp"]:.2f}°F')
        print(f'Visibility: {predicted_features["visibility"]:.2f} meters')
        print(f'Dew Point: {predicted_features["dew_point"]:.2f}°F')
        print(f'Feels Like: {predicted_features["feels_like"]:.2f}°F')
        print(f'Pressure: {predicted_features["pressure"]:.2f} hPa')
        print(f'Humidity: {predicted_features["humidity"]:.2f}%')
        print(f'Wind Speed: {predicted_features["wind_speed"]:.2f} m/s')
        print(f'Cloud Coverage: {predicted_features["clouds_all"]:.2f}%')
    else:
        print(f"Insufficient data to make a prediction for {target_date.strftime('%B %d, %Y')}.")
    
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
