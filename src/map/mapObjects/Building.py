from typing import Tuple

from abc import ABC, abstractmethod
import src.map.MapObject as mo
import src.Constants as const
import src.map.mapObjects.Player as p


class Building(mo.MapObject, ABC):
    def __init__(self, texture: str, position: Tuple[int, int], hitPoints: int):
        super().__init__(position, texture, const.BLOCK_SIZE, hitPoints)

    @abstractmethod
    def update(self):
        """
        Every frame a building gets to do whatever it is supposed to
        :return:
        """

    @abstractmethod
    def interact(self, player: p.Player):
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
