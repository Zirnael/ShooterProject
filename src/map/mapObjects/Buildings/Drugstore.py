import pygame.time

from src.map.mapObjects.Building import Building
from typing import Tuple
import src.Constants as const
from src.map.mapObjects.Player import Player


class Drugstore(Building):
    def __init__(self, texture: str, position: Tuple[int, int], hitPoints: int):
        super().__init__(texture, position, hitPoints)
        self.lastUsed = 0
        self.available = False

    def update(self):
        if not self.available and pygame.time.get_ticks() - self.lastUsed > const.DRUGSTORE_COOLDOWN:
            self.enable()

    def interact(self, player: Player):
        if self.available:
            player.heal(const.DRUGSTORE_RESTORED_HEALTH)
            self.disable()

    def disable(self):
        self.available = False
        self.lastUsed = pygame.time.get_ticks()
        self.img.set_alpha(150)

    def enable(self):
        self.available = True
        self.img.set_alpha(255)
