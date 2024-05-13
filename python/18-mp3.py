#Faça um programa que abra e execute um aúdio em mp3

import pygame
pygame.init()

file_path = 'Verbalase - No No No.mp3'
pygame.mixer.music.load(file_path)
pygame.mixer.music.play()

clock = pygame.time.Clock()

# Aguarde até que a música termine
while pygame.mixer.music.get_busy():
    clock.tick(30)  # Ajuste conforme necessário

pygame.quit()