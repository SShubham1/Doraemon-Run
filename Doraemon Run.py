import pygame

pygame.init()

window_height = 676
window_width = 1200
window_title = "Doraemon Run"
white = (255, 255, 255)
window_icon = pygame.image.load("icon.png")
game_exit = False
doraemon_sprite = [pygame.image.load("D1.png"), pygame.image.load("D2.png"), pygame.image.load("D3.png"),
                   pygame.image.load("D4.png"), pygame.image.load("D5.png"), pygame.image.load("D6.png")]
background_sprite = pygame.image.load("bg.png")
bigcloud = pygame.image.load("bigcloud.png")
medcloud = pygame.image.load("mediumcloud.png")
smallcloud = pygame.image.load("smallcloud.png")
med_x = 800
med_y = 100
big_x = 100
big_y = 200
small_x = 1200
small_y = 50
walk_count = 0
shown_time = 0
fps = 60

pygame.display.set_icon(window_icon)
pygame.display.set_caption(window_title)
game_window = pygame.display.set_mode((window_width, window_height))

clock = pygame.time.Clock()


def redraw_game_window():
    global walk_count, shown_time, big_x, med_x, small_x
    game_window.fill(white)
    game_window.blit(background_sprite, (0, 0))
    game_window.blit(bigcloud, (big_x, big_y))
    game_window.blit(medcloud, (med_x, med_y))
    game_window.blit(smallcloud, (small_x, small_y))
    big_x = big_x - 1.5
    med_x = med_x - 1.4
    small_x = small_x - 1.3
    if big_x <= -250:
        big_x = 1300
    if med_x <= -200:
        med_x = 1300
    if small_x <= -200:
        small_x = 1300
    game_window.blit(doraemon_sprite[walk_count], (0, 360))
    shown_time = shown_time + 1
    if shown_time >= 7:
        walk_count = walk_count + 1
        shown_time = 0
    if walk_count >= 6:
        walk_count = 0


while not game_exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
    redraw_game_window()
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
