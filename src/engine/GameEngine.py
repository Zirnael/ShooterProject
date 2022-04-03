import pygame

from src.display.DisplayHandler import DisplayHandler


class GameEngine:

    def __init__(self):
        self.displayHandler = DisplayHandler()

    def progress(self):
        self.displayHandler.print()


