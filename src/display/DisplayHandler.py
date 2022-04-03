import pygame
from typing import List

from src.display.DisplayObject import DisplayObject
import src.Constants as const


class DisplayHandler:
    def __init__(self):
        from src.Constants import WIDTH, HEIGHT
        self.screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.objects: List[DisplayObject] = []

    def print(self) -> None:
        """
        Display all the objects onto the pygame display
        :return: None
        """
        self.screen.fill(const.colors.GREEN)  # background

        for obj in self.objects:
            miniSurface = obj.print()
            self.screen.blit(miniSurface, obj.rectangle.topleft)

        pygame.display.flip()

    def addObject(self, newObject: DisplayObject) -> None:
        """
        Add an object for the displayHandler to handle

        :param newObject: DisplayObject
        :return: None
        """
        self.objects.append(newObject)
