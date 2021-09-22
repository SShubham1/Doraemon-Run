#!/bin/env python3
import pygame

pygame.init()


class Sprite:

    def __init__(self, x, y, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.x = x
        self.rect.y = self.y = y

    def render(self):
        self.rect.y = self.y
        self.rect.x = self.x
        game_window.blit(self.image, (self.rect.x, self.rect.y))

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)


white = (255, 255, 255)
font = pygame.font.SysFont(str('freesansbold.ttf'), 40)

window_width = 1200
window_height = 676
game_exit = False
doraemon_died = False
walk_count = 0
shown_time = 0
fps = 60
# Force (v) up and mass m.
v = 14
y = 360
m = 1
score = 0
isjump = False
res_folder = "res/"

doraemon_img = [res_folder + "D1.png", res_folder + "D2.png",
                res_folder + "D3.png", res_folder + "D4.png",
                res_folder + "D5.png", res_folder + "D6.png",
                res_folder + "died.png"]
background_img = pygame.image.load(res_folder + "bg.png")
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_icon(pygame.image.load(res_folder+"icon.png"))
pygame.display.set_caption("Doraemon Run - version.1.0")
clock = pygame.time.Clock()

pipe = Sprite(1500, 520, res_folder + "pipe.png")
rock = Sprite(1800, 540, res_folder + "rock.png")
bigcloud = Sprite(100, 200, res_folder + "bigcloud.png")
smallcloud = Sprite(1200, 50, res_folder + "smallcloud.png")
medcloud = Sprite(800, 100, res_folder + "mediumcloud.png")
c1 = Sprite(1600, 500, res_folder + "cake.png")
c2 = Sprite(1700, 500, res_folder + "cake.png")
c3 = Sprite(1800, 500, res_folder + "cake.png")
c4 = Sprite(1900, 500, res_folder + "cake.png")
c5 = Sprite(2000, 500, res_folder + "cake.png")
c6 = Sprite(2100, 500, res_folder + "cake.png")
c7 = Sprite(2200, 500, res_folder + "cake.png")
c8 = Sprite(2300, 500, res_folder + "cake.png")
c9 = Sprite(2400, 500, res_folder + "cake.png")
c10 = Sprite(2500, 500, res_folder + "cake.png")
c11 = Sprite(2600, 500, res_folder + "cake.png")
c12 = Sprite(2700, 500, res_folder + "cake.png")
c13 = Sprite(2800, 500, res_folder + "cake.png")
c14 = Sprite(2900, 500, res_folder + "cake.png")
c15 = Sprite(3000, 500, res_folder + "cake.png")
c16 = Sprite(3100, 500, res_folder + "cake.png")
c17 = Sprite(3200, 500, res_folder + "cake.png")



def doraemon_render():
    global walk_count, shown_time, isjump, m, v, game_exit, score, y, doraemon_died
    doraemon = Sprite(0, y, doraemon_img[walk_count])
    if shown_time >= 7 and walk_count != 6:
        walk_count = walk_count + 1
        shown_time = 0
    if walk_count == 5:
        walk_count = 0

    if doraemon.is_collided_with(rock):
        if doraemon.x <= rock.x - 20:
            doraemon_died = True
            walk_count = 6

    if doraemon.is_collided_with(pipe):
        if doraemon.rect.x + 120 < pipe.rect.x:
            if doraemon.x <= rock.x - 20:
                doraemon_died = True
                walk_count = 6
        else:
            doraemon.y = pipe.y - 240

    if doraemon.is_collided_with(c1):
        c1.x = 1600
        score += 10

    if doraemon.is_collided_with(c2):
        c2.x = 1700
        score += 10
    if doraemon.is_collided_with(c3):
        c3.x = 1800
        score += 10
    if doraemon.is_collided_with(c4):
        c4.x = 1900
        score += 10
    if doraemon.is_collided_with(c5):
        c5.x = 2000
        score += 10

    if doraemon.is_collided_with(c6):
        c6.x = 2100
        score += 10
    if doraemon.is_collided_with(c7):
        c7.x = 2200
        score += 10
    if doraemon.is_collided_with(c8):
        c8.x = 2300
        score += 10
    if doraemon.is_collided_with(c9):
        c9.x = 2400
        score += 10

    if doraemon.is_collided_with(c10):
        c10.x = 2500
        score += 10
    if doraemon.is_collided_with(c11):
        c11.x = 2600
        score += 10
    if doraemon.is_collided_with(c12):
        c12.x = 2700
        score += 10
    if doraemon.is_collided_with(c13):
        c1.x = 2800
        score += 10

    if doraemon.is_collided_with(c14):
        c1.x = 2900
        score += 10
    if doraemon.is_collided_with(c15):
        c1.x = 3000
        score += 10
    if doraemon.is_collided_with(c16):
        c1.x = 3100
        score += 10
    if doraemon.is_collided_with(c17):
        c1.x = 3200
        score += 10

    doraemon.render()


