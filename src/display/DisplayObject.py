from abc import abstractmethod, ABC
from typing import Tuple
import src.Constants as const
import pygame


class DisplayObject(ABC):
    def __init__(self, position: Tuple[int, int], size):
        """

        :param size:
        :param position: Top left corner
        """
        self.shouldDisplay = True
        self.displayRectangle = pygame.Rect(position, (size, size))
        """Structure to hold position"""

    @abstractmethod
    def print(self) -> pygame.Surface:
        """ Create and return Surface representing an object.

        It will then be drawn onto the screen in appropriate place on map"""
