# pip install pygame
import pygame

pygame.init()

size = (800, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mario game")
mario_img = pygame.image.load("mario.png")
mario_img = pygame.transform.scale(mario_img, (150, 200))

# mario_up = pygame.transform.rotate(mario_img, 180)
# mario_down = pygame.transform.rotate(mario_img, 0)
# mario_left = pygame.transform.rotate(mario_img, -90)
# mario_right = pygame.transform.rotate(mario_img, 90)

mario_rect = mario_img.get_rect()
mario_rect.center = (size[0] // 2, size[1] // 2)


def move_tank():
    global mario_img
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and mario_rect.left > 0:
        # mario_img = mario_left
        mario_rect.x -= 5
    elif key[pygame.K_d] and mario_rect.right < size[1]:
        # mario_img = mario_right
        mario_rect.x += 5
    elif key[pygame.K_w] and mario_rect.top > 0:
        # mario_img = mario_up
        mario_rect.y -= 5
    elif key[pygame.K_s] and mario_rect.bottom < size[0]:
        # mario_img = mario_down
        mario_rect.y += 5


def QUIT():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


running = True
while running:
    screen.fill((30,20,20))
    screen.blit(mario_img, mario_rect)
    QUIT()
    move_tank()
    pygame.display.update()

pygame.quit()
