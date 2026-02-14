'''Add Elements to My Screen

Write a Python program to create a game screen and add
elements like - rectangle and text using the Pygame library

Window Size(640,480)
Set Caption - My First Game Screen
Create a rectangle of the colour of your choice, positioned at the centre of the screen
Display a text on the screen
the Backgroung colour of the Screen - White(0,0,0)


import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480
SCREEN_COLOR = (255, 255, 255) 
RECT_COLOR = (0, 128, 0)
TEXT_COLOR = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game Screen")

font = pygame.font.Font(None, 32)
text_surface = font.render("Hello, Pygame!", True, TEXT_COLOR)
text_rect = text_surface.get_rect()
text_rect.center = (WIDTH // 2, HEIGHT // 4)

rect_width, rect_height = 100, 100

rect_surface = pygame.Rect(0, 0, rect_width, rect_height)
rect_surface.center = (WIDTH // 2, HEIGHT // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SCREEN_COLOR)
    pygame.draw.rect(screen, RECT_COLOR, rect_surface)
    screen.blit(text_surface, text_rect)
    pygame.display.flip() 

pygame.quit()
sys.exit()'''

