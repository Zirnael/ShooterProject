import pygame
from typing import List
from os import chdir, path

from src.display.DisplayObject import DisplayObject
import src.Constants as const

chdir(r"..\map")


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
        img = pygame.image.load(path.join("images", "grass.jpg")).convert_alpha()
        img = pygame.transform.scale(img, (const.BLOCK_SIZE, const.BLOCK_SIZE))
        for i in range(const.MAP_SIZE):
            for j in range(const.MAP_SIZE):
                self.screen.blit(img, pygame.Rect((const.BLOCK_SIZE * i, const.BLOCK_SIZE * j),
                                                  (const.BLOCK_SIZE, const.BLOCK_SIZE)))

        # self.screen.fill(const.colors.GREEN)  # background

        for obj in self.objects:
            miniSurface = obj.print()
            self.screen.blit(miniSurface, obj.rectangle.topleft)

        pygame.display.flip()

    def addObject(self, newObject: DisplayObject):
        self.objects.append(newObject)
