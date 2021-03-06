import pygame

import other.Constants as const
from src.engine.GameEngine import GameEngine


def main():
    pygame.init()
    pygame.font.init()
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
            elif event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_q or key == pygame.K_ESCAPE:
                    run = False
                elif key == pygame.K_f:
                    gameEngine.player.maxHealth = 100
                    gameEngine.player.currentHealth = 50
                    gameEngine.player.alive = True
                    gameEngine.player.gold = 200
                    gameEngine.gameActive = True
                    gameEngine.HQ.shouldDisplay = True
                    gameEngine.HQ.alive = True
                    gameEngine.HQ.currentHealth = gameEngine.HQ.maxHealth
                elif key == pygame.K_c:
                    gameEngine.waveCounter.generateWave()
                gameEngine.keyPress(key)
            elif event.type == pygame.KEYUP:
                key = event.key
                gameEngine.keyRelese(key)
            elif event.type == pygame.MOUSEMOTION:
                position = event.pos
                gameEngine.updateMousePosition(position)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = event.pos
                gameEngine.mouseClick(position, event.button)

        gameEngine.progress(dt)


if __name__ == '__main__':
    main()
