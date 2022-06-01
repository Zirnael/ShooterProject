from typing import Optional

import CollisionMap as cm
import other.Constants as const
from Enemies.Enemy import Enemy
from MapObject import MapObject


class BossEnemy(Enemy):
    def __init__(self, position, texture, target):
        super().__init__(position=position,
                         texture=texture,
                         collistionRectangleSize=2 * const.BLOCK_SIZE,
                         hitPoints=const.ENEMY_BOSS_HEALTH,
                         displayRectangleSize=2 * const.BLOCK_SIZE,
                         target=target,
                         speed=const.ENEMY_BOSS_SPEED,
                         isRotating=False,
                         damage=const.ENEMY_BOSS_DAMAGE,
                         hitDelay=const.ENEMY_BOSS_HITDELAY,
                         wiggle=0)

        self.img.set_colorkey(const.colors.WHITE)

    def move(self, dt: int, collisionMap: cm.CollisionMap, considerBuildings=True, considerEnemies=True) -> Optional[
        MapObject]:
        return super().move(dt, collisionMap, True, False)
