import pygame
from typing import List
import src.Constants as const


class CollisionMap:
    def __init__(self):
        self.buildings = []
        self.buildingsRect: List[pygame.rect] = []
        self.enemies = []
        self.enemiesRect: List[pygame.rect] = []
        self.player = None
        self.entireScreen: pygame.Rect = pygame.Rect(0, 0, const.WIDTH, const.HEIGHT)

    def addEnemy(self, newEnemy):
        self.enemies.append(newEnemy)
        self.enemiesRect.append(newEnemy.collisionRectangle)

    def removeEnemy(self, delEnemy):
        try:
            self.enemies.remove(delEnemy)
            self.enemiesRect.remove(delEnemy.collisionRectangle)
        except ValueError:
            pass

    def addBuilding(self, newBuilding):
        self.buildings.append(newBuilding)
        self.buildingsRect.append(newBuilding.collisionRectangle)

    def removeBuilding(self, delBuilding):
        try:
            self.buildings.remove(delBuilding)
            self.buildingsRect.remove(delBuilding.collisionRectangle)
        except ValueError:
            pass

    def isLegalPosition(self, destination: pygame.Rect, callerEnemy=None) -> bool:
        if not self.entireScreen.contains(destination):
            return False
        
        copyEnemiesRect = self.enemiesRect.copy()
        try:
            copyEnemiesRect.remove(callerEnemy.collisionRectangle)
        except (ValueError, AttributeError):
            pass
        if destination.collidelist(copyEnemiesRect) != -1:
            return False
        if destination.collidelist(self.buildingsRect) != -1:
            return False

        return True

    def doesOverlapPlayer(self, rect: pygame.Rect) -> bool:
        if self.player is None:
            return False
        return self.player.collisionRectangle.colliderect(rect)

    def getBuilding(self, rect: pygame.Rect):
        index = rect.collidelist(self.buildingsRect)
        if index == -1:
            return None
        return self.buildings[index]

    def assignPlayer(self, player):
        self.player = player
