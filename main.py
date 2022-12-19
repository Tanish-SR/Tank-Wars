import os
import random
import time
import pygame

pygame.init()

display_width = 1000
display_height = 800
SCREEN = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Tank Wars!")

# colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

light_red = (150, 0, 0)
red = (255, 0, 0)

light_yellow = (200, 200, 0)
yellow = (254, 225, 1)
light_green = (34, 177, 76)
green = (0, 255, 0)

dark_purple = (153, 0, 153)
grey = (96, 96, 96)

midnight_blue = (27, 5, 87)

ground_height = 115

# background
BG = pygame.image.load(os.path.join("background-1.jpg"))
BG = pygame.transform.scale(BG, (display_width, display_height))


# font
def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Beckman-Free.otf", size)


# main Tank
tank_height1, tank_width1 = 40, 80

turrentWidth = 8
wheelWidth = 5


# font
def get_Font(size):
    return pygame.font.Font("Beckman-Free.otf", size)


# Barrier
def barrier(xlocation, randomheight, barrier_Width):
    pygame.draw.rect(SCREEN, grey, [xlocation, display_height - randomheight, barrier_Width, randomheight])


# drawing turrent + tank + wheels
def Right_Tank(x, y, turrPos):
    x = int(x)
    y = int(y)

    # turrent position
    possibleTurrent = [(x - 50, y - 15),
                       (x - 49, y - 17),
                       (x - 48, y - 20),
                       (x - 47, y - 24),
                       (x - 45, y - 29),
                       (x - 43, y - 34),
                       (x - 38, y - 39),
                       (x - 39, y - 43),
                       (x - 34, y - 48),
                       (x - 30, y - 52),
                       (x - 24, y - 57),
                       ]

    # turrents base
    pygame.draw.circle(SCREEN, red, (x, y), int(tank_height1 / 2))
    pygame.draw.rect(SCREEN, red, (x - tank_height1, y, tank_width1, tank_height1))

    # turrent
    pygame.draw.line(SCREEN, red, (x, y), possibleTurrent[turrPos], turrentWidth)

    # wheels
    pygame.draw.circle(SCREEN, red, (x - 35, y + 40), wheelWidth)
    pygame.draw.circle(SCREEN, red, (x - 27, y + 40), wheelWidth)

    pygame.draw.circle(SCREEN, red, (x - 35, y + 40), wheelWidth)
    pygame.draw.circle(SCREEN, red, (x - 27, y + 40), wheelWidth)
    pygame.draw.circle(SCREEN, red, (x - 19, y + 40), wheelWidth)
    pygame.draw.circle(SCREEN, red, (x - 11, y + 40), wheelWidth)
    pygame.draw.circle(SCREEN, red, (x - 3, y + 40), wheelWidth)
    pygame.draw.circle(SCREEN, red, (x + 5, y + 40), wheelWidth)
    pygame.draw.circle(SCREEN, red, (x + 13, y + 40), wheelWidth)
    pygame.draw.circle(SCREEN, red, (x + 21, y + 40), wheelWidth)
    pygame.draw.circle(SCREEN, red, (x + 29, y + 40), wheelWidth)
    pygame.draw.circle(SCREEN, red, (x + 35, y + 40), wheelWidth)
    return possibleTurrent[turrPos]


