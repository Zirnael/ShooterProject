from abc import ABC

import pygame

import Player as p
from Building import Building
from CollisionMap import CollisionMap


class UsableBuilding(Building, ABC):
    def __init__(self, texture, position, hitPoints, cooldown, cost):
        super().__init__(texture, position, hitPoints, cost)
        self.lastUsed = pygame.time.get_ticks()
        self.available = False
        self.img.set_alpha(150)
        self.cooldown = cooldown

    def enable(self):
        self.available = True
        self.img.set_alpha(255)

    def disable(self):
        self.available = False
        self.lastUsed = pygame.time.get_ticks()
        self.img.set_alpha(150)

    def update(self, collisionMap: CollisionMap, player: p.Player):
        """Enable if 'cooldown' time has passed
        """
        if self.alive and not self.available and pygame.time.get_ticks() - self.lastUsed > self.cooldown:
            self.enable()
