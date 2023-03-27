class WeatherForecast:
    def __init__(self, date, temperatureC, summary=None):
        self.date = date
        self.temperatureC = temperatureC
        self.summary = summary
    
    @property
    def temperatureF(self):
        return 32 + int(self.temperatureC / 0.5556)
