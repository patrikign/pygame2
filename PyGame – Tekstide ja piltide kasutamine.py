"""
import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill([205, 205, 205])

#lisame teksti
#font = pygame.font.Font(pygame.font.match_font('arial'), 50)
font = pygame.font.Font(pygame.font.match_font('arial'), 50)
font.set_underline(True)
text = font.render("Hello PyGame", True, [0,0,0])

#tekstikasti suurus
text_width = text.get_rect().width
text_height = text.get_rect().height

screen.blit(text, [32,24])

pygame.display.flip()
"""

import pygame

pygame.init()

# Ekraani seaded
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Harjutamine")
screen.fill([204, 255, 204])

# Lisame pildid
bg = pygame.image.load("20252.jpg")

# Muudame pildi suurust
bg_resized = pygame.transform.scale(bg, (640, 480))

# Paigutame tausta ekraanile
screen.blit(bg_resized, [0, 0])

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Kui kasutaja vajutab "X", sulgub aken
            running = False

pygame.quit()

