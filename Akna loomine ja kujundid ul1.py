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
sinine = (0, 56, 168)  # Sinine (Eesti lipu värv)
must = (0, 0, 0)  # Must (Eesti lipu värv)
valge = (255, 255, 255)  # Valge (Eesti lipu värv)

# Funktsioon valgusfoori joonistamiseks
def draw_traffic_light():
    # Joonista punane, kollane ja roheline ring
    pygame.draw.circle(screen, punane, [150, 100], 20)   # Punane
    pygame.draw.circle(screen, kollane, [150, 150], 20)  # Kollane
    pygame.draw.circle(screen, roheline, [150, 200], 20) # Roheline

# Funktsioon postialuse joonistamiseks
def draw_base():
    # Joonista postialus Eesti lipu värvides
    pygame.draw.polygon(screen, sinine, [(125, 275), (175, 275), (200, 300), (100, 300)])  # Sinine osa
    pygame.draw.polygon(screen, must, [(125, 275), (175, 275), (200, 250), (100, 250)])   # Must osa
    pygame.draw.polygon(screen, valge, [(125, 250), (175, 250), (200, 225), (100, 225)])  # Valge osa

    # post (ristkülik)
    pygame.draw.rect(screen, must, [145, 230, 10, 50])  

# Tsükkel
running = True
while running:
    screen.fill(valge)  

    #  postialus
    draw_base()

    #  valgusfoor
    draw_traffic_light()

    #  tekst
    font = pygame.font.SysFont("Arial", 15)  
    text = font.render("Valgusfoor – Pätrik Ignatenko", True, must)
    screen.blit(text, [50, 10])

    #  must ristkülik valgusfoori ümber
    pygame.draw.rect(screen, must, [110, 50, 80, 180], 2)

    # Kontrollime kas akent suletakse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
