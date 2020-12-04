import pygame
import sys
import random

pygame.init()

# title
game_title = 'Doodle Cube!'

# set display
win = pygame.display.set_mode((750, 500), pygame.FULLSCREEN)
pygame.display.set_caption(game_title)

# load images
cloud = pygame.image.load('999-cloud-clipart-free-download-' +
'transparent-png-cloud-clipart-cloud-clipart-transparent-1044_592.png')
cloud = pygame.transform.scale(cloud, (128, 72))

# fonts
pygame.font.init()
font = pygame.font.SysFont('noteworthyttc', 60)
font_2 = pygame.font.SysFont('timesnewromanttf', 30)
font_3 = pygame.font.SysFont('timesnewromanttf', 25)
font_4 = pygame.font.SysFont('timesnewromanttf', 13)
font_5 = pygame.font.SysFont('noteworthyttc', 30)
font_6 = pygame.font.SysFont('timesnewromanttf', 20)

# colors
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (128, 0, 128)
pink = (255, 192, 203)
grey = (110, 110, 100)
brown = (139, 69, 19)
white = (255, 255, 255)
light_blue = (173, 216, 230)
navy = (0, 0, 200)
black = (0, 0, 0)
other_blue = (48, 131, 159)
title_blue = (0, 102, 204)
light_green = (153, 255, 153)
light_grey = (224, 224, 224)

# clouds
cloud_values = []
i = 0
while i < 10:
    cloud_values.append([random.randint(-750, -80), random.randint(-50, 550)])
    i += 1

def title_screen():
    run_title = True
    run = True
    show_help = False
    play_game = False

    while run_title:

        # background
        pygame.draw.rect(win, light_blue, pygame.Rect(0, 0, 750, 500))

        # clouds
        for i in range(len(cloud_values)):
            win.blit(cloud, (cloud_values[i][0], cloud_values[i][1]))
            cloud_values[i][0] += 5
            if cloud_values[i][0] > 760:
                cloud_values[i][0] = random.randint(-750, -80)
        pygame.draw.rect(win, black, pygame.Rect(0, 500, 1000, 400))
        pygame.draw.rect(win, black, pygame.Rect(750, 0, 300, 1000))

        # buttons
        play_button = pygame.draw.rect(win, other_blue, pygame.Rect(150, 175, 450, 75))
        help_button = pygame.draw.rect(win, other_blue, pygame.Rect(150, 275, 450, 75))
        quit_button = pygame.draw.rect(win, other_blue, pygame.Rect(150, 375, 450, 75))
        text = font_2.render('PLAY', True, white)
        text_2 = font_2.render('HELP', True, white)
        text_3 = font_2.render('QUIT', True, white)
        title = font.render(game_title, True, title_blue)
        win.blit(text, (340, 197))
        win.blit(text_2, (340, 297))
        win.blit(text_3, (340, 397))
        win.blit(title, (225, 60))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False

        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # if click happens
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0] > 150 and pos[0] < 600 and pos[1] > 175 and pos[1] < 250:
                    play_game = True
                elif pos[0] > 150 and pos[0] < 600 and pos[1] > 275 and pos[1] < 375:
                    show_help = True
                elif pos[0] > 150 and pos[0] < 600 and pos[1] > 375 and pos[1] < 450:
                    run = False

        # button reactions
        if pos[0] > 150 and pos[0] < 600 and pos[1] > 175 and pos[1] < 250:
            pygame.draw.rect(win, other_blue, pygame.Rect(145, 170, 460, 85))
            win.blit(text, (340, 197))
        elif pos[0] > 150 and pos[0] < 600 and pos[1] > 275 and pos[1] < 375:
            pygame.draw.rect(win, other_blue, pygame.Rect(145, 270, 460, 85))
            win.blit(text_2, (340, 297))
        elif pos[0] > 150 and pos[0] < 600 and pos[1] > 375 and pos[1] < 450:
            pygame.draw.rect(win, other_blue, pygame.Rect(145, 370, 460, 85))
            win.blit(text_3, (340, 397))

        # checks for start of game or help screen or quit
        if play_game or show_help or not run:
            run_title = False

        # author's name
        author_text = font_6.render('Made By: Brendan Perry | 2020', True, black)
        win.blit(author_text, (484, 468))

        # updates display
        pygame.display.flip()

    return run_title, play_game, run, show_help

