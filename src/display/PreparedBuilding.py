from os import path

import pygame.image

from other import Constants as const
from DisplayObject import DisplayObject


class PreparedBuilding(DisplayObject):
    def __init__(self, position, texture=None, building=None):
        super().__init__(position, const.BLOCK_SIZE)
        self.isLegal = False
        if texture is not None and building is not None:
            self.img = pygame.image.load(path.join("images", texture)).convert_alpha()
            self.img = pygame.transform.scale(self.img, (const.BLOCK_SIZE, const.BLOCK_SIZE))
            self.type = building
            self.img.set_alpha(200)
            self.img.set_colorkey(const.colors.WHITE)
            self.texture = texture
        else:
            self.img = None
            self.type = None
            self.texture = None

    def changeBuilding(self, newTexture=None, building=None):
        self.type = building
        if newTexture is not None:
            self.texture = newTexture
            self.img = pygame.image.load(path.join("images", newTexture)).convert_alpha()
            self.img = pygame.transform.scale(self.img, (const.BLOCK_SIZE, const.BLOCK_SIZE))
            self.img.set_colorkey(const.colors.WHITE)
            self.img.set_alpha(200)
            return
        self.img = None
        self.texture = None

    def move(self, newPosition):
        self.displayRectangle.topleft = newPosition

    def print(self) -> pygame.Surface:
        if self.img is not None and self.isLegal:
            return self.img
        return pygame.Surface((0, 0))
