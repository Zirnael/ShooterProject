from typing import List

import pygame

import src.Constants as const
from src.display.DisplayHandler import DisplayHandler
from src.map.Map import Map
from src.map.mapObjects.Enemy import Enemy
from src.map.mapObjects.Player import Player
from src.map.MapObject import MapObject


class GameEngine:

    def __init__(self):
        self.displayHandler = DisplayHandler()
        self.moveVector: List[int, int] = [0, 0]
        self.map = Map()
        self.player = Player((0, 0), const.colors.WHITE, self.map)
        self.enemy = Enemy((100, 250), const.colors.RED)
        # self.addObject(self.player)
        self.displayHandler.addObject(self.player)
        self.addObject(self.enemy)

    def progress(self, dt: int):
        """

        :param dt: How much time passed since the last frame
        :return:
        """
        self.player.move(self.moveVector, dt)
        self.displayHandler.print()

    def keyPress(self, key):
        """
        Change MoveVector based on input
        :param key:
        :return:
        """
        if key == pygame.K_LEFT:
            self.moveVector[0] -= 1
        if key == pygame.K_RIGHT:
            self.moveVector[0] += 1
        if key == pygame.K_DOWN:
            self.moveVector[1] += 1
        if key == pygame.K_UP:
            self.moveVector[1] -= 1

    def keyRelese(self, key):
        """
        Change MoveVector based on input
        :param key:
        :return:
        """
        if key == pygame.K_LEFT:
            self.moveVector[0] += 1
        if key == pygame.K_RIGHT:
            self.moveVector[0] -= 1
        if key == pygame.K_DOWN:
            self.moveVector[1] -= 1
        if key == pygame.K_UP:
            self.moveVector[1] += 1

    def addObject(self, newObject: MapObject):
        self.displayHandler.addObject(newObject)
        self.map.addObject(newObject.rectangle)
