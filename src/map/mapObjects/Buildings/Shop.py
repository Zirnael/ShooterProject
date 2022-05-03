import Player as p
from CollisionMap import CollisionMap
from UsableBuilding import UsableBuilding
import Constants as const


class Shop(UsableBuilding):
    def __init__(self, texture, position, hitPoints):
        super().__init__(texture, position, hitPoints, const.SHOP_COOLDOWN)
        self.img.set_colorkey(const.colors.WHITE)

    def interact(self, collistionMap: CollisionMap, player: p.Player):
        pass