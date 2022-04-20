from abc import ABC
from os import path
from typing import Tuple
import pygame

from src.display.DisplayObject import DisplayObject
import src.Constants as const


class MapObject(DisplayObject, ABC):

    def __init__(self, position: Tuple[int, int], texture: str):
        super().__init__(position)
        self.health: int = 10
        """Every object with collisions can be destroyed by enemies"""
        self.img: pygame.Surface = pygame.image.load(path.join("images", texture)).convert_alpha()
        self.img = pygame.transform.scale(self.img, (const.BLOCK_SIZE, const.BLOCK_SIZE))

    def print(self) -> pygame.Surface:
        return self.img

    def position(self) -> Tuple[int, int]:
        return self.rectangle.center
