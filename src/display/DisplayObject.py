from abc import abstractmethod, ABC
from typing import Tuple

import pygame


class DisplayObject(ABC):
    def __init__(self, position: Tuple[int, int], offset: Tuple[float, float] = (0, 0)):
        self.position: Tuple[int, int] = position
        self.offset: Tuple[float, float] = offset

    @abstractmethod
    def print(self) -> pygame.Surface:
        """
        Create and return Surface with size of Block representing an object.

        It will then be drawn onto the screen in appropriate block on map

        :return: pygame.Surface
        """
