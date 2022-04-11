import pygame

import src.Constants as const
from src.engine.GameEngine import GameEngine


def main():
    pygame.init()
    clock = pygame.time.Clock()
    gameEngine = GameEngine()
    run = True

    while run:
        dt = clock.tick(const.FRAMERATE)
        """How much time passed since last frame (in mili seconds)"""

        # print(round(1000/dt))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_q or key == pygame.K_ESCAPE:
                    run = False
                gameEngine.keyPress(key)
            if event.type == pygame.KEYUP:
                key = event.key
                gameEngine.keyRelese(key)
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                gameEngine.updateMousePosition(position)

        gameEngine.progress(dt)


if __name__ == '__main__':
    main()
