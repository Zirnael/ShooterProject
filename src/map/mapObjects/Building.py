from typing import Tuple

from abc import ABC, abstractmethod
from src.map.MapObject import MapObject
import src.Constants as const
from src.map.mapObjects.Player import Player


class Building(MapObject, ABC):
    def __init__(self, texture: str, position: Tuple[int, int], hitPoints: int):
        super().__init__(position, texture, const.BLOCK_SIZE)
        self.maxHealth: int = hitPoints
        self.currentHealth: int = hitPoints

    @abstractmethod
    def update(self):
        """
        Every frame a building gets to do whatever it is supposed to
        :return:
        """

    @abstractmethod
    def interact(self, player: Player):
        """
        Interact with a player if the player steps onto the building
        :return:
        """
