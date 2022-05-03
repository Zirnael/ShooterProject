import pygame.time

from CollisionMap import CollisionMap
from UsableBuilding import UsableBuilding
from typing import Tuple
import src.Constants as const
from src.map.mapObjects.Player import Player


class Drugstore(UsableBuilding):

    def __init__(self, texture: str, position: Tuple[int, int], hitPoints: int):
        super().__init__(texture, position, hitPoints, const.DRUGSTORE_COOLDOWN)

    def interact(self, collistionMap: CollisionMap, player: Player):
        if self.alive and self.available:
            player.heal(const.DRUGSTORE_RESTORED_HEALTH)
            self.disable()
