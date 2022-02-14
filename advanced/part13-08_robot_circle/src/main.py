# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")

angle = 0
clock = pygame.time.Clock()
def coordinates(angle, incre):
    x = 320+math.cos(angle+incre*math.radians(40))*150-robot.get_width()/2
    y = 240+math.sin(angle+incre*math.radians(40))*150-robot.get_height()/2
    return (x,y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    window.fill((0, 0, 0))
    window.blit(robot, coordinates(angle,0))
    window.blit(robot, coordinates(angle,1))
    window.blit(robot, coordinates(angle,2))
    window.blit(robot, coordinates(angle,3))
    window.blit(robot, coordinates(angle,4))
    window.blit(robot, coordinates(angle,5))
    window.blit(robot, coordinates(angle,6))
    window.blit(robot, coordinates(angle,7))
    window.blit(robot, coordinates(angle,8))
    window.blit(robot, coordinates(angle,9))

    pygame.display.flip()

    angle += 0.01
    clock.tick(60)