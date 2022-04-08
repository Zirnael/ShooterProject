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
        orig_rect = img.get_rect()
        rot_image = pygame.transform.rotate(img, -degrees(self.angle))
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

        '''surface: pygame.Surface = pygame.Surface((const.BLOCK_SIZE, const.BLOCK_SIZE))
        surface.fill(self.color)'''

