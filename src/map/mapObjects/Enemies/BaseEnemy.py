import random
from typing import Tuple

import CollisionMap as cm
import other.Constants as const
from src.map.mapObjects.Enemies.Enemy import Enemy


class BaseEnemy(Enemy):

    def __init__(self, position: Tuple[int, int], texture: str, target):
        super().__init__(position=position,
                         texture=texture,
                         collistionRectangleSize=const.ENEMY_BASE_COLLISION_SIZE,
                         hitPoints=const.ENEMY_BASE_HITPOINTS,
                         displayRectangleSize=const.BLOCK_SIZE,
                         target=target,
                         speed=const.ENEMY_BASE_SPEED * (random.random() + 0.5),
                         isRotating=True,
                         damage=1,
                         hitDelay=const.ENEMY_BASE_HITDELAY,
                         wiggle=1)
        self.considerEnemies = False

    def move(self, dt: int, collisionMap: cm.CollisionMap, considerBuildings=True, considerEnemies=True):
        res = super().move(dt, collisionMap, considerBuildings, self.considerEnemies)
        if collisionMap.isLegalPosition(self.collisionRectangle, callerEnemy=self, extendedMap=True):
            self.considerEnemies = True

        return res
