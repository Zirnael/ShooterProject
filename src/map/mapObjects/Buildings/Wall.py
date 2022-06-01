from typing import Tuple

from other import Constants as const
import Building as b
import src.map.mapObjects.Player as p
from CollisionMap import CollisionMap


class Wall(b.Building):

    def __init__(self, texture: str, position: Tuple[int, int]):
        super().__init__(texture, position, const.WALL_HEALTH, const.WALL_COST)

    def update(self, collisionMap: CollisionMap, player: p.Player):
        super().update(collisionMap, player)

    def interact(self, collistionMap: CollisionMap, player: p.Player):
        pass
