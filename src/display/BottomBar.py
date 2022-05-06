from os import path
from typing import Tuple

import pygame

import src.Constants as const
from src.display.DisplayObject import DisplayObject
from src.map.mapObjects.Player import Player


class BottomBar(DisplayObject):
    def __init__(self, position: Tuple[int, int], player: Player, buildingTypes):
        super().__init__(position, const.BLOCK_SIZE)
        buildings = [("wall.jpg", 5), ("shop.png", 10)]
        self.buildingTypes = buildingTypes
        self.images = []
        for texture, _, price in self.buildingTypes:
            img = pygame.image.load(path.join("images", texture)).convert_alpha()
            img = pygame.transform.scale(img, (const.ICON_SIZE, const.ICON_SIZE))
            self.images.append((img, price))

        self.player = player
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def print(self) -> pygame.Surface:
        res = pygame.Surface((const.WIDTH, const.BOTTOM_BAR_HEIGHT))
        health_value = self.player.currentHealth
        text = self.font.render(f"Health: {self.player.currentHealth}/{self.player.maxHealth} Gold: {self.player.gold}",
                                False, const.colors.WHITE)
        res.blit(text, (10, 0))
        textEnd = text.get_width() + 20
        for i, (img, price) in enumerate(self.images):
            offset = i * (const.ICON_SIZE + 10)
            res.blit(img, (textEnd + offset, 5))
            text = self.font.render(str(price), False, const.colors.WHITE)
            w = text.get_width()
            res.blit(text, (textEnd + offset + const.ICON_SIZE / 2 - w / 2, 10 + const.ICON_SIZE))
        return res
