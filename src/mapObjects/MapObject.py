from abc import ABC

import pygame

from src.display.DisplayObject import DisplayObject
import src.Constants as const


class MapObject(DisplayObject, ABC):

    def __init__(self, position):
        super().__init__(position)
        # TODO self.image


