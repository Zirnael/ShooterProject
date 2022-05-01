# Weird stuff to make typing without circular imports
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.map.mapObjects.Player import Player
    from src.map.mapObjects.Enemy import Enemy
    from src.map.mapObjects.Building import Building
# End of weird stuff

import pygame
from typing import List
import src.Constants as const


class CollisionMap:
    def __init__(self, player: Player):
        self.buildings: List[Building] = []
        self.buildingsRect: List[pygame.rect] = []
        self.enemies: List[Enemy] = []
        self.enemiesRect: List[pygame.rect] = []
        self.player: Player = player
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
