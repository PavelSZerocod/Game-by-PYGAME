import pygame

pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("ИГРА - SPACESHUTTLE")

image1 = pygame.image.load("space_ship.png")
image_rect1 = image1.get_rect()

image2 = pygame.image.load("meteorit.png")
image_rect2 = image2.get_rect()

sound = pygame.mixer.Sound("vzryiv-s-ognennyim-plamenem.wav")
sound.play()


speed = 1

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        image_rect1.x -= speed
        if image_rect1.left < 0:
            image_rect1.left = 0
    if keys[pygame.K_RIGHT]:
        image_rect1.x += speed
        if image_rect1.right > window_size[0]:
            image_rect1.right = window_size[0]
    if keys[pygame.K_UP]:
        image_rect1.y -= speed
        if image_rect1.top < 0:
            image_rect1.top = 0
    if keys[pygame.K_DOWN]:
        image_rect1.y += speed
        if image_rect1.bottom > window_size[1]:
            image_rect1.bottom = window_size[1]

    screen.fill((0, 0, 0))
    screen.blit(image1,image_rect1)
    screen.blit(image2, image_rect2)
    pygame.display.flip()



pygame.quit()
