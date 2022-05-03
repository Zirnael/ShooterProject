import Player as p
from CollisionMap import CollisionMap
import Constants as const
import pygame

from UsableBuilding import UsableBuilding


class Goldmine(UsableBuilding):

    def __init__(self, texture, position, hitPoints):
        super().__init__(texture, position, hitPoints, const.GOLDMINE_COOLDOWN)

    def interact(self, collistionMap: CollisionMap, player: p.Player):
        if self.alive and self.available:
            player.gold += const.GOLDMINE_GOLD
            self.disable()
