from typing import List

import pygame

import other.Constants as const
from Building import Building
from Bullet import Bullet
from DisplayObject import DisplayObject
from Enemies.Enemy import Enemy
from Goldmine import Goldmine
from Headquarters import Headquarters
from PreparedBuilding import PreparedBuilding
from Shop import Shop
from Turret import Turret
from src.display.BottomBar import BottomBar
from src.display.DisplayHandler import DisplayHandler
from src.engine.WaveCounter import WaveCounter
from src.map.CollisionMap import CollisionMap
from src.map.mapObjects.Buildings.Drugstore import Drugstore
from src.map.mapObjects.Buildings.Wall import Wall
from src.map.mapObjects.Player import Player


class GameEngine:

    def __init__(self):
        self.displayHandler = DisplayHandler()
        self.gameActive = True
        self.moveVector: List[int, int] = [0, 0]

        self.player = Player((5 * const.BLOCK_SIZE, 5 * const.BLOCK_SIZE), "player.png")
        self.map = CollisionMap(self.player)
        self.buildingsTypes = [("wall.jpg", Wall, const.WALL_COST),
                               ("goldmine.png", Goldmine, const.GOLDMINE_COST),
                               ("drugstore.png", Drugstore, const.DRUGSTORE_COST),
                               ("shop.png", Shop, const.SHOP_COST),
                               ("turret.png", Turret, const.TURRET_COST)]

        self.preparedBuilding = PreparedBuilding((0, 0))

        self.addDisplayObject(self.preparedBuilding)

        self.enemies: List[Enemy] = []

        self.buildings: List[Building] = []

        self.HQ = Headquarters((9 * const.BLOCK_SIZE, 8 * const.BLOCK_SIZE), "hq.png")
        # self.HQ = Headquarters((5 * const.BLOCK_SIZE, 5 * const.BLOCK_SIZE), "hq.png")
        self.addBuilding(self.HQ)

        self.addPlayer()

        self.bullets: List[Bullet] = []

        self.mousePosition = (0, 0)
        self.bottom_bar = BottomBar((0, const.HEIGHT), self.player, self.buildingsTypes)

        self.displayHandler.addObject(self.bottom_bar)

        self.waveCounter = WaveCounter(self.bottom_bar, self.player, self.HQ, self.addEnemy)

    def progress(self, dt: int):
        """

        :param dt: How much time passed since the last frame
        :return:
        """
        if self.gameActive:
            if any(self.moveVector):  # move only if some key is pressed
                self.player.move(self.moveVector, dt, self.map)

            self.player.rotate(self.mousePosition)
            newBullets = self.player.autoShot(self.mousePosition)

            for bullet in newBullets:
                self.addBullet(bullet)

            self.enemies[:] = [enemy for enemy in self.enemies if enemy.alive]
            self.bullets[:] = [bullet for bullet in self.bullets if bullet.alive]
            self.buildings[:] = [building for building in self.buildings if building.alive or building.shouldDisplay]

            for enemy in self.enemies:
                hitObject = enemy.move(dt, self.map)
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

            self.waveCounter.update()

            self.preparedBuilding.isLegal = self.map.isLegalPosition(self.preparedBuilding.displayRectangle,
                                                                     considerPlayer=True)
            if not self.player.alive or not self.HQ.alive:
                self.gameOver()

        self.displayHandler.print()

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
                    newBuilding = self.preparedBuilding.type(self.preparedBuilding.texture, (x, y))
                    self.addBuilding(newBuilding)
                    self.player.gold -= newBuilding.cost
                    if self.player.gold < newBuilding.cost:
                        self.preparedBuilding.changeBuilding()
            else:
                newBullets = self.player.shoot(position)
                for newBullet in newBullets:
                    self.addBullet(newBullet)

    def gameOver(self):
        self.bottom_bar.waveCountMessage = "Game over"
        self.gameActive = False
