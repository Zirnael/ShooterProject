BOTTOM_BAR_HEIGHT = 100

WIDTH = 800
HEIGHT = WIDTH
SCREEN_HEIGHT = HEIGHT + BOTTOM_BAR_HEIGHT

MAP_SIZE = 20
"""The visible area is VISION_RANGE * VISION_RANGE square (in blocks)"""

BLOCK_SIZE = WIDTH / MAP_SIZE
"""Building occupy a BLOCK_SIZE * BLOCKSIZE square"""

ICON_SIZE = 40
"""How big are icons on bottom bar"""

FRAMERATE = 60
"""Self explanatory"""

AFTER_HIT_DELAY = 1000
"""How much time the enemy doesnt move after attacking the player"""

ENEMY_SPEED = BLOCK_SIZE / 200
"""distance in 1 ms"""

PLAYER_SPEED = BLOCK_SIZE / 300
"""distance in 1 ms"""

BULLET_SPEED = 100
"""not distance in 1 ms"""

ENEMY_COLLISION_SIZE = BLOCK_SIZE / 4
"""Size of CollisionRectangle of Enemies"""

DRUGSTORE_COOLDOWN = 5000
"""For how long the drugstore becomes inactive after use"""

DRUGSTORE_RESTORED_HEALTH = 5
"""How much health the drugstore restores"""

DRUGSTORE_HEALTH = 10
"""How much health the drugstore has"""

TURRET_COOLDOWN = 1000
"""How long does the turret wait between shots"""

TURRET_HEALTH = 5

BULLET_LENGTH = 20
"""How long is the tail of the bullet"""

GOLDMINE_GOLD = 2
"""How much gold the goldmine gives"""

GOLDMINE_COOLDOWN = 5000
"""For how long the goldmine becomes inactive after use"""

GOLDMINE_HEALTH = 7

SHOP_COOLDOWN = 5000
"""For how long the shop becomes inactive after use"""

SHOP_HEALTH = 10

SHOT_COOLDOWN = 1000
"""How much time needs to pass before player can shoot again"""

HQ_HEALTH = 50

WALL_HEALTH = 15


class colors:
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)


class mouseButtons:
    LEFT = 1
    RIGHT = 3
    WHEEL_UP = 4
    WHEEL_DOWN = 5
