BOTTOM_BAR_HEIGHT = 60

WIDTH = 500
HEIGHT = WIDTH
SCREEN_HEIGHT = HEIGHT + BOTTOM_BAR_HEIGHT

VISION_RANGE = 10
"""The visible area is VISION_RANGE * VISION_RANGE square (in blocks"""

MAP_SIZE = 10  # How big the map is (in blocks)
"""TODO"""
# TODO Zastosowac Map_size

BLOCK_SIZE = WIDTH / VISION_RANGE
"""Building occupy a BLOCK_SIZE * BLOCKSIZE square"""

FRAMERATE = 60
"""Self explanatory"""




class colors:
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
