import pygame

pygame.init()

screen = pygame.display.set_mode([640, 480], pygame.RESIZABLE)
pygame.display.set_caption("My Screen")
screen.fill([1, 11,55])               

#joonistamine
"""
#joon
pygame.draw.line(screen, [255,0,0], [100,100], [200,200], 2)

#ristkülik
pygame.draw.rect(screen, [0, 225, 0], [50, 80, 200, 300], 2)

#ring
pygame.draw.circle(screen, [0, 0, 255], [150,200], 100, 1)

#hulknurk
pygame.draw.polygon(screen, [255, 0, 255], [[50,50],[100,50],[100,150],[250,50],[350,250],[50,250]], 2)

#ovaal
pygame.draw.ellipse(screen, [0, 225, 0], [50, 80, 200, 300], 2)

"""
#kaar
pygame.draw.arc(screen,[255,0,0], [100,100,250,200], 0, 3.14*1.5, 1)

pygame.display.flip()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Kui kasutaja vajutab "X", sulgub aken
            running = False

pygame.quit()