# Left tank
def left_tank(x, y, l_turrPos):
    x = int(x)
    y = int(y)

    l_possibleTurrent = [(x + 45, y - 15),
                         (x + 44, y - 17),
                         (x + 43, y - 20),
                         (x + 42, y - 29),
                         (x + 45, y - 34),
                         (x + 43, y - 39),
                         (x + 38, y - 43),
                         (x + 39, y - 48),
                         (x + 34, y - 52),
                         (x + 30, y - 57),
                         (x + 24, y - 61),
                         (x + 8, y - 63),
                         (x + 2, y - 65)
                         ]

    pygame.draw.circle(SCREEN, light_green, (x, y), int(tank_height1 / 2))
    pygame.draw.rect(SCREEN, light_green, (x - tank_height1, y, tank_width1, tank_height1))

    # turrent
    pygame.draw.line(SCREEN, light_green, (x, y), l_possibleTurrent[l_turrPos], turrentWidth)

    # wheels
    pygame.draw.circle(SCREEN, light_green, (x - 35, y + 40), wheelWidth)
    pygame.draw.circle(SCREEN, light_green, (x - 27, y + 40), wheelWidth)
    pygame.draw.circle(SCREEN, light_green, (x - 19, y + 40), wheelWidth)
    pygame.draw.circle(SCREEN, light_green, (x - 11, y + 40), wheelWidth)
    pygame.draw.circle(SCREEN, light_green, (x - 3, y + 40), wheelWidth)
    pygame.draw.circle(SCREEN, light_green, (x + 5, y + 40), wheelWidth)
    pygame.draw.circle(SCREEN, light_green, (x + 13, y + 40), wheelWidth)
    pygame.draw.circle(SCREEN, light_green, (x + 21, y + 40), wheelWidth)
    pygame.draw.circle(SCREEN, light_green, (x + 29, y + 40), wheelWidth)
    pygame.draw.circle(SCREEN, light_green, (x + 35, y + 40), wheelWidth)
    return l_possibleTurrent[l_turrPos]


# R_fire
def r_fire(xy, turPos, r_firepower, xlocation, barrier_Width, randomheight, l_tankx):
    fire = True
    damage = 0
    coordinates = list(xy)
    clock = pygame.time.Clock()
    FPS = 60
    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # print(coordinates[0], coordinates[1])
        pygame.draw.circle(SCREEN, red, (coordinates[0], coordinates[1]), 5)

        coordinates[0] -= (12 - turPos) * 2
        # print(coordinates[0])
        coordinates[1] += int(
            (((coordinates[0] - xy[0]) * 0.015 / (r_firepower / 50)) ** 2) - (turPos + turPos / (12 - turPos)))
        # print(coordinates[1])

        if coordinates[1] > display_height - ground_height:
            fire = False

            hit_x = int((coordinates[0] * display_height - ground_height) / coordinates[1])
            hit_y = int(display_height - ground_height)

            if l_tankx + 10 > hit_x > l_tankx - 10:
                print('Critical Hit')
                damage = 25
            elif l_tankx + 15 > hit_x > l_tankx - 15:
                print("Hard Hit!")
                damage = 18
            elif l_tankx + 25 > hit_x > l_tankx - 25:
                print("Medium Hit")
                damage = 10
            elif l_tankx + 35 > hit_x > l_tankx - 35:
                print("Light Hit")
                damage = 5

            explosion(hit_x, hit_y)

        check_x_1 = coordinates[0] <= xlocation + barrier_Width
        check_x_2 = coordinates[0] >= xlocation

        check_y_1 = coordinates[1] <= display_height
        check_y_2 = coordinates[1] >= display_height - randomheight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            fire = False

            hit_x = int(coordinates[0])
            hit_y = int(coordinates[1])

            explosion(hit_x, hit_y)

        pygame.display.update()
        clock.tick(FPS)
    return damage


# L_fire
def l_fire(xy, turPos, l_firepower, xlocation, barrier_Width, randomheight, r_tankx):
    fire = True
    damage = 0
    coordinates = list(xy)
    clock = pygame.time.Clock()
    FPS = 60
    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # print(coordinates[0], coordinates[1])
        pygame.draw.circle(SCREEN, red, (coordinates[0], coordinates[1]), 5)

        coordinates[0] += (12 - turPos) * 2
        # print(coordinates[0])
        coordinates[1] += int(
            (((coordinates[0] - xy[0]) * 0.015 / (l_firepower / 50)) ** 2) - (turPos + turPos / (12 - turPos)))
        # print(coordinates[1])

        if coordinates[1] > display_height - ground_height:
            fire = False

            hit_x = int((coordinates[0] * display_height - ground_height) / coordinates[1])
            hit_y = int(display_height - ground_height)

            if r_tankx + 10 > hit_x > r_tankx - 10:
                print('Critical Hit')
                damage = 25
            elif r_tankx + 15 > hit_x > r_tankx - 15:
                print("Hard Hit!")
                damage = 18
            elif r_tankx + 25 > hit_x > r_tankx - 25:
                print("Medium Hit")
                damage = 10
            elif r_tankx + 35 > hit_x > r_tankx - 35:
                print("Light Hit")
                damage = 5
            explosion(hit_x, hit_y)

        check_x_1 = coordinates[0] <= xlocation + barrier_Width
        check_x_2 = coordinates[0] >= xlocation

        check_y_1 = coordinates[1] <= display_height
        check_y_2 = coordinates[1] >= display_height - randomheight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            fire = False

            hit_x = int(coordinates[0])
            hit_y = int(coordinates[1])

            explosion(hit_x, hit_y)

        pygame.display.update()
        clock.tick(FPS)
    return damage


