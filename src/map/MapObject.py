from abc import ABC, abstractmethod
from os import path, chdir
from math import pi, degrees
import string
from typing import Tuple
import pygame

from src.display.DisplayObject import DisplayObject
import src.Constants as const


class MapObject(DisplayObject, ABC):

    def __init__(self, position: Tuple[int, int], texture: str):
        super().__init__(position)
        self.angle = None
        self.angle: float
        self.texture: str = texture

    def print(self) -> pygame.Surface:
        # TODO self.image - to display something other than square
        img = pygame.image.load(path.join("images", self.texture)).convert_alpha()
        img = pygame.transform.scale(img, (const.BLOCK_SIZE, const.BLOCK_SIZE))
        img = pygame.transform.rotate(img, -degrees(self.angle))

        '''surface: pygame.Surface = pygame.Surface((const.BLOCK_SIZE, const.BLOCK_SIZE))
        surface.fill(self.color)'''
        return img
