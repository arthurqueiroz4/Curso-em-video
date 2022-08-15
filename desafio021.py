import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('musc021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
input()
pygame.event.wait()