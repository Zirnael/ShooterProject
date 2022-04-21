import pygame

from typing import Tuple
from src.map.MapObject import MapObject
from math import degrees, sqrt, pi, acos
from abc import ABC


class RotatingMapObject(MapObject, ABC):
    def __init__(self, position: Tuple[int, int], texture: str, collisionRectangleSize: int):
        super().__init__(position, texture, collisionRectangleSize, 10)
        self.angle: float = 0

    def print(self) -> pygame.Surface:
        orig_rect = self.img.get_rect()
        rot_image = pygame.transform.rotate(self.img, -degrees(self.angle))
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

    def rotate(self, targetPosition):
        cursorDistance = sqrt(
            (targetPosition[0] - self.displayRectangle.center[0]) ** 2 + (
                        targetPosition[1] - self.displayRectangle.center[1]) ** 2)

        newAngle = self.angle
        if cursorDistance == 0:
            return
        cosa = (targetPosition[1] - self.displayRectangle.center[1]) / cursorDistance
        # print(cosa)
        if abs(targetPosition[0] - self.displayRectangle.center[0]) > 0.00001:
            newAngle = (((-targetPosition[0] + self.displayRectangle.center[0]) / abs(
                -targetPosition[0] + self.displayRectangle.center[0])) * acos(cosa) - pi * (13 / 10)) % (2 * pi)
        else:
            if targetPosition[1] > self.displayRectangle.center[1]:
                newAngle = (0 - pi * (13 / 10)) % (2 * pi)
            elif targetPosition[1] < self.displayRectangle.center[1]:
                newAngle = (pi - pi * (13 / 10)) % (2 * pi)
        self.angle = newAngle

        '''rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)

        surf.blit(rotated_image, new_rect)
        return angle'''
