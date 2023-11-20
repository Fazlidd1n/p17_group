import pygame

pygame.init()

size = width, hight = 1000, 700
speed = [3, 3]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("ball game")
ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball,(180,150))
ball_rect = ball.get_rect()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ball_rect = ball_rect.move(speed)
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > hight:
        speed[1] = -speed[1]
    screen.fill("darkgreen")
    screen.blit(ball, ball_rect)

    pygame.display.flip()
