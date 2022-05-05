from typing import Tuple, List

import pygame.time

import src.Constants as const
import src.map.CollisionMap as cm
import src.map.RotatingMapObject as rmo
from Bullet import Bullet


class Player(rmo.RotatingMapObject):

    def __init__(self, position: Tuple[int, int], texture: str):
        super().__init__(position, texture, const.BLOCK_SIZE / 2)

        self.gold = 10
        self.speed = const.PLAYER_SPEED
        self.lastShot = -const.SHOT_COOLDOWN

    def move(self, moveVector: List[int], dt: int, collisionMap: cm.CollisionMap):

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
        elif xMove < 0:
            xMove = min(-1, xMove)
        if yMove > 0:
            yMove = max(1, yMove)
        elif yMove < 0:
            yMove = min(-1, yMove)

        xMove = int(xMove)
        yMove = int(yMove)
        newX = x + xMove
        newY = y + yMove
        newY = max(0, newY)
        newY = min(const.HEIGHT, newY)
        newX = max(0, newX)
        newX = min(const.WIDTH, newX)

        newPosition = (newX, newY)
        destination.center = newPosition

        if collisionMap.isLegalPosition(destination, False, True):
            self.changePosition(newPosition)
            return
        else:
            buildings = collisionMap.getBuildings(destination)
            for building in buildings:
                building.interact(collisionMap, self)

        # Now try to move in one direction if you were trying to move in two at the same time
        if xMove != 0 and yMove != 0:
            newPosition = (x, newY)
            destination.center = newPosition
            if collisionMap.isLegalPosition(destination, False, True):
                self.changePosition(newPosition)
                return
            newPosition = (newX, y)
            destination.center = newPosition

            if collisionMap.isLegalPosition(destination, False, True):
                self.changePosition(newPosition)
                return

        # Now try to move at least a little bit
        if xMove > 0:
            xMove = min(1, xMove)
        elif xMove < 0:
            xMove = max(-1, xMove)
        if yMove > 0:
            yMove = min(1, yMove)
        elif yMove < 0:
            yMove = max(-1, yMove)

        newX = x + xMove
        newY = y + yMove
        newY = max(0, newY)
        newY = min(const.HEIGHT, newY)
        newX = max(0, newX)
        newX = min(const.WIDTH, newX)

        newPosition = (newX, newY)
        destination.center = newPosition

        if collisionMap.isLegalPosition(destination, False, True):
            self.changePosition(newPosition)
            return

    def heal(self, amount: int):
        if self.alive:
            self.currentHealth += amount
            self.currentHealth = min(self.currentHealth, self.maxHealth)
            print(f"player: {self.currentHealth}/{self.maxHealth}")

    def hit(self, damage: int):
        if self.alive:
            self.currentHealth -= damage
            if self.currentHealth <= 0:
                self.currentHealth = max(self.currentHealth, 0)
                self.alive = False

    def rotate(self, targetPosition):
        if self.alive:
            super().rotate(targetPosition)

    def shoot(self, targetPosition) -> List[Bullet]:
        if pygame.time.get_ticks() - self.lastShot > const.SHOT_COOLDOWN:
            newBullet = Bullet(self.position(), targetPosition, 10)
            self.lastShot = pygame.time.get_ticks()
            return [newBullet]
        return []
