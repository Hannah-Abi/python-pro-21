# # WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame
from pygame.constants import WINDOWHITTEST

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("ball.png")

x = 400
y = 0
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    if velocity > 0 and x+robot.get_width() <= 640:
        x += velocity
        y += velocity
        if x+robot.get_width() >= 640:
            velocity = -velocity
    if velocity < 0 and y + robot.get_width() <= 480:
        x += velocity
        y -= velocity
        if y + robot.get_height() >= 480:
            velocity = - velocity

            


    clock.tick(150)