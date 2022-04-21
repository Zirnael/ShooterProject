import pygame
from typing import List, Optional

from src.map.MapObject import MapObject


class CollisionMap:
    def __init__(self):
        self.buildings: List[pygame.Rect] = []
        self.enemies: List[pygame.Rect] = []
        self.playerRect: Optional[pygame.Rect] = None

    def addEnemy(self, newObject: MapObject):
        self.enemies.append(newObject.collisionRectangle)

    def removeEnemy(self, objectToRemove: MapObject):
        self.enemies.remove(objectToRemove.collisionRectangle)

    def isLegalPosition(self, destination: pygame.Rect, callerEnemy: pygame.Rect = None) -> bool:
        copy = self.enemies.copy()
        try:
            copy.remove(callerEnemy)
        except ValueError:
            pass
        if destination.collidelist(copy) != -1:
            return False
        if destination.collidelist(self.buildings) != -1:
            return False

        return True

    def doesOverlapPlayer(self, rect: pygame.Rect) -> bool:
        if self.playerRect is None:
            return False
        return self.playerRect.colliderect(rect)

    def assignPlayer(self, pRect: pygame.Rect):
        self.playerRect: pygame.Rect = pRect