def redraw_game_window():
    global walk_count, shown_time, game_exit

    text = font.render('Score: ' + str(score), True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.x = 10
    text_rect.y = 10
    game_window.fill(white)
    game_window.blit(background_img, (0, 0))

    bigcloud.render()
    smallcloud.render()
    medcloud.render()

    doraemon_render()
    rock.render()
    pipe.render()
    c1.render()
    c2.render()
    c3.render()
    c4.render()
    c5.render()
    c6.render()
    c7.render()
    c8.render()
    c9.render()
    c10.render()
    c11.render()
    c12.render()
    c13.render()
    c14.render()
    c15.render()
    c16.render()
    c17.render()
    game_window.blit(text, text_rect)


def game_over():
    global res_folder, game_exit, doraemon_died, walk_count, shown_time, v, y, m, score, isjump, fps, pipe, rock
    dgo = pygame.image.load(res_folder + "doraemon_gameover.png")
    text_go = pygame.font.Font("freesansbold.ttf", 64).render("Game Over!", True, (255, 0, 0))
    text_go_rect = text_go.get_rect()
    text_go_rect.centerx = (window_width / 2)
    bgot = pygame.font.Font("freesansbold.ttf", 48).render("Try Again", True, (0, 255, 0))
    bgo = bgot.get_rect()
    bgo.centerx = window_width / 2
    cre1 = pygame.font.Font("freesansbold.ttf", 32).render("Made by", True, (255, 0, 0))
    cre2 = pygame.font.Font("freesansbold.ttf", 32).render("Shubham Shrivastav", True, (255, 0, 0))
    creb1 = cre1.get_rect()
    creb2 = cre2.get_rect()
    creb2.bottomright = (window_width, window_height)
    creb1.bottomright = (creb2.centerx + 75, window_height - 32)

    bgo.y = 300
    rectbgo = pygame.rect.Rect(bgo.x - 25, bgo.y - 25, bgo.width + 50, bgo.height + 50)
    scoretext = pygame.font.Font("freesansbold.ttf", 32).render("Score: " + str(score), True, (255, 0, 0))
    scoretextr = scoretext.get_rect()
    scoretextr.centerx = window_width / 2
    scoretextr.y = 450
    text_go_rect.y = 100
    game_exit = False
    doraemon_died = False
    walk_count = 0
    shown_time = 0
    # Force (v) up and mass m.
    pipe = Sprite(1500, 520, res_folder + "pipe.png")
    rock = Sprite(1800, 540, res_folder + "rock.png")
    v = 14
    y = 360
    m = 1

    score = 0
    isjump = False
    while not game_exit:
        game_window.fill((0, 100, 255))
        game_window.blit(text_go, text_go_rect)
        game_window.blit(dgo, (100, 200))
        pygame.draw.rect(game_window, (255, 0, 0), rectbgo)
        pygame.draw.rect(game_window, (255, 0, 0), bgo)
        game_window.blit(bgot, bgo)
        game_window.blit(scoretext, scoretextr)
        game_window.blit(cre1, creb1)
        game_window.blit(cre2, creb2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            key = pygame.key.get_pressed()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if rectbgo.x <= mouse[0] <= rectbgo.x+bgo.width+50 and rectbgo.y <= mouse[
                    1] <= rectbgo.y + bgo.height + 50:
                    gameloop()
                    break
            if key[pygame.K_RETURN]:
                gameloop()
                break
        pygame.display.update()
        clock.tick(fps)


def gameloop():
    global game_exit, shown_time, isjump, m, v, y
    while not game_exit:
        if not doraemon_died:
            c1.x -= 10
            c2.x -= 10
            c3.x -= 10
            c4.x -= 10
            c5.x -= 10
            c6.x -= 10
            c7.x -= 10
            c8.x -= 10
            c9.x -= 10
            c10.x -= 10
            c11.x -= 10
            c12.x -= 10
            c13.x -= 10
            c14.x -= 10
            c15.x -= 10
            c16.x -= 10
            c17.x -= 10

            if c1.x <= 0:
                c1.x = 1600
            if c2.x <= 0:
                c2.x = 1700
            if c3.x <= 0:
                c3.x = 1800
            if c4.x <= 0:
                c4.x = 1900
            if c5.x <= 0:
                c5.x = 2000
            if c6.x <= 0:
                c6.x = 2100
            if c7.x <= 0:
                c7.x = 2200
            if c8.x <= 0:
                c8.x = 2300
            if c9.x <= 0:
                c9.x = 2400
            if c10.x <= 0:
                c10.x = 2500
            if c11.x <= 0:
                c11.x = 2600
            if c12.x <= 0:
                c12.x = 2700
            if c13.x <= 0:
                c13.x = 2800
            if c14.x <= 0:
                c14.x = 2900
            if c15.x <= 0:
                c15.x = 3000
            if c16.x <= 0:
                c16.x = 3100
            if c17.x <= 0:
                c17.x = 3200

            bigcloud.x = bigcloud.x - 1.5
            medcloud.x = medcloud.x - 1.4
            smallcloud.x = smallcloud.x - 1.3
            if bigcloud.x <= -250:
                bigcloud.x = 1300
            if medcloud.x <= -200:
                medcloud.x = 1300
            if smallcloud.x <= -200:
                smallcloud.x = 1300

            shown_time = shown_time + 1
            rock.x = rock.x - 10
            pipe.x = pipe.x - 13
            if rock.x <= -200:
                rock.x = 1400
            if pipe.x <= -200:
                pipe.x = 1800
        else:
            if y <= 800:
                y += 10
            else:
                game_over()
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.MOUSEBUTTONDOWN and not isjump and not doraemon_died:
                isjump = True

        keys = pygame.key.get_pressed()
        if not isjump and not doraemon_died:
            if keys[pygame.K_SPACE]:
                isjump = True
        if isjump:
            f = (1 / 2) * m * (v ** 2)

            y -= f
            v = v - 1
            if v < 0:
                m = -1
            if v == -15:
                isjump = False
                v = 14
                m = 1
        redraw_game_window()

        pygame.display.update()
        clock.tick(fps)


gameloop()

pygame.quit()
