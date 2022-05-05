import Player as p
from CollisionMap import CollisionMap
from UsableBuilding import UsableBuilding
import Constants as const


class Shop(UsableBuilding):
    def __init__(self, texture, position):
        super().__init__(texture, position, const.SHOP_HEALTH, const.SHOP_COOLDOWN)
        self.img.set_colorkey(const.colors.WHITE)

    def interact(self, collistionMap: CollisionMap, player: p.Player):
        pass