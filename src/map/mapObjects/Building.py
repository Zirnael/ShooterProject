from typing import Tuple

from src.map.MapObject import MapObject
from src.Constants import BLOCK_SIZE


class Building(MapObject):
    def __init__(self, position: Tuple[int, int]):
        super().__init__(position)
