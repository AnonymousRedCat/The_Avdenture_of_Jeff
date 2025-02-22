import pygame

pygame.init()

screen_width = 1200
screen_height = 900

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("The Adventure of Jeff")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 225, 0)
RED = (255, 0, 0)

player_acceleration = 5

entity_width = 50
entity_height = 50
entity_x = 300
entity_y = 300

while True:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        entity_x = entity_x - player_acceleration
    if keys[pygame.K_RIGHT]:
        entity_x = entity_x + player_acceleration
    if keys[pygame.K_UP]:
        entity_y = entity_y - player_acceleration
    if keys[pygame.K_DOWN]:
        entity_y = entity_y + player_acceleration
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(GREEN)  # draws background grass
    pygame.draw.rect(screen, BLUE, (entity_x, entity_y, entity_width, entity_height))
    pygame.draw.rect(screen, WHITE, (entity_x + 10, entity_y + 10, 10, 10))
    pygame.draw.rect(screen, WHITE, (entity_x + 30, entity_y + 10, 10, 10))
    pygame.draw.rect(screen, BLACK, (entity_x + 14, entity_y + 14, 5, 5))
    pygame.draw.rect(screen, BLACK, (entity_x + 34, entity_y + 14, 5, 5))
    pygame.draw.rect(screen, BLACK, (entity_x + 10, entity_y + 30, 20, 5))

    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()
