from abc import ABC, abstractmethod
from os import path
from typing import Tuple
import pygame

from src.display.DisplayObject import DisplayObject
import src.Constants as const


class MapObject(DisplayObject, ABC):

    def __init__(self, position: Tuple[int, int], texture: str, collistionRectangleSize: int, hitPoints: int,
                 displayRectangleSize: int):
        """
        Object which is displayed on the map and uses collisions
        :param size:
        :param hitPoints:
        :param position: Initial position on the map
        :param texture:
        :param collistionRectangleSize: The size of collision can be different from the size of texture displayed
        """
        super().__init__(position, displayRectangleSize)
        self.maxHealth: int = hitPoints
        self.currentHealth: int = hitPoints
        self.alive = True
        self.img: pygame.Surface = pygame.image.load(path.join("images", texture)).convert_alpha()
        self.img = pygame.transform.scale(self.img, (displayRectangleSize, displayRectangleSize))
        self.collisionRectangle = pygame.Rect((0, 0), (collistionRectangleSize, collistionRectangleSize))
        self.collisionRectangle.center = self.displayRectangle.center

    def print(self) -> pygame.Surface:
        return self.img

    def position(self) -> Tuple[int, int]:
        return self.displayRectangle.center

    def changePosition(self, position: Tuple[int, int]):
        self.collisionRectangle.center = position
        self.displayRectangle.center = position

    @abstractmethod
    def hit(self, damage: int):
        """
        Recive damage
        :return:
        """
