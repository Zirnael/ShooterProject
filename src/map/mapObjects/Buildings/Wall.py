import src.map.mapObjects.Building as b
import src.map.mapObjects.Player as p
from typing import Tuple


class Wall(b.Building):

    def __init__(self, texture: str, position: Tuple[int, int], hitPoints: int):
        super().__init__(texture, position, hitPoints)

    def update(self):
        pass

    def interact(self, player: p.Player):
        pass
