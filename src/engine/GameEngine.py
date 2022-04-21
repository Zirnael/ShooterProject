from typing import List

import pygame

import src.Constants as const
from src.display.DisplayHandler import DisplayHandler
from src.map.CollisionMap import CollisionMap
from src.map.mapObjects.Building import Building
from src.map.mapObjects.Enemy import Enemy
from src.map.mapObjects.Player import Player
from src.map.MapObject import MapObject
from src.map.mapObjects.Buildings.Drugstore import Drugstore
from src.display.BottomBar import BottomBar


class GameEngine:

    def __init__(self):
        self.displayHandler = DisplayHandler()
        self.moveVector: List[int, int] = [0, 0]
        self.map = CollisionMap()
        self.player = Player((0, 0), self.map, "player.png")

        self.enemies: List[Enemy] = []
        for i in range(0):
            newEnemy = Enemy((i * 40, 200), self.map, "enemy.png")
            self.enemies.append(newEnemy)
            self.addCollidingObject(newEnemy)

        self.buildings: List[Building] = []
        self.buildings.append(Drugstore("drugstore.png", (200, 200), 10))
        self.addCollidingObject(self.buildings[0])
        self.buildings[0].disable()

        self.addPlayer()

        self.mousePosition = (0, 0)
        # self.bottom_bar = BottomBar((0, const.HEIGHT), "kotek", self.player)
        # self.displayHandler.addObject(self.bottom_bar)

    def progress(self, dt: int):
        """

        :param dt: How much time passed since the last frame
        :return:
        """
        if any(self.moveVector):  # move only if some key is pressed
            self.player.move(self.moveVector, dt)
        self.player.rotate(self.mousePosition)

        if self.player.alive:
            for enemy in self.enemies:
                if enemy.simpleMove(dt, self.player.position()):
                    self.player.hit()
                    print(f"hit! {self.player.health}")
                enemy.rotate(self.player.position())

            for building in self.buildings:
                building.update()
        self.displayHandler.print()

    def keyPress(self, key):
        """
        Change MoveVector based on input
        :param key:
        :return:
        """
        if key == pygame.K_LEFT:
            self.moveVector[0] -= 1
        elif key == pygame.K_RIGHT:
            self.moveVector[0] += 1
        elif key == pygame.K_DOWN:
            self.moveVector[1] += 1
        elif key == pygame.K_UP:
            self.moveVector[1] -= 1

    def keyRelese(self, key):
        """
        Change MoveVector based on input
        :param key:
        :return:
        """
        if key == pygame.K_LEFT:
            self.moveVector[0] += 1
        elif key == pygame.K_RIGHT:
            self.moveVector[0] -= 1
        elif key == pygame.K_DOWN:
            self.moveVector[1] -= 1
        elif key == pygame.K_UP:
            self.moveVector[1] += 1

    def addCollidingObject(self, newObject: MapObject):
        self.displayHandler.addObject(newObject)
        self.map.addEnemy(newObject)

    def addNonCollidingObject(self, newObject: MapObject):
        self.displayHandler.addObject(newObject)

    def addPlayer(self):
        self.displayHandler.addObject(self.player)
        self.map.assignPlayer(self.player.collisionRectangle)

    def updateMousePosition(self, position):
        self.mousePosition = position
        self.player.rotate(position)
