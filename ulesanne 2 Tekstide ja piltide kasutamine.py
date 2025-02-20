import pygame

# Initsialiseeri Pygame
pygame.init()

# Mänguakna seaded
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ülesanne 2")

# Laadi pildid
bg = pygame.image.load("bgshop.jpg")
seller = pygame.image.load("seller.png")
chat = pygame.image.load("chat.png")

# Muuda piltide suurust
seller = pygame.transform.scale(seller, (248, 294))
chat = pygame.transform.scale(chat, (230, 183))

# Fondi seaded
font = pygame.font.Font(None, 33)
text = font.render("Pätrik Ignatenko", True, (255, 255, 255))

# Mängutsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Joonista ekraanile
    screen.blit(bg, (0, 0))  # Taust
    screen.blit(seller, (90, 150))
    screen.blit(chat, (216, 75))
    screen.blit(text, (236, 140))

    pygame.display.flip()

pygame.quit()