# r_fire power
def r_power(power_level):
    text = get_Font(20).render(f'Power: ' + str(power_level) + '', True, white)
    SCREEN.blit(text, (display_width / 2, 0))


# l_fire power
def l_power(power_level):
    text = get_Font(20).render(f'Power: ' + str(power_level) + '', True, white)
    SCREEN.blit(text, (display_width / 7, 0))


# explotion
def explosion(x, y, size=50):
    explode = True
    clock = pygame.time.Clock()
    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        colorChoices = [red, light_red, yellow, light_yellow]

        magnitude = 1
        while magnitude < size:
            exploding_x = x + random.randrange(-1 * magnitude, magnitude)
            exploding_y = y + random.randrange(-1 * magnitude, magnitude)

            pygame.draw.circle(SCREEN, colorChoices[random.randrange(0, 4)], (exploding_x, exploding_y),
                               random.randrange(1, 5))
            magnitude += 1
            pygame.display.update()
            clock.tick(100)
        explode = False


# health bars
def health_bars(player1, player2):
    global player1_color, player2_color
    if player1 > 75:
        player1_color = green
    elif player1 < 75:
        player1_color = yellow
    if player1 < 25:
        player1_color = red

    # player 2 health
    if player2 > 75:
        player2_color = green
    elif player2 < 75:
        player2_color = yellow
    if player2 < 25:
        player2_color = red

    pygame.draw.rect(SCREEN, player1_color, (280, 25, player1, 25))
    pygame.draw.rect(SCREEN, player2_color, (680, 25, player2, 25))

    if player1 == 0:
        game_over(player1, player2)

    elif player2 == 0:
        game_over(player1, player2)


def game_over(player1, player2):
    game_over = True
    clock = pygame.time.Clock()
    while game_over:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # background
        SCREEN.blit(BG, (0, 0))
        text = get_Font(50).render('Game Over', True, white)
        SCREEN.blit(text, (400, 300))
        if player1 == 0:
            text = get_Font(50).render('player2 Wins', True, black)
            SCREEN.blit(text, (400, 400))
        elif player2 == 0:
            text = get_Font(50).render('player1 Wins', True, black)
            SCREEN.blit(text, (400, 400))

        # btn("Play Again", 150, 500, 150, 50, wheat, light_green, action="play")
        # btn("Controls", 350, 500, 100, 50, wheat, light_yellow, action="controls")
        # btn("Quit", 550, 500, 100, 50, wheat, light_red, action="quit")

        pygame.display.update()

        clock.tick(15)


# main
FPS = 15


