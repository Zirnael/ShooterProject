from abc import abstractmethod, ABC
from typing import Tuple
import src.Constants as const
import pygame
import os.path

os.chdir(r"..\display")
class DisplayObject(ABC):
    def __init__(self, position: Tuple[int, int],*argv):
        self.position: Tuple[int, int] = position
        """Current position on a map"""
        self.rectangle = pygame.Rect(position, (const.BLOCK_SIZE, const.BLOCK_SIZE))
        """Structure to hold position and check for collisions"""

    @abstractmethod
    def print(self):


        ''' Create and return Surface with size of Block representing an object.

        It will then be drawn onto the screen in appropriate block on map'''


