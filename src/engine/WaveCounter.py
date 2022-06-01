import random

import pygame

import other.Constants as const
from Enemies.BaseEnemy import BaseEnemy
from Enemies.BossEnemy import BossEnemy
from Enemies.SplitEnemy import SplitEnemy


def randomPosition(displayRectangleSize):
    direction = random.randint(0, 2)
    place = random.randint(0, const.MAP_SIZE - 1) * const.BLOCK_SIZE
    if direction == 0:
        return -const.BLOCK_SIZE, place
    if direction == 1:
        return place, -const.BLOCK_SIZE

    return const.WIDTH + const.BLOCK_SIZE - displayRectangleSize, place


class WaveCounter:
    def __init__(self, bottomBar, player, hq, addEnemyFunction):
        self.bottomBar = bottomBar
        self.wave = 1
        self.score = 0
        self.waveStart = 10_000
        self.targets = [player, hq]
        self.add = addEnemyFunction

    def generateWave(self):
        baseNO, splitNO, bossNO = const.waves[self.wave]
        for _ in range(baseNO):
            newEnemy = BaseEnemy(randomPosition(const.BLOCK_SIZE), "enemy.png", random.choice(self.targets))
            self.add(newEnemy)
        for _ in range(splitNO):
            newEnemy = SplitEnemy(randomPosition(2 * const.BLOCK_SIZE), "split.png", random.choice(self.targets),
                                  self.add)
            self.add(newEnemy)
        for _ in range(bossNO):
            newEnemy = BossEnemy(randomPosition(2 * const.BLOCK_SIZE), "boss.png", random.choice(self.targets))
            self.add(newEnemy)

        self.waveStart = pygame.time.get_ticks()
        self.score += self.wave
        self.wave += 1
        self.wave = min(self.wave, 20)

    def updateMessage(self):
        currentTime = pygame.time.get_ticks()
        timeLeft = (self.waveStart + const.WAVE_DURATION - currentTime) / 1000
        self.bottomBar.nextWaveMessage = f"Next wave in: {timeLeft}"
        self.bottomBar.scoreMessage = f"Score: {self.score}"
        self.bottomBar.waveCountMessage = f"Wave: {self.wave}"

    def update(self):
        """
        See if next wave needs to start, update information about next wave.
        :return:
        """
        currentTime = pygame.time.get_ticks()
        if currentTime - self.waveStart > const.WAVE_DURATION:
            self.generateWave()

        self.updateMessage()
