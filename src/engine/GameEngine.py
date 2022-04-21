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
from src.map.mapObjects.Buildings.Wall import Wall
from src.display.BottomBar import BottomBar


class GameEngine:

    def __init__(self):
        self.displayHandler = DisplayHandler()
        self.moveVector: List[int, int] = [0, 0]
        self.map = CollisionMap()
        self.player = Player((0, 0), "player.png")

        self.enemies: List[Enemy] = []
        for i in range(2):
            newEnemy = Enemy((i * const.BLOCK_SIZE, 2*const.BLOCK_SIZE), "enemy.png")
            self.addEnemy(newEnemy)

        self.buildings: List[Building] = []

        self.addBuilding(Drugstore("drugstore.png", (2 * const.BLOCK_SIZE, 3 * const.BLOCK_SIZE), 10))
        self.addBuilding(Wall("wall.jpg", (3 * const.BLOCK_SIZE, 3 * const.BLOCK_SIZE), 10))

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
            self.player.move(self.moveVector, dt, self.map)

        self.player.rotate(self.mousePosition)
        for enemy in self.enemies:
            hitObject = enemy.simpleMove(dt, self.player.position(), self.map)
            if hitObject is not None:
                hitObject.hit(enemy.damage)
            enemy.rotate(self.player.position())

        for building in self.buildings:
            building.update()
            if not building.alive:
                self.map.removeBuilding(building)
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

    def addNonCollidingObject(self, newObject: MapObject):
        self.displayHandler.addObject(newObject)

    def addEnemy(self, newEnemy):
        self.enemies.append(newEnemy)
        self.displayHandler.addObject(newEnemy)
        self.map.addEnemy(newEnemy)

    def addBuilding(self, newBuilding):
        self.buildings.append(newBuilding)
        self.displayHandler.addObject(newBuilding)
        self.map.addBuilding(newBuilding)

    def addPlayer(self):
        self.displayHandler.addObject(self.player)
        self.map.assignPlayer(self.player)

    def updateMousePosition(self, position):
        self.mousePosition = position
        self.player.rotate(position)