def main():
    clock = pygame.time.Clock()
    run = True

    # health bar
    player1 = 100
    player2 = 100

    # moving tank
    r_tankx = display_width * 0.9
    r_tanky = display_height * 0.8
    tankMove = 0

    # barrier
    xlocation = (display_width / 2) + random.randint(-0.1 * display_width, 0.1 * display_width)
    randomheight = random.randrange(display_height * 0.3, display_height * 0.5)
    barrier_Width = 50
    # moving left tank
    l_tankx = display_width * 0.1
    l_tanky = display_height * 0.8
    l_tankMove = 0

    # turrent pos
    currentTurPos = 0
    changeTur = 0

    # left turrent pos
    l_currentTurPos = 0
    l_changeTur = 0

    # l_firepower
    l_firePower = 50
    l_powerchange = 0

    # r_firepower
    r_firePower = 50
    r_powerchange = 0

    while run:

        # Gun
        r_gun = Right_Tank(r_tankx, r_tanky, currentTurPos)
        l_gun = left_tank(l_tankx, l_tanky, l_currentTurPos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5
                elif event.key == pygame.K_RIGHT:
                    tankMove = 5
                elif event.key == pygame.K_DOWN:
                    changeTur = -1
                    time.sleep(0.05)
                elif event.key == pygame.K_UP:
                    changeTur = 1
                    time.sleep(0.05)
                elif event.key == pygame.K_SLASH:
                    damage = r_fire(r_gun, currentTurPos, r_firePower, xlocation, barrier_Width,
                                    randomheight, l_tankx)
                    player1 -= damage
                elif event.key == pygame.K_PERIOD:
                    r_powerchange += 1
                elif event.key == pygame.K_COMMA:
                    r_powerchange -= 1

            # left tank controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    l_tankMove = -5
                elif event.key == pygame.K_d:
                    l_tankMove = 5
                elif event.key == pygame.K_s:
                    l_changeTur = -1
                    time.sleep(0.05)
                elif event.key == pygame.K_w:
                    l_changeTur = 1
                    time.sleep(0.05)
                elif event.key == pygame.K_q:
                    damage = l_fire(l_gun, l_currentTurPos, l_firePower, xlocation, barrier_Width,
                                    randomheight, r_tankx)
                    player2 -= damage
                elif event.key == pygame.K_e:
                    l_powerchange += 1
                elif event.key == pygame.K_r:
                    l_powerchange -= 1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    tankMove = 0
                    l_tankMove = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    changeTur = 0
                    l_changeTur = 0
                if event.key == pygame.K_PERIOD or pygame.K_COMMA:
                    r_powerchange = 0
                if event.key == pygame.K_e or pygame.K_r:
                    l_powerchange = 0

        # background
        SCREEN.blit(BG, (0, 0))

        # bar
        health_bars(player1, player2)

        r_tankx += tankMove
        currentTurPos += changeTur

        l_tankx += l_tankMove
        l_currentTurPos += l_changeTur

        if l_currentTurPos > 10:
            l_currentTurPos = 10
        elif l_currentTurPos < 0:
            l_currentTurPos = 0

        if currentTurPos > 10:
            currentTurPos = 10
        elif currentTurPos < 0:
            currentTurPos = 0

        if r_tankx - (tank_width1 / 2) < xlocation + barrier_Width:
            r_tankx += 5

        if l_tankx - (tank_width1 / 2) >= xlocation + barrier_Width:
            l_tankx += 5

        Right_Tank(r_tankx, r_tanky, currentTurPos)
        left_tank(l_tankx, l_tanky, l_currentTurPos)

        # barier
        barrier(xlocation, randomheight, barrier_Width)

        # fire power
        l_firePower += l_powerchange

        if l_firePower > 100:
            l_firePower = 100
        elif l_firePower < 1:
            l_firePower = 1

        r_firePower += r_powerchange
        if r_firePower > 100:
            r_firePower = 100
        elif r_firePower < 1:
            r_firePower = 1

        r_power(r_firePower)
        l_power(l_firePower)

        # adding ground
        SCREEN.fill(midnight_blue, rect=[0, display_height - ground_height, display_width, ground_height])

        # adding details
        pygame.draw.circle(SCREEN, yellow, (5, 710), 14)
        pygame.draw.circle(SCREEN, yellow, (110, 750), 24)
        pygame.draw.circle(SCREEN, yellow, (300, 790), 31)
        pygame.draw.circle(SCREEN, yellow, (220, 750), 21)
        pygame.draw.circle(SCREEN, yellow, (450, 740), 23)
        pygame.draw.circle(SCREEN, yellow, (450, 740), 23)
        pygame.draw.circle(SCREEN, yellow, (490, 800), 29)
        pygame.draw.circle(SCREEN, yellow, (600, 740), 40)
        pygame.draw.circle(SCREEN, yellow, (700, 790), 20)
        pygame.draw.circle(SCREEN, yellow, (750, 730), 15)
        pygame.draw.circle(SCREEN, yellow, (800, 750), 25)
        pygame.draw.circle(SCREEN, yellow, (880, 790), 42)
        pygame.draw.circle(SCREEN, yellow, (940, 730), 22)

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()

main()
