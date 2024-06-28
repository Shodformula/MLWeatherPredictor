# MLWeatherPredictor

This project involves developing a machine learning model to predict weather conditions for a specified date using historical weather data. By leveraging historical weather patterns, the model forecasts multiple weather parameters, providing a detailed weather outlook for the chosen date. Specifically, the model predicts:

- **Temperature**: The expected air temperature in degrees Fahrenheit.
- **Visibility**: The distance one can clearly see, measured in meters.
- **Dew Point**: The temperature at which air becomes saturated with moisture, measured in degrees Fahrenheit.
- **Feels-Like Temperature**: The apparent temperature considering wind and humidity, measured in degrees Fahrenheit.
- **Pressure**: The atmospheric pressure at sea level, measured in hectopascals (hPa).
- **Humidity**: The relative humidity as a percentage.
- **Wind Speed**: The speed of the wind, measured in meters per second.
- **Cloud Coverage**: The fraction of the sky covered by clouds, expressed as a percentage.

The project utilizes linear regression models trained on historical weather data to provide accurate and reliable predictions. It incorporates extensive data processing, feature engineering, and model evaluation techniques to ensure the model's robustness and accuracy. The final product is an interactive Python script that prompts users for a specific date and returns detailed weather predictions based on historical trends.

## Project Structure

- `weather_predictor.py`: Main script containing data processing, model training, and prediction logic.
- `DallasWeather40Years.csv`: Historical weather data file for the city of Dallas

## Features

- **Machine Learning Models**: Utilizes linear regression to predict various weather parameters.
- **Data Processing**: Cleans and preprocesses the data, handles missing values, and extracts relevant features.
- **Feature Engineering**: Incorporates year, month, and day to capture temporal patterns.
- **User Interaction**: Prompts the user to input a date and provides weather predictions for that date.

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. **Install Dependencies**:
   Install the required Python libraries using pip
   ```bash
   pip install pandas scikit-learn numpy

3. **Place the Dataset**:
   Find a dataset for any city using services such as the OpenWeatherMap website
   Place the dataset in the same directory as the weather_predictor.py file
   The data set that I used is available here: https://drive.google.com/file/d/1tkzNEhMolT0frTo6uIbDb30guDKsQEW6/view?usp=sharing

## Usage

1. **Run the script**:
   ```bash
   python weather_predictor.py

2. **Input the date**:
   Input the date in the format: 'YYYY-MM-DD'

## Example Output
```bash
$ python weather_prediction.py
Enter a date (YYYY-MM-DD): 2024-05-25
Predicted weather for May 25, 2024:
Temperature: 76.01°F
Visibility: 9643.79 meters
Dew Point: 65.14°F
Feels Like: 77.48°F
Pressure: 1011.86 hPa
Humidity: 71.46%
Wind Speed: 4.60 m/s
Cloud Coverage: 61.72%
