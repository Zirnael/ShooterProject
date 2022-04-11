from typing import Tuple, List
from math import pi, sqrt, acos, asin

import src.Constants as const
from src.map.MapObject import MapObject
from src.map.Map import Map


class Player(MapObject):

    def __init__(self, position: Tuple[int, int], mapObject: Map, texture: str):
        super().__init__(position, texture)

        self.speed = const.BLOCK_SIZE / 250
        """distance in 1 ms"""

        self.size = (const.BLOCK_SIZE, const.BLOCK_SIZE)
        self.map = mapObject
        self.health = 10
        self.angle = 0

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

    def rotate(self, mouse_pos):
        cursorDistance = sqrt(
            (mouse_pos[0] - self.rectangle.center[0]) ** 2 + (mouse_pos[1] - self.rectangle.center[1]) ** 2)

        newAngle = self.angle
        if cursorDistance == 0:
            return
        cosa = (mouse_pos[1] - self.rectangle.center[1]) / cursorDistance
        # print(cosa)
        if abs(mouse_pos[0] - self.rectangle.center[0]) > 0.00001:
            newAngle = (((-mouse_pos[0] + self.rectangle.center[0]) / abs(
                -mouse_pos[0] + self.rectangle.center[0])) * acos(cosa) - pi * (13 / 10)) % (2 * pi)
        else:
            if mouse_pos[1] > self.rectangle.center[1]:
                newAngle = (0 - pi * (13 / 10)) % (2 * pi)
            elif mouse_pos[1] < self.rectangle.center[1]:
                newAngle = (pi - pi * (13 / 10)) % (2 * pi)
        self.angle = newAngle

        '''rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)

        surf.blit(rotated_image, new_rect)
        return angle'''
