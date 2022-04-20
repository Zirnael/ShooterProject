from typing import List

import pygame

import src.Constants as const
from src.display.DisplayHandler import DisplayHandler
from src.map.CollisionMap import Map
from src.map.mapObjects.Enemy import Enemy
from src.map.mapObjects.Player import Player
from src.map.MapObject import MapObject
from src.display.BottomBar import BottomBar


class GameEngine:

    def __init__(self):
        self.displayHandler = DisplayHandler()
        self.moveVector: List[int, int] = [0, 0]
        self.map = Map()
        self.player = Player((0, 0), self.map, "player1.png")
        self.enemy = Enemy((100, 250), self.map, "enemy1.png")
        self.displayHandler.addObject(self.player)
        # self.addObject(self.enemy)
        # TODO Debug
        self.addNonCollidingObject(self.enemy)

        self.mousePosition = (0, 0)
        self.bottom_bar = BottomBar((0, const.HEIGHT), "kotek", self.player)
        self.displayHandler.addObject(self.bottom_bar)

    def progress(self, dt: int):
        """

        :param dt: How much time passed since the last frame
        :return:
        """
        if any(self.moveVector):  # move only if some key is pressed
            self.player.move(self.moveVector, dt)
        self.player.rotate(self.mousePosition)
        self.enemy.simpleMove(dt, self.player.position())
        self.enemy.rotate(self.player.position())
        self.displayHandler.print([self.player.position(), self.enemy.position()])

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

    def addColligingObject(self, newObject: MapObject):
        self.displayHandler.addObject(newObject)
        self.map.addObject(newObject.rectangle)

    def addNonCollidingObject(self, newObject: MapObject):
        self.displayHandler.addObject(newObject)

    def updateMousePosition(self, position):
        self.mousePosition = position
        self.player.rotate(position)
