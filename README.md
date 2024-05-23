![Alt text](https://spacecityweather.com/wp-content/uploads/2021/10/CODNEXLAB-GOES-East-local-Austin-comp_radar-11_35Z-20211001_counties-usstrd-ushw-usint-map-id_-20-1n-10-100.gif)

# MLWeatherPredictor-Dallas

This project involves developing a machine learning model to predict weather conditions for a specified date using historical weather data for the city of Dallas. The model forecasts temperature, visibility, dew point, feels-like temperature, pressure, humidity, wind speed, and cloud coverage.

## Project Structure

- `weather_predictor.py`: Main script containing data processing, model training, and prediction logic.
- `DallasWeather40Years.csv`: Historical weather data file.

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
   Place the dataset in the same directory as the weather_predictor.py file
   The data set is available here: https://drive.google.com/file/d/1tkzNEhMolT0frTo6uIbDb30guDKsQEW6/view?usp=sharing

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
