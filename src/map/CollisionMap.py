# Weird stuff to make typing without circular imports
from __future__ import annotations

import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.map.mapObjects.Player import Player
    from src.map.mapObjects.Enemy import Enemy
    from src.map.mapObjects.Building import Building
# End of weird stuff

import pygame
from typing import List
import src.Constants as const
from LineIntersect import rectIntersect


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

    def isLegalPosition(self, destination: pygame.Rect, considerEnemies=True, considerBuildings=True,
                        considerPlayer=False,
                        callerEnemy=None) -> bool:

        if not self.entireScreen.contains(destination):
            return False

        copyEnemiesRect = self.enemiesRect.copy()
        try:
            copyEnemiesRect.remove(callerEnemy.collisionRectangle)
        except (ValueError, AttributeError):
            pass
        if considerEnemies and destination.collidelist(copyEnemiesRect) != -1:
            return False
        if considerBuildings and destination.collidelist(self.buildingsRect) != -1:
            return False
        if considerPlayer and self.doesOverlapPlayer(destination):
            return False

        return True

    def doesOverlapPlayer(self, rect: pygame.Rect) -> bool:
        if self.player is None:
            return False
        return self.player.collisionRectangle.colliderect(rect)

    def getBuildings(self, rect: pygame.Rect):
        indexes = rect.collidelistall(self.buildingsRect)
        res = []
        for index in indexes:
            res.append(self.buildings[index])

        return res

    def getEnemy(self, rect: pygame.Rect):
        index = rect.collidelist(self.enemiesRect)
        if index == -1:
            return None
        return self.enemies[index]

    def assignPlayer(self, player):
        self.player = player

    def getEnemyPoint(self, position):
        for i, enemy in enumerate(self.enemiesRect):
            enemy: pygame.Rect
            if enemy.collidepoint(position):
                return self.enemies[i]
        return None

    def getEnemyLine(self, line):
        for i, enemy in enumerate(self.enemies):
            enemy: Enemy
            if rectIntersect(enemy.displayRectangle, line) is not None:
                return self.enemies[i]
        return None

    def getRandomEnemy(self):
        leng = len(self.enemies)
        if leng == 0:
            return None
        return self.enemies[random.randint(0, len(self.enemies) - 1)]

    def getBuilding(self, rect):
        index = rect.collidelist(self.buildingsRect)
        if index == -1:
            return None
        return self.buildings[index]


