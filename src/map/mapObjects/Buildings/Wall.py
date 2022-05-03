import src.map.mapObjects.Building as b
import src.map.mapObjects.Player as p
from typing import Tuple

from CollisionMap import CollisionMap


class Wall(b.Building):

    def __init__(self, texture: str, position: Tuple[int, int], hitPoints: int):
        super().__init__(texture, position, hitPoints)

    def update(self, collisionMap: CollisionMap, player: p.Player):
        pass

    def interact(self, collistionMap:CollisionMap, player: p.Player):
        pass
