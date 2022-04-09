import pygame
from typing import List
from os import chdir, path

from src.display.DisplayObject import DisplayObject
import src.Constants as const
from src.Constants import WIDTH, HEIGHT, BOTTOM_BAR_HEIGHT ,SCREEN_HEIGHT, BLOCK_SIZE
chdir(r"..\map")


class DisplayHandler:
    def __init__(self):

        self.screen: pygame.Surface = pygame.display.set_mode((WIDTH, SCREEN_HEIGHT))
        self.objects: List[DisplayObject] = []
        self.background: pygame.Surface = pygame.image.load(path.join("images", "grass.jpg")).convert_alpha()
        self.background = pygame.transform.scale(self.background, (BLOCK_SIZE, BLOCK_SIZE))

    def print(self) -> None:
        """
        Display all the objects onto the pygame display
        :return: None
        """
        for i in range(const.MAP_SIZE):
            for j in range(const.MAP_SIZE):
                self.screen.blit(self.background, pygame.Rect((BLOCK_SIZE * i, BLOCK_SIZE * j),
                                                  (BLOCK_SIZE, BLOCK_SIZE)))


        # self.screen.fill(const.colors.GREEN)  # background

        for obj in self.objects:
            miniSurface = obj.print()
            self.screen.blit(miniSurface, obj.rectangle.topleft)


        pygame.display.flip()

    def addObject(self, newObject: DisplayObject):
        self.objects.append(newObject)
