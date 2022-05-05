from typing import Tuple
import pygame

import Player as p
from Building import Building
from CollisionMap import CollisionMap
import Constants as const


class Headquarters(Building):

    def __init__(self, position: Tuple[int, int], texture: str):
        super().__init__(texture, position, const.HQ_HEALTH, isHQ=True)


    def hit(self, damage: int):
        self.currentHealth -= damage
        if self.currentHealth <= 0:
            self.alive = False

    def update(self, collisionMap: CollisionMap, player: p.Player):
        pass

    def interact(self, collistionMap: CollisionMap, player: p.Player):
        pass
