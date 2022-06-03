import pygame
import random
from pygame.locals import *

black = (0,0,0)

class Game:
    def __init__(self):
        pygame.init()
        miniknight = pygame.image.load("resources/junkyard/sheets/miniknight.jpg")
        map1 = pygame.image.load("resources/maps/FE7C01.jpeg")

        self.baseplane = pygame.display.set_mode((240, 160))
        self.baseplane.fill((black))
        self.baseplane.blit(map1, (0,0))
        self.baseplane.blit(miniknight, (120, 80))



    def run(self):
        running = True
        while running:
            pygame.display.flip()
            for event in pygame.event.get():

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                elif event.type == pygame.QUIT:
                    running = False

if __name__ == "__main__":
    game = Game()
    game.run()



    # def run(self):
    #     running = True
    #     pause = False
    #     global gamespeed
    #
    #     while running:
    #         for event in pygame.event.get():
    #             print(gamespeed)
    #             if event.type == KEYDOWN:
    #                 if event.key == K_ESCAPE:
    #                     running = False
    #
    #                 if event.key == K_RETURN:
    #                     pause = False
    #                     gamespeed = 0.15
    #                     self.snake.length -= self.snake.length - 1
    #                     pygame.mixer.Sound.play(bgmusic, 999999999)
    #
    #                 if event.key == K_UP:
    #                     self.snake.move_up()
    #
    #                 if event.key == K_DOWN:
    #                     self.snake.move_down()
    #
    #                 if event.key == K_LEFT:
    #                     self.snake.move_left()
    #
    #                 if event.key == K_RIGHT:
    #                     self.snake.move_right()
    #
    #             elif event.type == QUIT:
    #                 running = False
    #
    #         try:
    #             if not pause:
    #                 self.play()
    #         except Exception as e:
    #             self.show_game_over()
    #             pause = True
    #             pygame.mixer.Sound.stop(bgmusic)
    #             pygame.mixer.Sound.play(gameoversong)
