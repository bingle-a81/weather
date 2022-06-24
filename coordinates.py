import logging.config
from settings import logger_config
from dataclasses import dataclass
from exceptions import CantGetCoordinates

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')


@dataclass(frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using MacBook GPS"""
    try:
        return Coordinates(57.63516, 39.8)
    except TypeError as e:
        raise CantGetCoordinates


def main():
    logger.debug(r'console')
    print(get_gps_coordinates())
    # logger.info(r'console file')
    # logger.warning(r'console file telegram')
    # logger.error(r'console file telegram mail')


if __name__ == '__main__':
    main()
