from typing import Tuple, List
import src.Constants as const
from src.map.CollisionMap import Map
from src.map.RotatingMapObject import RotatingMapObject


class Player(RotatingMapObject):

    def __init__(self, position: Tuple[int, int], collisionMap: Map, texture: str):
        super().__init__(position, texture)

        self.speed = const.BLOCK_SIZE / 400
        """distance in 1 ms"""

        self.size = (const.BLOCK_SIZE, const.BLOCK_SIZE)
        self.map = collisionMap
        self.health = 10

    def move(self, moveVector: List[int], dt: int):

        x, y = self.rectangle.topleft
        destination = self.rectangle.copy()

        # Try to see if you can stay in new Position
        xMove, yMove = moveVector
        xMove *= self.speed * dt
        yMove *= self.speed * dt
        if xMove > 0:
            xMove = max(1, xMove)
        if yMove > 0:
            yMove = max(1, yMove)

        newX = x + xMove
        newY = y + yMove
        newY = max(0, newY)
        newY = min(const.HEIGHT - self.size[1], newY)
        newX = max(0, newX)
        newX = min(const.WIDTH - self.size[0], newX)

        newPosition = (newX, newY)
        destination.topleft = newPosition
        if self.map.isLegalPosition(destination):
            self.rectangle.topleft = newPosition
            return

        # Now try to move in one direction if you were trying to move in two at the same time
        if xMove != 0 and yMove != 0:
            newPosition = (x, newY)
            destination.topleft = newPosition
            if self.map.isLegalPosition(destination):
                self.rectangle.topleft = newPosition
                return
            newPosition = (newX, y)
            destination.topleft = newPosition
            if self.map.isLegalPosition(destination):
                self.rectangle.topleft = newPosition
                return



