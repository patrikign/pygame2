import pygame

pygame.init()
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("My Screen")

roheline = (153, 255, 153)
punane = (255, 0, 0)


def draw_grid(square_size, rows, cols, line_color):
    for row in range(rows):
        for col in range(cols):
            x = col * square_size
            y = row * square_size
            pygame.draw.rect(screen, line_color, (x, y, square_size, square_size), 1)


running = True
while running:
    screen.fill(roheline)
    draw_grid(20, screen.get_height() // 20, screen.get_width() // 20, punane)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
