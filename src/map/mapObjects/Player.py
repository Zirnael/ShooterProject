from typing import Tuple, List

import src.Constants as const
from src.map.MapObject import MapObject
from src.map.Map import Map


class Player(MapObject):

    def __init__(self, position: Tuple[int, int], color: Tuple[int, int, int], map: Map):
        super().__init__(position, color)
        self.speed = const.BLOCK_SIZE * 0.2 / 60
        self.size = (const.BLOCK_SIZE, const.BLOCK_SIZE)
        self.map = map

    def move(self, moveVector: List[int], dt: int):
        x, y = self.rectangle.topleft
        destination = self.rectangle.copy()

        # Try to see if you can stay in new Position
        xMove, yMove = moveVector
        xMove *= self.speed * dt
        yMove *= self.speed * dt
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
