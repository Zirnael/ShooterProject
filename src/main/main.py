import pygame
from src.engine.GameEngine import GameEngine

def main():
    pygame.init()
    gameEngine = GameEngine()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_q or key == pygame.K_ESCAPE:
                    run = False
                if key == pygame.K_a:
                    gameEngine.progress()

        i = 3
        i += 1

if __name__ == '__main__':
    main()
