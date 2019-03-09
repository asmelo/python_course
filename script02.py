from pygame import mixer
mixer.init()
mixer.music.load('audio.mp3')
mixer.music.play()
input('Agora você escuta?')
'''
import pygame
pygame.init()
pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''