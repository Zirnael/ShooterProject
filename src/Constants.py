BOTTOM_BAR_HEIGHT = 60

WIDTH = 800
HEIGHT = WIDTH
SCREEN_HEIGHT = HEIGHT + BOTTOM_BAR_HEIGHT

MAP_SIZE = 10
"""The visible area is VISION_RANGE * VISION_RANGE square (in blocks"""

BLOCK_SIZE = WIDTH / MAP_SIZE
"""Building occupy a BLOCK_SIZE * BLOCKSIZE square"""

FRAMERATE = 60
"""Self explanatory"""

AFTER_HIT_DELAY = 1000
"""How much time the enemy doesnt move after attacking the player"""

ENEMY_SPEED = BLOCK_SIZE / 300
"""distance in 1 ms"""

PLAYER_SPEED = BLOCK_SIZE / 250
"""distance in 1 ms"""

ENEMY_COLLISION_SIZE = BLOCK_SIZE / 4
"""Size of CollisionRectangle of Enemies"""

DRUGSTORE_COOLDOWN = 5000
"""For how long the drugstore becomes inactive after use"""

DRUGSTORE_RESTORED_HEALTH = 5
"""How much health the drugstore restores"""


class colors:
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
