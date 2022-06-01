from math import atan, cos, sin, pi

from CollisionMap import CollisionMap
from other import Constants as const


class Bullet:

    def __init__(self, position, target, damage: int):
        self.damage = damage
        self.alive = True
        targetX, targetY = target
        positionX, positionY = position
        yDiff = targetY - positionY
        xDiff = targetX - positionX
        if xDiff == 0:
            if yDiff > 0:
                self.angle = pi / 2
            else:
                self.angle = -pi / 2
        else:
            self.angle = atan(yDiff / xDiff)
        if xDiff < 0:
            self.angle = self.angle + pi
        self.speed = const.BULLET_SPEED
        self.prevPosition = position
        self.currentPosition = position

    def move(self, dt: int, collisionMap: CollisionMap = None):
        if not self.alive:
            return
        speed = self.speed * dt / 100
        changeVector = (cos(self.angle) * speed, sin(self.angle) * speed)
        distanceSqr = (self.currentPosition[0] - self.prevPosition[0]) ** 2 + (
                self.currentPosition[1] - self.prevPosition[1]) ** 2
        if distanceSqr > const.BULLET_LENGTH ** 2:
            self.prevPosition = [sum(x) for x in zip(self.prevPosition, changeVector)]

        self.currentPosition = [sum(x) for x in zip(self.currentPosition, changeVector)]

        if collisionMap:
            enemy = collisionMap.getEnemyLine((self.prevPosition, self.currentPosition))
            if enemy:
                enemy.hit(self.damage)
                if not enemy.alive:
                    collisionMap.removeEnemy(enemy)

                self.alive = False
        if self.currentPosition[0] < 0 or self.currentPosition[0] > const.WIDTH or self.currentPosition[1] < 0 or \
                self.currentPosition[1] > const.HEIGHT:
            self.alive = False
