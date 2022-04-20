from typing import Tuple

from math import pi, sqrt, acos, asin

import pygame
import random

import src.Constants as const
from src.map import CollisionMap
from src.map.CollisionMap import CollisionMap
from src.map.RotatingMapObject import RotatingMapObject


class Enemy(RotatingMapObject):

    def __init__(self, position: Tuple[int, int], collisionMap: CollisionMap, texture: str):
        super().__init__(position, texture, const.ENEMYCOLLISIONSIZE)
        self.hitDelay: int = 0
        self.speed: float = const.ENEMYSPEED * (random.random() + 0.5)
        self.map: CollisionMap = collisionMap

    def simpleMove(self, dt: int, targetPosition: tuple[int, int]):
        """
        Move in target direction
        :param dt:
        :param targetPosition:
        :return:
        """
        if pygame.time.get_ticks() - self.hitDelay < const.AFTERHITDELAY:
            return
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

        newPosition = (newX, newY)
        destination = self.collisionRectangle.copy()
        destination.center = newPosition
        if self.map.doesOverlapPlayer(destination):
            print("hit!")
            self.hitDelay = pygame.time.get_ticks()
            return
        if self.map.isLegalPosition(destination, self.collisionRectangle):
            self.changePosition(newPosition)

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

        print(xMe, xDiff, newXDiff, newX - xTarget)
        self.displayRectangle.center = (newX, newY)

    def dijkstraMove(self):
        """
        Use dijkstra algorithm to find optimal path to the target
        :return:
        """
