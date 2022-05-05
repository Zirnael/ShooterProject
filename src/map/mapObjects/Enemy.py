from typing import Tuple, Optional

from math import sqrt

import pygame
import random

import src.Constants as const
import src.map.CollisionMap as cm
import src.map.RotatingMapObject as rmo
from src.map.MapObject import MapObject


class Enemy(rmo.RotatingMapObject):

    def __init__(self, position: Tuple[int, int], texture: str):
        super().__init__(position, texture, const.ENEMY_COLLISION_SIZE)
        self.damage: int = 1
        self.hitDelay: int = -const.AFTER_HIT_DELAY
        self.speed: float = const.ENEMY_SPEED * (random.random() + 0.5)

    def simpleMove(self, dt: int, targetPosition: tuple[int, int], collisionMap: cm.CollisionMap) -> Optional[
        MapObject]:
        """
        Move in target direction
        :param collisionMap:
        :param dt:
        :param targetPosition:
        :return: True if hit the target, otherwise false
        """
        if pygame.time.get_ticks() - self.hitDelay < const.AFTER_HIT_DELAY:
            return None
        xTarget, yTarget = targetPosition
        xMe, yMe = self.displayRectangle.center

        xDiff = abs(xTarget - xMe)
        yDiff = abs(yTarget - yMe)

        travelDistance = self.speed * dt
        travelDistance = max(1, int(travelDistance))

        if xDiff < travelDistance:
            newX = xTarget + self.randomMoveDistance(dt, xDiff)
        else:
            signX = (xTarget - xMe) / xDiff
            newX = xMe + travelDistance * signX + self.randomMoveDistance(dt, xDiff)
        if yDiff < travelDistance:
            newY = yTarget + self.randomMoveDistance(dt, yDiff)
        else:
            signY = (yTarget - yMe) / yDiff
            newY = yMe + travelDistance * signY + self.randomMoveDistance(dt, yDiff)

        """Calculated new position"""
        newPosition = (newX, newY)
        destination = self.collisionRectangle.copy()
        destination.center = newPosition
        if collisionMap.doesOverlapPlayer(destination):
            self.hitDelay = pygame.time.get_ticks()
            return collisionMap.player
        attackedBuilding = collisionMap.getBuilding(destination)
        if attackedBuilding is not None:
            self.hitDelay = pygame.time.get_ticks()
            return attackedBuilding

        if collisionMap.isLegalPosition(destination, True, True, callerEnemy=self):
            self.changePosition(newPosition)
        return None

    def hit(self, damage: int):
        self.currentHealth -= damage
        if self.currentHealth <= 0:
            self.alive = False
            self.shouldDisplay = False

    def randomMoveDistance(self, dt: int, differenceInPositions) -> float:
        """
        :param dt:
        :param differenceInPositions: The bigger the difference the less wiggle
        :return:
        """
        if differenceInPositions < const.BLOCK_SIZE:
            multiplier = 3
        else:
            multiplier = 1

        return random.random() * self.speed * dt * random.choice([-1, 1]) * multiplier

    def diagonalMove(self, dt: int, targetPosition: tuple[int, int]):
        """
        Move in player's direction
        :param targetPosition:
        :param dt:
        :return:
        """
        xTarget, yTarget = targetPosition
        xMe, yMe = self.displayRectangle.center

        xDiff = abs(xTarget - xMe)
        yDiff = abs(yTarget - yMe)
        distance = sqrt(xDiff ** 2 + yDiff ** 2)
        travelDistance = self.speed * dt

        if xDiff == 0:
            newXDiff = 0
            newYDiff = yDiff - travelDistance
            newYDiff = max(0, newYDiff)
        elif yDiff == 0:
            newYDiff = 0
            newXDiff = xDiff - travelDistance
            newXDiff = max(0, newXDiff)
        else:
            newXDiff = sqrt((distance - travelDistance) ** 2 / (1 + yDiff ** 2 / xDiff ** 2))
            newXDiff = min(xDiff - 1, newXDiff)
            newYDiff = newXDiff * yDiff / xDiff
            newYDiff = min(yDiff - 1, newYDiff)

        if xMe < xTarget:
            newX = xTarget - newXDiff
        else:
            newX = xTarget + newXDiff
        if yMe < yTarget:
            newY = yTarget - newYDiff
        else:
            newY = yTarget + newYDiff

        self.displayRectangle.center = (newX, newY)

    def print(self):
        res = super().print()
        pygame.draw.line(res, const.colors.RED, (3, const.BLOCK_SIZE), (const.BLOCK_SIZE - 3, const.BLOCK_SIZE), 5)
        pygame.draw.line(res, const.colors.GREEN, (3, const.BLOCK_SIZE),
                         (max(const.BLOCK_SIZE * self.currentHealth / self.maxHealth - 3, 0), const.BLOCK_SIZE), 5)
        return res