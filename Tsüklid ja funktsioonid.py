import pygame

pygame.init()

# Akna loomine
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("My Screen")

# Värvid
valge = (255, 255, 255)
must = (0, 0, 0)

# Funktsioon ruudustiku joonistamiseks
def draw_grid(square_size, rows, cols, line_color):
    for row in range(rows):
        for col in range(cols):
            # Arvutame ruudu koordinaadid
            x = col * square_size
            y = row * square_size
            # Joonistame ruudu
            pygame.draw.rect(screen, line_color, (x, y, square_size, square_size), 1)

# Tsükkel
running = True
while running:
    screen.fill(valge)  # Täidame ekraani taustavärviga

    # Joonistame ruudud (ruudu suurus, ridade arv, veergude arv, joone värv)
    draw_grid(20, screen.get_height() // 20, screen.get_width() // 20, must)

    # Kontrollime, kas akent suletakse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()


pygame.quit()
