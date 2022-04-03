from typing import Tuple

import pygame

import src.Constants as const

from MapObject import MapObject


class Player(MapObject):

    def __init__(self, position: Tuple[int, int]):
        super().__init__(position)
        # TODO self.health?

    def print(self) -> pygame.Surface:
        surface: pygame.Surface = pygame.Surface((const.BLOCK_SIZE, const.BLOCK_SIZE))
        surface.fill(const.colors.WHITE)
        return surface
