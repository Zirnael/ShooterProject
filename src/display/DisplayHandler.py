import pygame
from typing import List
from os import chdir, path

from Bullet import Bullet
from src.display.DisplayObject import DisplayObject
import src.Constants as const

chdir(r"..\map")


class DisplayHandler:
    def __init__(self):

        # self.screen: pygame.Surface = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
        self.screen: pygame.Surface = pygame.display.set_mode((const.WIDTH, const.SCREEN_HEIGHT))
        self.objects: List[DisplayObject] = []
        self.bullets: List[Bullet] = []
        self.background: pygame.Surface = pygame.image.load(path.join("images", "grass.jpg")).convert_alpha()
        self.background = pygame.transform.scale(self.background, (const.BLOCK_SIZE, const.BLOCK_SIZE))

    def print(self, debugPositions=None) -> None:
        """
        Display all the objects onto the pygame display
        :return: None
        """
        for i in range(const.MAP_SIZE):
            for j in range(const.MAP_SIZE):
                self.screen.blit(self.background, pygame.Rect((const.BLOCK_SIZE * i, const.BLOCK_SIZE * j),
                                                              (const.BLOCK_SIZE, const.BLOCK_SIZE)))

        # self.screen.fill(const.colors.GREEN)  # background

        for obj in self.objects:
            miniSurface = obj.print()
            self.screen.blit(miniSurface, obj.displayRectangle.topleft)
        for bullet in self.bullets:
            pygame.draw.line(self.screen, const.colors.YELLOW, bullet.prevPosition, bullet.currentPosition)
        if debugPositions:
            for x in debugPositions:
                pygame.draw.circle(self.screen, const.colors.RED, x, 3)

        pygame.display.flip()

    def addObject(self, newObject: DisplayObject):
        self.objects.append(newObject)

    def addBullet(self, newBullet):
        self.bullets.append(newBullet)
