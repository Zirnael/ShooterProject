from typing import Tuple

import src.Constants as const
from src.map.MapObject import MapObject


class Enemy(MapObject):

    def __init__(self, position: Tuple[int, int], color: Tuple[int, int, int]):
        super().__init__(position, color)
        self.speed = const.BLOCK_SIZE*0.3
