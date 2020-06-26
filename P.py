import random
import sys
from sys import platform
import pygame
from pygame.locals import *


FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode(SCREENWIDTH,SCREENHEIGHT)
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'ABOUT/GALLERY/download(8).jpg'
BACKGROUND = 'ABOUT/GALLERY/background.jpg'
PIPE = 'ABOUT/GALLERY/pipe.jpg'

if __name__ == "__main__":
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Flappy bird by Totalmad_3.0")
    GAME_SPRITES['numbers'] = (
        pygame.image.load('ABOUT/GALLERY/download(7).jpg').convert_alpha(),
        pygame.image.load('ABOUT/GALLERY/1.jpg').convert_alpha(),
        pygame.image.load('ABOUT/GALLERY/download.jpg').convert_alpha(),
        pygame.image.load('ABOUT/GALLERY/download(1).jpg').convert_alpha(),
        pygame.image.load('ABOUT/GALLERY/download(2).jpg').convert_alpha(),
        pygame.image.load('ABOUT/GALLERY/download(3).jpg').convert_alpha(),
        pygame.image.load('ABOUT/GALLERY/images.jpg').convert_alpha(),
        pygame.image.load('ABOUT/GALLERY/download(4).jpg').convert_alpha(),
        pygame.image.load('ABOUT/GALLERY/download(5).jpg').convert_alpha(),
        pygame.image.load('ABOUT/GALLERY/download(6).jpg').convert_alpha()
    )
    GAME_SPRITES['startup'] = pygame.image.load('ABOUT/GALLERY/background.jpg').convert_alpha()
    GAME_SPRITES['pipe'] = (
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180) ,
        pygame.image.load(PIPE).convert_alpha()
    )

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    # sounds
    GAME_SOUNDS['DIE'] = pygame.mixer.sound('/ABOT/sound/die.wav')
    GAME_SOUNDS['TRACK'] = pygame.mixer.sound('ABOUT/sound/TRACK.mp3')

    # while True:
    #     welcomeScreen()
    #     mainGame()