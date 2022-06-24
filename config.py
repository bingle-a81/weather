USE_ROUNDED_COORDS = True
OPENWEATHER_API = "a5e80fbd037ef34ce675ab15254e4eb4"
OPENWEATHER_URL = (
        "https://api.openweathermap.org/data/2.5/weather?"
        "lat={latitude}&lon={longitude}&"
        "appid=" + OPENWEATHER_API + "&lang=ru&"
                                     "units=metric"
)
