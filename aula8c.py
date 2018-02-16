# TOCAR MUSICA EM PYTHON

import pygame
pygame.init()
pygame.mixer.music.load('003.mp3')
pygame.mixer.music.play()
pygame.event.wait()