def game_play():
    run_game = True
    run = True
    x = 350
    y = 225
    x_box = 475
    width = 50
    height = 50
    color = red
    vel = 10
    count = 50

    # loads in saved file
    new_parts = []
    saved_rects = []
    new_rect = []
    file_saved_rects = []
    saved_file = open('draw_file.txt', 'r+')
    for line in saved_file:
        new_rect = []
        parts = line.strip('\n | ').split(' | ')
        for part in parts:
            if part.isnumeric():
                new_rect.append(int(part))
            else:
                numbers = part.strip('()').split(', ')
                new_numbers = []
                for number in numbers:
                    new_number = int(number)
                    new_numbers.append(new_number)
                new_rect.append(tuple(new_numbers))
        file_saved_rects.append(new_rect)
    saved_file.write('')
    saved_file.close()

    while run_game:

        pygame.draw.rect(win, black, pygame.Rect(0, 500, 1000, 400))

        keys = pygame.key.get_pressed()

        # background
        pygame.draw.rect(win, white, pygame.Rect(0, 0, 750, 500))

        # clear board
        if keys[pygame.K_BACKSPACE]:
            pygame.draw.rect(win, white, pygame.Rect(0, 0, 750, 500))
            saved_rects = []

        # prints all saved and currently drawn rectangles
        for rect in saved_rects:
            pygame.draw.rect(win, rect[4], pygame.Rect(rect[0], rect[1], rect[2], rect[3]))

        # speed up / down keys
        if keys[pygame.K_PERIOD]:
            count += 1
            if count % 5 == 0:
                vel += 1
                if vel >= 40:
                    vel = 40
            if count >= 200:
                count = 200
        if keys[pygame.K_COMMA]:
            count -= 1
            if count % 5 == 0:
                vel -= 1
                if vel <= 0:
                    vel = 0
            if count <= 0:
                count = 0

        # movement
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            y -= vel
            if y <= 43:
                y = 43
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            y += vel
            if y >= 500 - height:
                y = 500 - height
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x -= vel
            if x <= 0:
                x = 0
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x += vel
            if x >= 750 - width:
                x = 750 - width

        if keys[pygame.K_ESCAPE]:
            run_game = False
            run = False

        # bigger / smaller
        if keys[pygame.K_b]:
            width += 1
            height += 1
            if width > 400:
                width = 400
            if height > 400:
                height = 400
        if keys[pygame.K_v]:
            width -= 1
            height -= 1
            if width < 5:
                width = 5
            if height < 5:
                height = 5

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                run = False

            # if click happens
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                # checks if its in color boxes
                if pos[0] > x_box and pos[0] < x_box + 20 and pos[1] > 10 and pos[1] < 30:
                    color = red
                elif pos[0] > x_box + 25 and pos[0] < x_box + 45 and pos[1] > 10 and pos[1] < 30:
                    color = orange
                elif pos[0] > x_box + 50 and pos[0] < x_box + 70 and pos[1] > 10 and pos[1] < 30:
                    color = yellow
                elif pos[0] > x_box + 75 and pos[0] < x_box + 95 and pos[1] > 10 and pos[1] < 30:
                    color = green
                elif pos[0] > x_box + 100 and pos[0] < x_box + 120 and pos[1] > 10 and pos[1] < 30:
                    color = blue
                elif pos[0] > x_box + 125 and pos[0] < x_box + 145 and pos[1] > 10 and pos[1] < 30:
                    color = purple
                elif pos[0] > x_box + 150 and pos[0] < x_box + 170 and pos[1] > 10 and pos[1] < 30:
                    color = pink
                elif pos[0] > x_box + 175 and pos[0] < x_box + 195 and pos[1] > 10 and pos[1] < 30:
                    color = brown
                elif pos[0] > x_box + 200 and pos[0] < x_box + 220 and pos[1] > 10 and pos[1] < 30:
                    color = grey
                elif pos[0] > x_box + 225 and pos[0] < x_box + 245 and pos[1] > 10 and pos[1] < 30:
                    color = black
                elif pos[0] > x_box - 50 and pos[0] < x_box - 5 and pos[1] > 10 and pos[1] < 30:
                    color = white
                elif pos[0] > x_box + 250 and pos[0] < x_box + 270 and pos[1] > 10 and pos[1] < 30:
                    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                # checks if its on speed arrows
                elif pos[0] > 126 and pos[0] < 142 and pos[1] > 9 and pos[1] < 15:
                        vel += 1
                        if vel >= 40:
                            vel = 40
                elif pos[0] > 126 and pos[0] < 142 and pos[1] > 26 and pos[1] < 32:
                        vel -= 1
                        if vel <= 0:
                            vel = 0

                # checks if its on bigger / smaller buttons
                elif pos[0] > 160 and pos[0] < 210 and pos[1] > 10 and pos[1] < 30:
                    width += 5
                    height += 5
                    if width > 400:
                        width = 400
                    if height > 400:
                        height = 400
                elif pos[0] > 215 and pos[0] < 265 and pos[1] > 10 and pos[1] < 30:
                    width -= 5
                    height -= 5
                    if width < 5:
                        width = 5
                    if height < 5:
                        height = 5

                # checks if its in clear box
                elif pos[0] > 278 and pos[0] < 323 and pos[1] > 10 and pos[1] < 30:
                    pygame.draw.rect(win, white, pygame.Rect(0, 0, 750, 500))
                    saved_rects = []

                # checks if its in save button
                elif pos[0] > 352 and pos[0] < 397 and pos[1] > 2 and pos[1] < 18:

                    # saves current rects
                    saved_rects_string = ''
                    for rect in saved_rects:
                        for i in range(len(rect)):
                            if i < 5:
                                saved_rects_string += str(rect[i]) + ' | '
                            else:
                                saved_rects_string += str(rect[i])
                        saved_rects_string += '\n'
                    draw_file = open('draw_file.txt', 'w')
                    draw_file.write(saved_rects_string)
                    draw_file.close()

                    # loads in saved file
                    new_parts = []
                    new_rect = []
                    file_saved_rects = []
                    saved_file = open('draw_file.txt', 'r+')
                    for line in saved_file:
                        new_rect = []
                        parts = line.strip('\n | ').split(' | ')
                        for part in parts:
                            if part.isnumeric():
                                new_rect.append(int(part))
                            else:
                                numbers = part.strip('()').split(', ')
                                new_numbers = []
                                for number in numbers:
                                    new_number = int(number)
                                    new_numbers.append(new_number)
                                new_rect.append(tuple(new_numbers))
                        file_saved_rects.append(new_rect)
                    saved_file.write('')
                    saved_file.close()

                # checks if its in load save button
                elif pos[0] > 333 and pos[0] < 418 and pos[1] > 22 and pos[1] < 38:
                    for rect in file_saved_rects:
                        saved_rects.append(rect)

        # main cube
        pygame.draw.rect(win, color, pygame.Rect(x, y, width, height))

        # main cube borders
        if color != black:
            pygame.draw.line(win, black, (x, y), (x + width, y), 1)
            pygame.draw.line(win, black, (x, y), (x, y + height), 1)
            pygame.draw.line(win, black, (x, y + height), (x + width, y + height), 1)
            pygame.draw.line(win, black, (x + width, y), (x + width, y + height), 1)
        else:
            pygame.draw.line(win, white, (x, y), (x + width, y), 1)
            pygame.draw.line(win, white, (x, y), (x, y + height), 1)
            pygame.draw.line(win, white, (x, y + height), (x + width, y + height), 1)
            pygame.draw.line(win, white, (x + width, y), (x + width, y + height), 1)

        # draw
        if keys[pygame.K_SPACE]:
            saved_rects.append([x, y, width, height, color])

        # display speed
        vel_text = 'Speed: ' + str(vel)
        vel_text = font_3.render(vel_text, True, black)
        win.blit(vel_text, (13, 5))

        # erase button
        pygame.draw.rect(win, light_grey, pygame.Rect(160, 10, 50, 20))
        pygame.draw.line(win, black, (x_box - 50, 10), (x_box - 50, 30), 1)
        pygame.draw.line(win, black, (x_box - 50, 10), (x_box - 5, 10), 1)
        pygame.draw.line(win, black, (x_box - 5, 10), (x_box - 5, 30), 1)
        pygame.draw.line(win, black, (x_box - 50, 30), (x_box - 5, 30), 1)
        erase_text = font_4.render('Erase', True, black)
        win.blit(erase_text, (x_box - 41, 12))

        # random color button
        random_color_text = font_4.render('?', True, black)
        win.blit(random_color_text, (x_box + 257, 13))

        # bigger / smaller buttons
        pygame.draw.rect(win, light_green, pygame.Rect(160, 10, 50, 20))
        pygame.draw.line(win, black, (160, 10), (210, 10), 1)
        pygame.draw.line(win, black, (210, 10), (210, 30), 1)
        pygame.draw.line(win, black, (160, 30), (210, 30), 1)
        pygame.draw.line(win, black, (160, 10), (160, 30), 1)

        pygame.draw.rect(win, light_green, pygame.Rect(215, 10, 50, 20))
        pygame.draw.line(win, black, (215, 10), (265, 10), 1)
        pygame.draw.line(win, black, (265, 10), (265, 30), 1)
        pygame.draw.line(win, black, (215, 30), (265, 30), 1)
        pygame.draw.line(win, black, (215, 10), (215, 30), 1)

        bigger_text = font_4.render('Bigger', True, black)
        win.blit(bigger_text, (166, 13))
        smaller_text = font_4.render('Smaller', True, black)
        win.blit(smaller_text, (219, 13))

        # clear button
        pygame.draw.rect(win, red, pygame.Rect(278, 10, 45, 20))
        pygame.draw.line(win, black, (278, 10), (323, 10), 1)
        pygame.draw.line(win, black, (278, 10), (278, 30), 1)
        pygame.draw.line(win, black, (278, 30), (323, 30), 1)
        pygame.draw.line(win, black, (323, 10), (323, 30), 1)
        clear_text = font_4.render('CLEAR', True, black)
        win.blit(clear_text, (280, 13))

        # save button
        pygame.draw.rect(win, light_blue, pygame.Rect(352, 2, 45, 16))
        pygame.draw.line(win, black, (352, 2), (397, 2), 1)
        pygame.draw.line(win, black, (352, 2), (352, 18), 1)
        pygame.draw.line(win, black, (352, 18), (397, 18), 1)
        pygame.draw.line(win, black, (397, 2), (397, 18), 1)
        save_text = font_4.render('SAVE', True, black)
        win.blit(save_text, (358, 3))

        # load save button
        pygame.draw.rect(win, light_blue, pygame.Rect(333, 22, 85, 16))
        pygame.draw.line(win, black, (333, 22), (418, 22), 1)
        pygame.draw.line(win, black, (333, 22), (333, 38), 1)
        pygame.draw.line(win, black, (333, 38), (418, 38), 1)
        pygame.draw.line(win, black, (418, 22), (418, 38), 1)
        load_save_text = font_4.render('LOAD SAVE', True, black)
        win.blit(load_save_text, (340, 23))

        # draw color boxes
        pygame.draw.rect(win, red, pygame.Rect(x_box, 10, 20, 20))
        pygame.draw.rect(win, orange, pygame.Rect(x_box + 25, 10, 20, 20))
        pygame.draw.rect(win, yellow, pygame.Rect(x_box + 50, 10, 20, 20))
        pygame.draw.rect(win, green, pygame.Rect(x_box + 75, 10, 20, 20))
        pygame.draw.rect(win, blue, pygame.Rect(x_box + 100, 10, 20, 20))
        pygame.draw.rect(win, purple, pygame.Rect(x_box + 125, 10, 20, 20))
        pygame.draw.rect(win, pink, pygame.Rect(x_box + 150, 10, 20, 20))
        pygame.draw.rect(win, brown, pygame.Rect(x_box + 175, 10, 20, 20))
        pygame.draw.rect(win, grey, pygame.Rect(x_box + 200, 10, 20, 20))
        pygame.draw.rect(win, black, pygame.Rect(x_box + 225, 10, 20, 20))

        # draw color box borders
        i = 0
        while i < 11:
            pygame.draw.line(win, black, (x_box, 10), (x_box + 20, 10), 1)
            pygame.draw.line(win, black, (x_box + 20, 10), (x_box + 20, 30), 1)
            pygame.draw.line(win, black, (x_box, 10), (x_box, 30), 1)
            pygame.draw.line(win, black, (x_box, 30), (x_box + 20, 30), 1)
            x_box += 25
            i += 1
        x_box = 475

        # speed arrows
        pygame.draw.line(win, black, (134, 9), (142, 15), 3)
        pygame.draw.line(win, black, (134, 9), (126, 15), 3)
        pygame.draw.line(win, black, (126, 15), (142, 15), 3)

        pygame.draw.line(win, black, (126, 26), (142, 26), 3)
        pygame.draw.line(win, black, (134, 32), (126, 26), 3)
        pygame.draw.line(win, black, (134, 32), (142, 26), 3)

        # separation line
        pygame.draw.rect(win, black, pygame.Rect(0, 41, 750, 2))

        # update display
        pygame.display.flip()

    return run

