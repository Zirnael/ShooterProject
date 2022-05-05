from typing import List

import pygame

import src.Constants as const
from Bullet import Bullet
from DisplayObject import DisplayObject
from Goldmine import Goldmine
from Headquarters import Headquarters
from PreparedBuilding import PreparedBuilding
from Shop import Shop
from Turret import Turret
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
        self.player = Player((0, 0), "player.png")
        self.map = CollisionMap(self.player)
        self.buildingsTypes = [("wall.jpg", Wall, 5),
                               ("goldmine.png", Goldmine, 15),
                               ("drugstore.png", Drugstore, 30),
                               ("shop.png", Shop, 20),
                               ("turret.png", Turret, 50)]

        self.preparedBuilding = PreparedBuilding((0, 0), self.buildingsTypes[1][0], self.buildingsTypes[1][1])

        self.addDisplayObject(self.preparedBuilding)

        self.enemies: List[Enemy] = []
        for i in range(5):
            newEnemy = Enemy((i * const.BLOCK_SIZE, 2 * const.BLOCK_SIZE), "enemy.png")
            self.addEnemy(newEnemy)

        self.buildings: List[Building] = []

        self.HQ = Headquarters((5 * const.BLOCK_SIZE, 5 * const.BLOCK_SIZE), "placeholder.png")
        self.addBuilding(self.HQ)
        # self.addBuilding(Drugstore("drugstore.png", (2 * const.BLOCK_SIZE, 3 * const.BLOCK_SIZE)))
        # self.addBuilding(Wall("wall.jpg", (3 * const.BLOCK_SIZE, 3 * const.BLOCK_SIZE)))
        # self.addBuilding(Turret("turret.png", (4 * const.BLOCK_SIZE, 3 * const.BLOCK_SIZE)))
        # self.addBuilding(Goldmine("goldmine.png", (5 * const.BLOCK_SIZE, 2 * const.BLOCK_SIZE)))

        self.addPlayer()

        self.bullets: List[Bullet] = []

        self.mousePosition = (0, 0)
        self.bottom_bar = BottomBar((0, const.HEIGHT), self.player, self.buildingsTypes)
        self.displayHandler.addObject(self.bottom_bar)

    def progress(self, dt: int):
        """

        :param dt: How much time passed since the last frame
        :return:
        """
        if any(self.moveVector):  # move only if some key is pressed
            self.player.move(self.moveVector, dt, self.map)

        self.player.rotate(self.mousePosition)

        self.enemies[:] = [enemy for enemy in self.enemies if enemy.alive]
        self.bullets[:] = [bullet for bullet in self.bullets if bullet.alive]
        self.buildings[:] = [building for building in self.buildings if building.alive]

        for enemy in self.enemies:
            hitObject = enemy.simpleMove(dt, self.player.position(), self.map)
            if hitObject is not None:
                hitObject.hit(enemy.damage)
            enemy.rotate(self.player.position())

        for building in self.buildings:
            newBullets = building.update(self.map, self.player)
            if newBullets is not None:
                for bullet in newBullets:
                    self.addBullet(bullet)
            if not building.alive:
                self.map.removeBuilding(building)

        for bullet in self.bullets:
            bullet.move(dt, self.map)

        self.preparedBuilding.isLegal = self.map.isLegalPosition(self.preparedBuilding.displayRectangle,
                                                                 considerPlayer=True)
        self.displayHandler.print([self.player.collisionRectangle.topleft, self.player.collisionRectangle.topright,
                                   self.player.collisionRectangle.bottomleft,
                                   self.player.collisionRectangle.bottomright])

    def keyPress(self, key):
        """
        Change MoveVector based on input
        :param key:
        :return:
        """
        texture, building, price = None, None, None
        changePreparedBuliding = False
        if key == pygame.K_LEFT:
            self.moveVector[0] -= 1
        elif key == pygame.K_RIGHT:
            self.moveVector[0] += 1
        elif key == pygame.K_DOWN:
            self.moveVector[1] += 1
        elif key == pygame.K_UP:
            self.moveVector[1] -= 1
        elif key == pygame.K_1:
            changePreparedBuliding = True
            texture, building, price = self.buildingsTypes[0]
        elif key == pygame.K_2:
            changePreparedBuliding = True
            texture, building, price = self.buildingsTypes[1]
        elif key == pygame.K_3:
            changePreparedBuliding = True
            texture, building, price = self.buildingsTypes[2]
        elif key == pygame.K_4:
            changePreparedBuliding = True
            texture, building, price = self.buildingsTypes[3]
        elif key == pygame.K_5:
            changePreparedBuliding = True
            texture, building, price = self.buildingsTypes[4]

        if changePreparedBuliding and price <= self.player.gold:
            self.preparedBuilding.changeBuilding(texture, building)

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

    def addDisplayObject(self, newObject: DisplayObject):
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

    def addBullet(self, newBullet):
        self.displayHandler.addBullet(newBullet)
        self.bullets.append(newBullet)

    def updateMousePosition(self, position):
        x, y = position
        x = x // const.BLOCK_SIZE * const.BLOCK_SIZE
        y = y // const.BLOCK_SIZE * const.BLOCK_SIZE
        self.preparedBuilding.move((x, y))
        self.mousePosition = position
        self.player.rotate(position)

    def mouseClick(self, position, key):
        x, y = position
        x = x // const.BLOCK_SIZE * const.BLOCK_SIZE
        y = y // const.BLOCK_SIZE * const.BLOCK_SIZE
        if key == const.mouseButtons.RIGHT:
            self.preparedBuilding.changeBuilding(None, None)
        elif key == const.mouseButtons.LEFT:
            if self.preparedBuilding.texture is not None:
                if self.map.isLegalPosition(pygame.Rect((x, y), (const.BLOCK_SIZE, const.BLOCK_SIZE)),
                                            considerPlayer=True):
                    self.addBuilding(self.preparedBuilding.type(self.preparedBuilding.texture, (x, y)))
            else:
                newBullets = self.player.shoot(position)
                for newBullet in newBullets:
                    self.addBullet(newBullet)
