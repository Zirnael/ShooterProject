from other import Constants as const
import Player as p
from CollisionMap import CollisionMap
from UsableBuilding import UsableBuilding


class Shop(UsableBuilding):
    def __init__(self, texture, position):
        super().__init__(texture, position, const.SHOP_HEALTH, const.SHOP_COOLDOWN, const.SHOP_COST)
        self.img.set_colorkey(const.colors.WHITE)

    def interact(self, collistionMap: CollisionMap, player: p.Player):
        if self.alive and self.available and player.gold >= const.SHOP_EFFECT_COST:
            player.boost(const.SHOP_EFFECT_DURATION)
            player.gold -= const.SHOP_EFFECT_COST
            self.disable()
