import pygame
import random

pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("ИГРА - SPACESHUTTLE")

background_images = [pygame.image.load("космос 1.jpg"), pygame.image.load("космос 2.jpg"),
                     pygame.image.load("космос 3.jpg"), pygame.image.load("космос 4.jpg")]

def get_random_background():
    return random.choice(background_images)

def reset_game():
    global image_rect1, image_rect2, meteorit_speed, current_background, death_count, start_time
    if death_count < 10:
        current_background = get_random_background()
        image_rect1.x = (window_size[0] - image_rect1.width) // 2
        image_rect1.y = window_size[1] - image_rect1.height
        image_rect2.x = random.randint(0, window_size[0] - image_rect2.width)
        image_rect2.y = -image_rect2.height
        meteorit_speed = random.randint(1, 2)
        death_count += 1
        start_time = pygame.time.get_ticks()

current_background = get_random_background()

image1 = pygame.image.load("space_ship.png")
image_rect1 = image1.get_rect()

image_rect1.x = (window_size[0] - image_rect1.width) // 2
image_rect1.y = window_size[1] - image_rect1.height

image2 = pygame.image.load("meteorit.png")
image_rect2 = image2.get_rect()


sound2 = pygame.mixer.Sound("electric-galaxy-20240519-sovrt.wav")
sound2.play()
sound = pygame.mixer.Sound("vzryiv-s-ognennyim-plamenem.wav")


speed = 1
meteorit_speed = 2

death_count = 0

font = pygame.font.SysFont(None, 36)

reset_game()

game_over = False

button_font = pygame.font.SysFont(None, 48)
button_text = button_font.render("Играть еще раз", True, (255, 255, 255))
game_over_text = button_font.render("Игра окончена", True, (255, 0, 0))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if game_over and event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                game_over = False
                death_count = 0
                reset_game()

    if not game_over:
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

        image_rect2.y += meteorit_speed

        if image_rect2.top > window_size[1]:
            image_rect2.x = random.randint(0, window_size[0] - image_rect2.width)
            image_rect2.y = -image_rect2.height
            meteorit_speed = random.randint(1, 2)

        if image_rect1.colliderect(image_rect2):
            sound.play()
            if death_count < 9:
                reset_game()
            else:
                game_over = True

        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000

    screen.blit(current_background, (0, 0))
    screen.blit(image1, image_rect1)
    screen.blit(image2, image_rect2)

    death_text = font.render(f"Смерти: {death_count}", True, (255, 255, 255))
    screen.blit(death_text, (window_size[0] - death_text.get_width() - 10, window_size[1] - death_text.get_height() - 10))

    if not game_over:
        time_text = font.render(f"Время: {elapsed_time} сек", True, (255, 255, 255))
        screen.blit(time_text, (10, window_size[1] - time_text.get_height() - 10))

    if game_over:
        game_over_rect = game_over_text.get_rect(center=(window_size[0] // 2, window_size[1] // 2))
        screen.blit(game_over_text, game_over_rect.topleft)
        button_rect = button_text.get_rect(center=(window_size[0] // 2, game_over_rect.bottom + 50))
        screen.blit(button_text, button_rect.topleft)

    pygame.display.flip()

pygame.quit()