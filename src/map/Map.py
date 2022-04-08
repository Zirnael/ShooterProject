import pygame
from typing import List
import src.Constants as const

mSize = const.MAP_SIZE

class Map:
    def __init__(self):
        self.objects : List[pygame.Rect] = []


    def addObject(self, newObject: pygame.Rect):
        self.objects.append(newObject)

    def removeObject(self, objectToRemove: pygame.Rect):
        self.objects.remove(objectToRemove)

    def isLegalPosition(self, destination: pygame.Rect) -> bool:
        return destination.collidelist(self.objects) == -1
