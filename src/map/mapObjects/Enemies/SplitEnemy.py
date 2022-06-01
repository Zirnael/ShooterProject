import random
from typing import Optional

import pygame

import CollisionMap as cm
from Enemies.BaseEnemy import BaseEnemy
from Enemies.Enemy import Enemy
from MapObject import MapObject
from other import Constants as const


class SplitEnemy(Enemy):
    def __init__(self, position, texture, target, addEnemyFunction):
        super().__init__(position=position,
                         texture=texture,
                         collistionRectangleSize=3 * const.ENEMY_BASE_COLLISION_SIZE,
                         hitPoints=const.ENEMY_SPLIT_HEALTH,
                         displayRectangleSize=2 * const.BLOCK_SIZE,
                         target=target,
                         speed=const.ENEMY_SPLIT_SPEED,
                         isRotating=False,
                         damage=const.ENEMY_SPLIT_DAMAGE,
                         hitDelay=const.ENEMY_SPLIT_HITDELAY,
                         wiggle=0)
        self.splitStart = pygame.time.get_ticks() - const.ENEMY_SPLIT_COOLDOWN
        self.splitting: bool = False
        self.addEnemyFunction = addEnemyFunction
        self.img.set_colorkey(const.colors.WHITE)

    def move(self, dt: int, collisionMap: cm.CollisionMap) -> Optional[MapObject]:
        currentTime = pygame.time.get_ticks()
        if not self.splitting and currentTime - self.splitStart < const.ENEMY_SPLIT_COOLDOWN + const.ENEMY_SPLIT_DURATION:
            return super().move(dt, collisionMap, considerEnemies=False)

        if not self.splitting:
            self.splitting = True
            self.splitStart = currentTime
            return
        elif currentTime - self.splitStart > const.ENEMY_SPLIT_DURATION:
            self.split()
            self.splitting = False

    def split(self):
        for _ in range(random.randint(1, 4)):
            self.addEnemyFunction(BaseEnemy(self.position(), "enemy.png", self.target))

    def print(self):
        img = super().print()
        if self.splitting:
            res = img.copy()
            passedTime = pygame.time.get_ticks() - self.splitStart
            pygame.draw.line(res, const.colors.BLUE, (3, self.displayRectangle.height - 8),
                             (max((self.displayRectangle.width - 4) * passedTime / const.ENEMY_SPLIT_DURATION + 3, 3),
                              self.displayRectangle.height - 8),
                             3)
            return res
        return img
