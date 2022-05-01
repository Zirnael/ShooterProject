import pygame

import Constants as const
from math import atan, cos, sin, pi
from CollisionMap import CollisionMap


class Bullet:

    def __init__(self, position, target):
        targetX, targetY = target
        positionX, positionY = position
        yDiff = targetY - positionY
        xDiff = targetX - positionX
        self.angle = atan(yDiff / xDiff)
        if xDiff < 0 and yDiff > 0:
            self.angle = pi / 2 - self.angle
        if xDiff < 0 and yDiff < 0:
            self.angle = self.angle + pi
        self.speed = const.BULLET_SPEED
        # dx = cos(self.angle) * self.speed
        # dy = sin(self.angle) * self.speed
        # self.changeVector = (dx, dy)
        self.prevPosition = position
        lenChangeVector = (cos(self.angle) * const.BULLET_LENGTH, sin(self.angle) * const.BULLET_LENGTH)
        self.currentPosition = [sum(x) for x in zip(self.prevPosition, lenChangeVector)]
        self.screen = pygame.Surface((const.WIDTH, const.SCREEN_HEIGHT))
        self.screen.set_colorkey(const.colors.BLACK)

    def print(self) -> pygame.Surface:
        self.screen.fill(const.colors.BLACK)
        pygame.draw.line(self.screen, const.colors.WHITE, self.prevPosition, self.currentPosition, 3)

        return self.screen

    def move(self, dt: int, collisionMap: CollisionMap = None):
        speed = self.speed * dt / 100
        changeVector = (cos(self.angle) * speed, sin(self.angle) * speed)
        self.currentPosition = [sum(x) for x in zip(self.currentPosition, changeVector)]
        self.prevPosition = [sum(x) for x in zip(self.prevPosition, changeVector)]
