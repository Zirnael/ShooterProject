WIDTH = 500
HEIGHT = WIDTH

VISION_RANGE = 10  # How many blocks in each direction can a player see
MAP_SIZE = 10  # How big the map is (in blocks)
# TODO Zastosowac Map_size

BLOCK_SIZE = WIDTH / VISION_RANGE  # How many pixels one block on a map has


class colors:
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
