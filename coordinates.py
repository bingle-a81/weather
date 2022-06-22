from typing import NamedTuple
from typing import Union
from typing import Literal
from dataclasses import dataclass

@dataclass
class Coordinates1:
    longitude: float
    latitude: float

def get_gps_coordinates3() -> Coordinates1:
    return Coordinates1(10, 20)

print(get_gps_coordinates3().latitude)
print(get_gps_coordinates3().longitude)


class Coordinates(NamedTuple):
    latitude: float
    longitude: float

def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using MacBook GPS"""
    return Coordinates(10,20)

a= Union[int, str, float]

# def get_gps_coordinates1() ->dict[Literal["longitude" , "latitude"], float]:
#     return {"longitude": 10, "latitude": 20}
coordinates = get_gps_coordinates()
print(coordinates.latitude)
print(coordinates.longitude)

# print(
#     get_gps_coordinates()["longitudeRRR"]  # Тут IDE покажет ошибку!
# )
