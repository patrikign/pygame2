import pygame
import sys

pygame.init()
WIDTH, HEIGHT, square_size = 640, 480, 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ruudustik")
lGreen, line_color = [153, 255, 153], (255, 0, 0)

running = True
while running:
    screen.fill(lGreen)
    for x in range(0, WIDTH, square_size):
        for y in range(0, HEIGHT, square_size):
            pygame.draw.rect(screen, line_color, (x, y, square_size, square_size), 1)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
