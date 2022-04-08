from typing import Tuple

import src.Constants as const
from src.map.MapObject import MapObject


class Enemy(MapObject):

    def __init__(self, position: Tuple[int, int], texture: str):
        super().__init__(position, texture)
        self.speed = const.BLOCK_SIZE * 0.3
        self.angle = 0
