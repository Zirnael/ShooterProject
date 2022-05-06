from typing import Tuple

import Constants as const
import Player as p
from Building import Building
from CollisionMap import CollisionMap


class Headquarters(Building):

    def __init__(self, position: Tuple[int, int], texture: str):
        super().__init__(texture, position, const.HQ_HEALTH, 10, isHQ=True)
        self.img.set_colorkey(const.colors.WHITE)

    def hit(self, damage: int):
        self.currentHealth -= damage
        if self.currentHealth <= 0:
            self.alive = False

    def update(self, collisionMap: CollisionMap, player: p.Player):
        pass

    def interact(self, collistionMap: CollisionMap, player: p.Player):
        pass
