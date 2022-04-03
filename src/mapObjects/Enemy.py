import pygame

from src.mapObjects.MapObject import MapObject
import src.Constants as const


class Enemy(MapObject):

    def print(self) -> pygame.Surface:
        surface: pygame.Surface = pygame.Surface((const.BLOCK_SIZE, const.BLOCK_SIZE))
        surface.fill(const.colors.RED)
        return surface
