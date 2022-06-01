from os import path
from typing import Tuple

import pygame

import other.Constants as const
from src.display.DisplayObject import DisplayObject
from src.map.mapObjects.Player import Player


class BottomBar(DisplayObject):
    def __init__(self, position: Tuple[int, int], player: Player, buildingTypes):
        super().__init__(position, const.BLOCK_SIZE)
        self.nextWaveMessage: str = ""
        self.waveCountMessage: str = ""
        self.scoreMessage: str = ""
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
        text = self.font.render(f"Health: {self.player.currentHealth}/{self.player.maxHealth} Gold: {self.player.gold}",
                                False, const.colors.WHITE)
        res.blit(text, (10, 15))
        textEnd = text.get_width() + 20
        text = self.font.render(self.nextWaveMessage, False, const.colors.WHITE)
        res.blit(text, (10, text.get_height() + 25))
        text = self.font.render(self.waveCountMessage, False, const.colors.WHITE)
        res.blit(text, (const.WIDTH - text.get_width() - 25, 15))
        text = self.font.render(self.scoreMessage, False, const.colors.WHITE)
        res.blit(text, (const.WIDTH - text.get_width() - 25, 25 + text.get_height()))
        for i, (img, price) in enumerate(self.images):
            offset = i * (const.ICON_SIZE + 10)
            res.blit(img, (textEnd + offset, 20))
            text = self.font.render(str(price), False, const.colors.WHITE)
            w = text.get_width()
            res.blit(text, (textEnd + offset + const.ICON_SIZE / 2 - w / 2, 25 + const.ICON_SIZE))
        return res
