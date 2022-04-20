from typing import Tuple

from math import pi, sqrt, acos, asin
import src.Constants as const
from src.map.CollisionMap import Map
from src.map.RotatingMapObject import RotatingMapObject


class Enemy(RotatingMapObject):

    def __init__(self, position: Tuple[int, int], collisionMap: Map, texture: str):
        super().__init__(position, texture)
        self.speed = const.BLOCK_SIZE / 500
        self.map = collisionMap

    def simpleMove(self, dt: int, targetPosition: tuple[int, int]):
        """
        Move in target direction
        :param dt:
        :param targetPosition:
        :return:
        """
        xTarget, yTarget = targetPosition
        xMe, yMe = self.rectangle.center

        xDiff = abs(xTarget - xMe)
        yDiff = abs(yTarget - yMe)

        travelDistance = self.speed * dt
        travelDistance = max(1, travelDistance)

        if xDiff < travelDistance:
            newX = xTarget
        else:
            signX = (xTarget - xMe) / xDiff
            newX = xMe + travelDistance * signX
        if yDiff < travelDistance:
            newY = yTarget
        else:
            signY = (yTarget - yMe) / yDiff
            newY = yMe + travelDistance * signY

        self.rectangle.center = (newX, newY)
        print(newX, newY)

    def diagonalMove(self, dt: int, targetPosition: tuple[int, int]):
        """
        Move in player's direction
        :param targetPosition:
        :param dt:
        :return:
        """
        xTarget, yTarget = targetPosition
        xMe, yMe = self.rectangle.center

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
        self.rectangle.center = (newX, newY)

    def dijkstraMove(self):
        """
        Use dijkstra algorithm to find optimal path to the target
        :return:
        """
