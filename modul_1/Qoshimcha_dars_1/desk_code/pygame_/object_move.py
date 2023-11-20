# pip install pygame
import pygame

pygame.init()

size = (800, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Player move")
tank_img = pygame.image.load("image/tank.png")
tank_img = pygame.transform.scale(tank_img, (100, 100))


tank_up = pygame.transform.rotate(tank_img , 180)
tank_down = pygame.transform.rotate(tank_img , 0)
tank_left = pygame.transform.rotate(tank_img , -90)
tank_right = pygame.transform.rotate(tank_img , 90)



tank_rect = tank_img.get_rect()
tank_rect.center = (size[0] // 2, size[1] // 2)


def move_tank():
    global tank_img
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and tank_rect.left > 0:
        tank_img = tank_left
        tank_rect.x -= 5
    elif key[pygame.K_d] and tank_rect.right < size[1]:
        tank_img = tank_right
        tank_rect.x += 5
    elif key[pygame.K_w] and tank_rect.top > 0:
        tank_img = tank_up
        tank_rect.y -= 5
    elif key[pygame.K_s] and tank_rect.bottom < size[0]:
        tank_img = tank_down
        tank_rect.y += 5


def QUIT():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




running = True
while running:
    screen.fill("green")
    screen.blit(tank_img, tank_rect)
    QUIT()
    move_tank()
    pygame.display.update()

pygame.quit()
