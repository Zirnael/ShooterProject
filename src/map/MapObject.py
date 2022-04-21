from abc import ABC
from os import path
from typing import Tuple
import pygame

from src.display.DisplayObject import DisplayObject
import src.Constants as const


class MapObject(DisplayObject, ABC):

    def __init__(self, position: Tuple[int, int], texture: str, collistionRectangleSize: int):
        """
        Object which is displayed on the map and uses collisions
        :param position: Initial position on the map
        :param texture:
        :param collistionRectangleSize: The size of collision can be different from the size of texture displayed
        """
        super().__init__(position)
        self.img: pygame.Surface = pygame.image.load(path.join("images", texture)).convert_alpha()
        self.img = pygame.transform.scale(self.img, (const.BLOCK_SIZE, const.BLOCK_SIZE))
        self.collisionRectangle = pygame.Rect((0, 0), (collistionRectangleSize, collistionRectangleSize))
        self.collisionRectangle.center = self.displayRectangle.center

    def print(self) -> pygame.Surface:
        return self.img

    def position(self) -> Tuple[int, int]:
        return self.displayRectangle.center

    def changePosition(self, position: Tuple[int, int]):
        self.collisionRectangle.center = position
        self.displayRectangle.center = position
