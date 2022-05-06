from typing import Tuple

import src.Constants as const
from CollisionMap import CollisionMap
from UsableBuilding import UsableBuilding
from src.map.mapObjects.Player import Player


class Drugstore(UsableBuilding):

    def __init__(self, texture: str, position: Tuple[int, int]):
        super().__init__(texture, position, const.DRUGSTORE_HEALTH, const.DRUGSTORE_COOLDOWN, const.DRUGSTORE_COST)

    def interact(self, collistionMap: CollisionMap, player: Player):
        if self.alive and self.available:
            player.heal(const.DRUGSTORE_RESTORED_HEALTH)
            self.disable()
