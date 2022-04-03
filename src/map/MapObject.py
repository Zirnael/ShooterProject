from abc import ABC
from typing import Tuple
import pygame

from src.display.DisplayObject import DisplayObject
import src.Constants as const


class MapObject(DisplayObject, ABC):

    def __init__(self, position: Tuple[int, int], color: Tuple[int, int, int]):
        super().__init__(position)
        self.color: Tuple[int, int, int] = color

    def print(self) -> pygame.Surface:
        # TODO self.image - to display something other than square
        surface: pygame.Surface = pygame.Surface((const.BLOCK_SIZE, const.BLOCK_SIZE))
        surface.fill(self.color)
        return surface
