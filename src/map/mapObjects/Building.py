from typing import Tuple

from abc import ABC, abstractmethod

import pygame

import src.map.MapObject as mo
import src.Constants as const
import src.map.mapObjects.Player as p
from CollisionMap import CollisionMap


class Building(mo.MapObject, ABC):
    def __init__(self, texture: str, position: Tuple[int, int], hitPoints: int, isHQ=False):
        self.isHQ = isHQ
        if isHQ:
            super().__init__(position, texture, const.BLOCK_SIZE * 2 - 5, hitPoints, const.BLOCK_SIZE * 2)
        else:
            super().__init__(position, texture, const.BLOCK_SIZE - 5, hitPoints, const.BLOCK_SIZE)

    @abstractmethod
    def update(self, collisionMap: CollisionMap, player: p.Player):
        """
        Every frame a building gets to do whatever it is supposed to
        :return:
        """

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
        self.img.set_alpha(50)

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
                                 (max(const.BLOCK_SIZE * 2 * self.currentHealth / self.maxHealth - 3, 0),
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
