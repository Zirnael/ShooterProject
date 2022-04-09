import pygame
from src.Constants import HEIGHT,WIDTH,SCREEN_HEIGHT,BOTTOM_BAR_HEIGHT,colors
from src.engine import GameEngine
from src.display.DisplayObject import DisplayObject
from typing import Tuple
from src.map.mapObjects.Player import Player



class BottomBar(DisplayObject):
    def __init__(self, position: Tuple[int, int],texture: str,player: Player):
        super().__init__(position, texture)
        self.position: Tuple[int, int] = position
        self.rectangle = pygame.Rect((0,HEIGHT), (WIDTH,SCREEN_HEIGHT-BOTTOM_BAR_HEIGHT))
        self.surface = pygame.Surface((WIDTH,SCREEN_HEIGHT-BOTTOM_BAR_HEIGHT))
        self.player = player
        self.topleft = position


    def print(self) -> pygame.Surface:
        if pygame.font:
            font = pygame.font.Font(None, 32)
            health_value = self.player.health
            text = font.render("Health : " + str(health_value), True, (255, 255, 255))
            textpos = text.get_rect(left=10, bottom=SCREEN_HEIGHT - BOTTOM_BAR_HEIGHT / 2)
            self.surface.blit(text,textpos)
            return self.surface
