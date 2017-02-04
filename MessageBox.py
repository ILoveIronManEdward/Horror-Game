import pygame

def MakeMessageBox(name, screenX, screenY, display):
    font = pygame.font.SysFont("Ariel", 50)
    label = font.render("Picked up " + name, 1, (255, 255, 255))
    pygame.draw.rect(display, (0, 0, 0), (0, screenY - 200, screenX, screenY))
    display.blit(label, (50, screenY - 190))
    pygame.display.update()

def GameOver():
    pass
