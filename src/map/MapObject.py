from abc import ABC
from os import path
from math import degrees
from typing import Tuple
import pygame

from src.display.DisplayObject import DisplayObject
import src.Constants as const


class MapObject(DisplayObject, ABC):

    def __init__(self, position: Tuple[int, int], texture: str):
        super().__init__(position)
        self.angle = None
        self.angle: float
        self.img: pygame.Surface = pygame.image.load(path.join("images", texture)).convert_alpha()
        self.img = pygame.transform.scale(self.img, (const.BLOCK_SIZE, const.BLOCK_SIZE))

    def print(self) -> pygame.Surface:
        orig_rect = self.img.get_rect()
        rot_image = pygame.transform.rotate(self.img, -degrees(self.angle))
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

        '''surface: pygame.Surface = pygame.Surface((const.BLOCK_SIZE, const.BLOCK_SIZE))
        surface.fill(self.color)'''