def show_help_screen():
    show_help = True
    while show_help:

        # background
        pygame.draw.rect(win, light_blue, pygame.Rect(0, 0, 750, 500))

        # clouds
        for i in range(len(cloud_values)):
            win.blit(cloud, (cloud_values[i][0], cloud_values[i][1]))
            cloud_values[i][0] += 5
            if cloud_values[i][0] > 760:
                cloud_values[i][0] = random.randint(-750, -80)
        pygame.draw.rect(win, black, pygame.Rect(0, 500, 1000, 400))
        pygame.draw.rect(win, black, pygame.Rect(750, 0, 300, 1000))

        # back button
        pygame.draw.rect(win, other_blue, pygame.Rect(150, 375, 450, 75))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            show_help = False

        # checks for exit of help screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if pos[0] > 150 and pos[0] < 600 and pos[1] > 375 and pos[1] < 450:
                    show_help = False

        # help screen instructions
        help_text_1 = 'How to Play'
        help_text_2 = '- Use the buttons on the top of the screen to adjust'
        help_text_3 = '  the settings of your cube, or use these alternate options:'
        help_text_4 = "        - 'V' = Smaller, 'B' = Bigger"
        help_text_5 = "        - '<' = Slower, '>' = Faster"
        help_text_6 = "        - 'BACKSPACE' = Clear Screen"
        help_text_7 = '- Use WASD or the arrow keys to move'
        help_text_8 = '- Hold the SPACE BAR to draw!'
        help_text_9 = '- You can save and load your work by clicking the buttons'
        help_text_10 = '  provided or by pressing TAB.'
        help_text_11 = 'Have fun!'
        help_text_BACK = 'BACK'
        help_text_surface_1 = font_5.render(help_text_1, True, title_blue)
        help_text_surface_2 = font_3.render(help_text_2, True, other_blue)
        help_text_surface_3 = font_3.render(help_text_3, True, other_blue)
        help_text_surface_4 = font_3.render(help_text_4, True, other_blue)
        help_text_surface_5 = font_3.render(help_text_5, True, other_blue)
        help_text_surface_6 = font_3.render(help_text_6, True, other_blue)
        help_text_surface_7 = font_3.render(help_text_7, True, other_blue)
        help_text_surface_8 = font_3.render(help_text_8, True, other_blue)
        help_text_surface_9 = font_3.render(help_text_9, True, other_blue)
        help_text_surface_10 = font_3.render(help_text_10, True, other_blue)
        help_text_surface_11 = font_3.render(help_text_11, True, other_blue)
        help_text_surface_BACK = font_2.render(help_text_BACK, True, white)
        win.blit(help_text_surface_1, (306, 7))
        win.blit(help_text_surface_2, (95, 56))
        win.blit(help_text_surface_3, (95, 86))
        win.blit(help_text_surface_4, (95, 116))
        win.blit(help_text_surface_5, (95, 146))
        win.blit(help_text_surface_6, (95, 176))
        win.blit(help_text_surface_7, (95, 206))
        win.blit(help_text_surface_8, (95, 236))
        win.blit(help_text_surface_9, (95, 266))
        win.blit(help_text_surface_10, (95, 296))
        win.blit(help_text_surface_11, (326, 329))
        win.blit(help_text_surface_BACK, (337, 397))

        # button reaction
        pos = pygame.mouse.get_pos()
        if pos[0] > 150 and pos[0] < 600 and pos[1] > 375 and pos[1] < 450:
            pygame.draw.rect(win, other_blue, pygame.Rect(145, 370, 460, 85))
            win.blit(help_text_surface_BACK, (337, 397))

        # updates display
        pygame.display.flip()

def main():
    run_title = True
    run = True
    while run:

        if run_title:
            run_title, play_game, run, show_help = title_screen()

        elif play_game:
            run = game_play()

        elif show_help:
            show_help_screen()
            run_title = True

    pygame.quit()
    sys.exit()

main()
