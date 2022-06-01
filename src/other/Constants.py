WIDTH = 800

HEIGHT = WIDTH

MAP_SIZE = 20
"""The visible area is VISION_RANGE * VISION_RANGE square (in blocks)"""

BLOCK_SIZE = WIDTH / MAP_SIZE
"""Building occupy a BLOCK_SIZE * BLOCKSIZE square"""

BOTTOM_BAR_HEIGHT = 100 + BLOCK_SIZE

SCREEN_HEIGHT = HEIGHT + BOTTOM_BAR_HEIGHT

WAVE_DURATION = 25_000

ICON_SIZE = 40
"""How big are icons on bottom bar"""

FRAMERATE = 60
"""Self explanatory"""

ENEMY_BASE_HITDELAY = 1000
"""How much time the enemy doesnt move after attacking"""

ENEMY_BASE_SPEED = BLOCK_SIZE * 5 / 1000
"""distance in 1 ms"""

BUILDING_DISAPPEAR_TIME = 5000
"""Time after which destroyed building diappears"""

ENEMY_BASE_COLLISION_SIZE = BLOCK_SIZE / 4

ENEMY_BASE_HITPOINTS = 10

ENEMY_BOSS_HEALTH = 1000

ENEMY_BOSS_SPEED = BLOCK_SIZE / 1100 / 1000

ENEMY_BOSS_DAMAGE = 30

ENEMY_BOSS_HITDELAY = 500

ENEMY_SPLIT_COOLDOWN = 3_000

ENEMY_SPLIT_DURATION = 5_000

ENEMY_SPLIT_HEALTH = 200

ENEMY_SPLIT_DAMAGE = 5

ENEMY_SPLIT_SPEED = BLOCK_SIZE / 1000

ENEMY_SPLIT_HITDELAY = 3000

PLAYER_HEALTH = 10

PLAYER_SPEED = BLOCK_SIZE * 3 / 1000
"""distance in 1 ms"""

PLAYER_DAMAGE = 10

BULLET_SPEED = 100
"""not distance in 1 ms"""

"""Size of CollisionRectangle of Enemies"""

DRUGSTORE_COOLDOWN = 5000
"""For how long the drugstore becomes inactive after use"""

DRUGSTORE_RESTORED_HEALTH = 5
"""How much health the drugstore restores"""

DRUGSTORE_HEALTH = 10
"""How much health the drugstore has"""

DRUGSTORE_COST = 10

TURRET_COOLDOWN = 1000
"""How long does the turret wait between shots"""

TURRET_HEALTH = 5

TURRET_COST = 50

BULLET_LENGTH = 20
"""How long is the tail of the bullet"""

GOLDMINE_GOLD = 3
"""How much gold the goldmine gives"""

GOLDMINE_COOLDOWN = 5_000
"""For how long the goldmine becomes inactive after use"""

GOLDMINE_COST = 15

GOLDMINE_HEALTH = 3

SHOP_COOLDOWN = 35_000
"""For how long the shop becomes inactive after use (in ms)"""

SHOP_HEALTH = 10

SHOP_COST = 30

SHOP_EFFECT_COST = 5

SHOP_EFFECT_DURATION = 2_000
"""How much time the boost lasts (in ms)"""

SHOT_COOLDOWN = 800
"""How much time needs to pass before player can shoot again"""

BOOST_SHOT_COOLDOWN = 200
"""How much time need to pass between auto shots during boost (see shop)"""

HQ_HEALTH = 50

WALL_HEALTH = 20

WALL_COST = 5


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


waves = {1: (1, 0, 0),
         2: (5, 0, 0),
         3: (8, 0, 0),
         4: (0, 1, 0),
         5: (0, 2, 0),
         6: (5, 1, 0),
         7: (5, 2, 0),
         8: (5, 3, 0),
         9: (10, 3, 0),
         10: (0, 0, 1),
         11: (10, 3, 0),
         12: (5, 1, 1),
         13: (0, 2, 1),
         14: (0, 3, 1),
         15: (0, 0, 2),
         16: (0, 3, 2),
         17: (0, 10, 0),
         18: (0, 0, 3),
         19: (0, 0, 4),
         20: (0, 0, 5)}
