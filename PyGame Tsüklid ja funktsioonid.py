import pygame
import sys
import random

# Initsialiseeri Pygame
pygame.init()

# Värvid
lGreen = [153, 255, 153]
red = [255, 0, 0]

# Ekraani seaded
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Harjutamine")

# Funktsioon maja joonistamiseks
def drawHouse(x, y, width, height, screen, color):
    points = [
        (x, y - ((3/4) * height)),
        (x, y),
        (x + width, y),
        (x + width, y - ((3/4) * height)),
        (x, y - ((3/4) * height)),
        (x + width/2, y - height),
        (x + width, y - ((3/4) * height))
    ]
    pygame.draw.lines(screen, color, False, points, 2)

# Esmane ekraani puhastamine ja taustavärvi seadmine
screen.fill(lGreen)

# Joonistame 9 suvalist punast ruutu ekraanile
for i in range(1, 10):
    x = random.randint(0, 620)
    y = random.randint(0, 460)
    pygame.draw.rect(screen, red, [x, y, 20, 20])

# Joonistame maja
drawHouse(100, 400, 300, 200, screen, red)

# Uuendame ekraani
pygame.display.flip()

# Peamine tsükkel, mis hoiab akna avatuna kuni kasutaja selle sulgeb
gameover = False
while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

pygame.quit()
sys.exit()
