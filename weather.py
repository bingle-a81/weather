import logging.config
from settings import logger_config
from exceptions import ApiServiceError, CantGetCoordinates
from coordinates import get_gps_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather
from pathlib import Path
from history import save_weather, JSONFileWeatherStorage

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')


def main():
    try:
        coordinates = get_gps_coordinates()
        logger.debug(coordinates)
    except CantGetCoordinates:
        print("Не удалось получить GPS координаты")
        exit(1)
    try:
        weather = get_weather(coordinates)
    except ApiServiceError:
        print(f"Не удалось получить погоду по координатам {coordinates}")
        exit(1)
    print(format_weather(weather))

    save_weather(
        weather,
        JSONFileWeatherStorage(Path.cwd() / "history.json")
    )


if __name__ == "__main__":
    main()
    # with open('history.json') as f:
    #     d=f.read()
    # print(d)
