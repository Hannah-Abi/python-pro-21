import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")
x = 0
y = 50
velocity_1 = 1
w = 0
z = 2*robot.get_height()
velocity_2 = 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot, (w, z))
    pygame.display.flip()
    
    x += velocity_1
    if velocity_1 > 0 and x + robot.get_width() >= 640:
        velocity_1 = -velocity_1
    if velocity_1 < 0 and x <= 0:
        velocity_1 = -velocity_1

    w += velocity_2
    if velocity_2 > 0 and w+robot.get_width() >= 640:
        velocity_2 = -velocity_2
    if velocity_2 < 0 and w <= 0:
        velocity_2 = -velocity_2

    clock.tick(100)