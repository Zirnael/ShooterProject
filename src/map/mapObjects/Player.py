from typing import Tuple, List
import src.Constants as const
import src.map.CollisionMap as cm
from src.map.RotatingMapObject import RotatingMapObject


class Player(RotatingMapObject):

    def __init__(self, position: Tuple[int, int], collisionMap: cm.CollisionMap, texture: str):
        super().__init__(position, texture, const.BLOCK_SIZE)

        self.speed = const.PLAYERSPEED
        self.size = (const.BLOCK_SIZE, const.BLOCK_SIZE)
        self.map = collisionMap
        self.health = 10
        self.alive = True

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.alive = False

    def move(self, moveVector: List[int], dt: int):

        if not self.alive:
            return
        x, y = self.displayRectangle.center
        destination = self.displayRectangle.copy()

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
        newY = min(const.HEIGHT, newY)
        newX = max(0, newX)
        newX = min(const.WIDTH, newX)

        newPosition = (newX, newY)
        destination.center = newPosition

        self.changePosition(newPosition)

        if self.map.isLegalPosition(destination):
            self.changePosition(newPosition)
            return

        # Now try to move in one direction if you were trying to move in two at the same time
        if xMove != 0 and yMove != 0:
            newPosition = (x, newY)
            destination.center = newPosition
            if self.map.isLegalPosition(destination):
                self.changePosition(newPosition)
                return
            newPosition = (newX, y)
            destination.center = newPosition

            # TODO Debug
            if self.map.isLegalPosition(destination):
                self.changePosition(newPosition)
                return
