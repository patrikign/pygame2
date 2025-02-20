import pygame

pygame.init()

# Akna loomine
screen = pygame.display.set_mode([300, 300])
pygame.display.set_caption("valgusfoor – Pätrik Ignatenko")

# Värvid
punane = (255, 0, 0)
kollane = (255, 255, 0)
roheline = (0, 255, 0)
must = (0, 0, 0)
valge = (255, 255, 255)
heledam_taust = (200, 200, 200)  

# Funktsioon valgusfoori joonistamiseks
def draw_traffic_light():
    # Joonista punane, kollane ja roheline ring
    pygame.draw.circle(screen, punane, [150, 100], 20)   # Punane
    pygame.draw.circle(screen, kollane, [150, 150], 20)  # Kollane
    pygame.draw.circle(screen, roheline, [150, 200], 20) # Roheline

# Tsükkel
running = True
while running:
    screen.fill(valge) 

    # Joonistame valgusfoori
    draw_traffic_light()

    # Lisa tekst
    font = pygame.font.SysFont("Arial", 15)  # Väiksem tekst
    text = font.render("Valgusfoor – Pätrik Ignatenko", True, must)
    screen.blit(text, [50, 10])

    # Joonista must ristkülik valgusfoori ümber
    pygame.draw.rect(screen, must, [110, 50, 80, 200], 2)

    # Kontrollime, kas akent suletakse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
