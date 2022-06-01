import random
from abc import ABC
from typing import Tuple, Optional

import pygame

import CollisionMap as cm
from MapObject import MapObject
from RotatingMapObject import RotatingMapObject
from other import Constants as const


class Enemy(RotatingMapObject, ABC):
    def __init__(self, position: Tuple[int, int], texture: str, collistionRectangleSize: int, hitPoints: int,
                 displayRectangleSize: int, target: MapObject, speed, isRotating, damage, hitDelay, wiggle):
        super().__init__(position, texture, collistionRectangleSize, hitPoints, displayRectangleSize)
        self.target: MapObject = target
        self.damage: int = damage
        self.hitDelayStart: int = 0
        self.hitDelayDuration: int = hitDelay
        self.speed: float = speed
        self.wiggle: int = wiggle
        self.toRotate: bool = isRotating

    def move(self, dt: int, collisionMap: cm.CollisionMap, considerBuildings=True, considerEnemies=True) -> Optional[
        MapObject]:
        """
        Move in target direction
        :param considerEnemies:
        :param considerBuildings:
        :param dt:
        :param targetPosition:
        :param collisionMap:
        :return:
        """
        if pygame.time.get_ticks() - self.hitDelayStart < self.hitDelayDuration:
            return None
        xTarget, yTarget = self.target.position()
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
            self.hitDelayStart = pygame.time.get_ticks()
            return collisionMap.player
        attackedBuilding = collisionMap.getBuilding(destination)
        if attackedBuilding is not None:
            self.hitDelayStart = pygame.time.get_ticks()
            return attackedBuilding

        if collisionMap.isLegalPosition(destination, considerEnemies, considerBuildings, callerEnemy=self,
                                        extendedMap=True):
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

        return random.random() * self.speed * dt * random.choice([-1, 1]) * multiplier * self.wiggle

    def print(self):
        res = super().print(self.toRotate)
        pygame.draw.line(res, const.colors.RED, (3, self.displayRectangle.height - 3),
                         (self.displayRectangle.width - 3, self.displayRectangle.height - 3),
                         width=int(self.displayRectangle.height / const.BLOCK_SIZE * 3))

        pygame.draw.line(res, const.colors.GREEN, (3, self.displayRectangle.height - 3),
                         end_pos=((self.displayRectangle.width - 6) * self.currentHealth / self.maxHealth + 3,
                                  self.displayRectangle.height - 3),
                         width=int(self.displayRectangle.height / const.BLOCK_SIZE * 3))
        return res
