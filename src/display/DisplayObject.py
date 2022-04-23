from abc import abstractmethod, ABC
from typing import Tuple
import src.Constants as const
import pygame



class DisplayObject(ABC):
    def __init__(self, position: Tuple[int, int]):

        self.displayRectangle = pygame.Rect(position, (const.BLOCK_SIZE, const.BLOCK_SIZE))
        """Structure to hold position"""

    @abstractmethod
    def print(self):
        """ Create and return Surface with size of Block representing an object.

        It will then be drawn onto the screen in appropriate place on map"""
