from typing import List

import pygame

import src.Constants as const
from src.display.DisplayHandler import DisplayHandler
from src.map.CollisionMap import CollisionMap
from src.map.mapObjects.Enemy import Enemy
from src.map.mapObjects.Player import Player
from src.map.MapObject import MapObject
from src.display.BottomBar import BottomBar


class GameEngine:

    def __init__(self):
        self.displayHandler = DisplayHandler()
        self.moveVector: List[int, int] = [0, 0]
        self.map = CollisionMap()
        self.player = Player((0, 0), self.map, "player1.png")

        self.enemies = []
        for i in range(3):
            newEnemy = Enemy((i * 40, 200), self.map, "enemy1.png")
            self.enemies.append(newEnemy)
            self.addCollidingObject(newEnemy)

        self.displayHandler.addObject(self.player)
        self.addPlayer()

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

        if self.player.alive:
            for enemy in self.enemies:
                if enemy.simpleMove(dt, self.player.position()):
                    self.player.hit()
                    print(f"hit! {self.player.health}")
                enemy.rotate(self.player.position())
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
        self.map.addObject(newObject)

    def addNonCollidingObject(self, newObject: MapObject):
        self.displayHandler.addObject(newObject)

    def addPlayer(self):
        self.displayHandler.addObject(self.player)
        self.map.assignPlayer(self.player.collisionRectangle)

    def updateMousePosition(self, position):
        self.mousePosition = position
        self.player.rotate(position)
