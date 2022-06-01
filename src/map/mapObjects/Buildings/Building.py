from abc import ABC, abstractmethod
from typing import Tuple

import pygame

import other.Constants as const
import src.map.MapObject as mo
import src.map.mapObjects.Player as p
from CollisionMap import CollisionMap


class Building(mo.MapObject, ABC):
    def __init__(self, texture: str, position: Tuple[int, int], hitPoints: int, cost=0, isHQ=False):
        self.isHQ = isHQ
        self.cost = cost
        self.disappearStart = 0

        if isHQ:
            super().__init__(position, texture, const.BLOCK_SIZE * 2 - 5, hitPoints, const.BLOCK_SIZE * 2)
        else:
            super().__init__(position, texture, const.BLOCK_SIZE - 5, hitPoints, const.BLOCK_SIZE)

    def update(self, collisionMap: CollisionMap, player: p.Player):
        """
        Every frame a building gets to do whatever it is supposed to
        :return:
        """
        if not self.alive and pygame.time.get_ticks() - self.disappearStart > const.BUILDING_DISAPPEAR_TIME:
            self.shouldDisplay = False

    @abstractmethod
    def interact(self, collistionMap: CollisionMap, player: p.Player):
        """
        Interact with a player if the player steps onto the building
        :return:
        """

    def destroyed(self):
        """
        Method is called when the building gets destroyed
        :return:
        """
        self.img.set_alpha(100)
        self.disappearStart = pygame.time.get_ticks()

    def hit(self, damage: int):
        """
        Method is called when the building get hit by the enemy
        :param damage:
        :return:
        """
        self.currentHealth -= damage
        if self.currentHealth <= 0:
            self.alive = False
            self.destroyed()

    def print(self) -> pygame.Surface:
        if self.isHQ:
            pygame.draw.line(self.img, const.colors.RED, (3, const.BLOCK_SIZE * 2),
                             (const.BLOCK_SIZE * 2 - 3, const.BLOCK_SIZE * 2), 5)
            if self.alive:
                pygame.draw.line(self.img, const.colors.GREEN, (3, const.BLOCK_SIZE * 2),
                                 (max(const.BLOCK_SIZE * 2 * self.currentHealth / self.maxHealth - 3, 3),
                                  const.BLOCK_SIZE * 2),
                                 5)
        else:
            pygame.draw.line(self.img, const.colors.RED, (3, const.BLOCK_SIZE),
                             (const.BLOCK_SIZE - 3, const.BLOCK_SIZE), 5)
            if self.alive:
                pygame.draw.line(self.img, const.colors.GREEN, (3, const.BLOCK_SIZE),
                                 (max(const.BLOCK_SIZE * self.currentHealth / self.maxHealth - 3, 0), const.BLOCK_SIZE),
                                 5)

        return self.img
