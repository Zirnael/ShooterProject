import pygame
from typing import List, Optional

from src.map.MapObject import MapObject


class CollisionMap:
    def __init__(self):
        self.objects: List[pygame.Rect] = []
        self.playerRect: Optional[pygame.Rect] = None

    def addObject(self, newObject: MapObject):
        self.objects.append(newObject.collisionRectangle)

    def removeObject(self, objectToRemove: MapObject):
        self.objects.remove(objectToRemove.collisionRectangle)

    def isLegalPosition(self, destination: pygame.Rect, caller: pygame.Rect = None) -> bool:
        copy = self.objects.copy()
        try:
            copy.remove(caller)
        except ValueError:
            pass
        return destination.collidelist(copy) == -1

    def doesOverlapPlayer(self, rect: pygame.Rect) -> bool:
        if self.playerRect is None:
            return False
        return self.playerRect.colliderect(rect)

    def assignPlayer(self, pRect: pygame.Rect):
        self.playerRect: pygame.Rect = pRect
