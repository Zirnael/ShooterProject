from other import Constants as const
import Player as p
from CollisionMap import CollisionMap
from UsableBuilding import UsableBuilding


class Goldmine(UsableBuilding):

    def __init__(self, texture, position):
        super().__init__(texture, position, const.GOLDMINE_HEALTH, const.GOLDMINE_COOLDOWN, const.GOLDMINE_COST)

    def interact(self, collistionMap: CollisionMap, player: p.Player):
        if self.alive and self.available:
            player.gold += const.GOLDMINE_GOLD
            self.disable()
