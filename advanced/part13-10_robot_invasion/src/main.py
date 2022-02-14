# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")
random_turn = [random.choice([-1,1]) for i in range(10)]
x = [random.randint(0,640-robot.get_width()) for i in range(10)]
y = [random.randint(-3 * robot.get_height(),0) for i in range(10)]
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x[0],y[0]))
    window.blit(robot, (x[1],y[1]))
    window.blit(robot, (x[2],y[2]))
    window.blit(robot, (x[3],y[3]))
    window.blit(robot, (x[4],y[4]))
    window.blit(robot, (x[5],y[5]))
    window.blit(robot, (x[5],y[5]))
    window.blit(robot, (x[6],y[7]))
    window.blit(robot, (x[8],y[8]))
    window.blit(robot, (x[9],y[9]))
    pygame.display.flip()
    
    for i in range(10):
        y[i] += velocity
        if y[i] + robot.get_height() >= 480:
            y[i] = 480 - robot.get_height()
            x[i] += random_turn[i]

    clock.tick(60)