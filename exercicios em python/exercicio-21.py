import pygame

pygame.init()
pygame.mixer.init()  # <-- ESSENCIAL

pygame.mixer.music.load('ex21.mp3.mp3')
pygame.mixer.music.play()

# Espera enquanto a música toca
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
