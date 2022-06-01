from typing import Tuple

import Player as p
from Building import Building
from CollisionMap import CollisionMap
from other import Constants as const


class Headquarters(Building):
    def __init__(self, position: Tuple[int, int], texture: str):
        super().__init__(texture, position, const.HQ_HEALTH, 10, isHQ=True)
        self.img.set_colorkey(const.colors.WHITE)

    def update(self, collisionMap: CollisionMap, player: p.Player):
        super().update(collisionMap, player)

    def interact(self, collistionMap: CollisionMap, player: p.Player):
        pass
