import pygame.time

from other import Constants as const
import Player as p
from Building import Building
from Bullet import Bullet
from CollisionMap import CollisionMap


class Turret(Building):

    def __init__(self, texture, position):
        super().__init__(texture, position, const.TURRET_HEALTH, const.TURRET_COST)
        self.lastShot = 0
        self.cooldown = const.TURRET_COOLDOWN
        self.damage = 5
        self.img.set_colorkey(const.colors.WHITE)

    def interact(self, collistionMap: CollisionMap, player: p.Player):
        pass

    def update(self, collisionMap: CollisionMap, player: p.Player):
        super().update(collisionMap, player)
        if not self.alive:
            return
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastShot > self.cooldown:
            enemy = collisionMap.getRandomEnemy()
            if enemy is not None:
                self.lastShot = currentTime
                return [Bullet(self.position(), enemy.position(), self.damage)]
        return []
