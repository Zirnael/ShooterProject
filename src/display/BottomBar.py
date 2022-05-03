import pygame
import src.Constants as const
from src.engine import GameEngine
from os import path
from src.display.DisplayObject import DisplayObject
from typing import Tuple
from src.map.mapObjects.Player import Player


class BottomBar(DisplayObject):
    def __init__(self, position: Tuple[int, int], player: Player):
        super().__init__(position)
        self.player = player
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    # TODO Display bottom bar with health

    def print(self) -> pygame.Surface:
        res = pygame.Surface((const.WIDTH, const.BOTTOM_BAR_HEIGHT))
        health_value = self.player.currentHealth
        text = self.font.render(f"Health: {self.player.currentHealth}/{self.player.maxHealth} Gold: {self.player.gold}",
                                False, const.colors.WHITE)
        textEnd = text.get_width() + 20
        # pygame.image.load(path.join("images", texture)).convert_alpha()
        res.blit(text, (10, 0))
        return res
