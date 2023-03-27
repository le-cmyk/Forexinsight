import random
from datetime import timedelta

from Functions.Class.weatherForecast import WeatherForecast

class WeatherForecastService:
    Summaries = [
        "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
    ]

    def get_forecast_async(self, start_date):
        return [
            WeatherForecast(start_date + timedelta(days=index),
                            random.randint(-20, 55),
                            random.choice(self.Summaries))
            for index in range(1, 6)
        ]
