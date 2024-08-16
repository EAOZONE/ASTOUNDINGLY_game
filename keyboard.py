from variables import *
def draw_keyboard(x, y, z, flag_lose, flag_win):
    x_1 = []
    y_1 = []
    if flag_lose == False and flag_win == False:

        # Checks if the letters repeat in either its own list or in other lists
        for i in x:
            if i in y:
                y.remove(i)
            if i not in x_1:
                x_1.append(i)
            if i in z:
                z.remove(i)
        for j in y:
            if j not in y_1:
                y_1.append(j)
            if j in z:
                z.remove(j)

        # Draws rectangles for each letter in each row
        for i in range(len(alphabet)):
            for j in range(len(alphabet[i])):
                curr_rect = pygame.Rect(
                    (RECT_WIDTH*j + j*10+ 100 + i*35, 600 + RECT_HEIGHT*i + i*10),
                    (RECT_WIDTH, RECT_HEIGHT))
                if i == 2:
                    curr_rect = pygame.Rect(
                        (RECT_WIDTH * j + j * 10 + 100 + i * 47, 600 + RECT_HEIGHT * i + i * 10),
                        (RECT_WIDTH, RECT_HEIGHT))

                # Draws color on key depending on if it is used in the guess and is correct, misplaced or incorrect
                if alphabet[i][j].lower() in x_1:
                    pygame.draw.rect(SCREEN,COLOR_CORRECT,curr_rect)
                elif alphabet[i][j].lower() in y_1:
                    pygame.draw.rect(SCREEN,COLOR_MISPLACED,curr_rect)
                elif alphabet[i][j].lower()  in z:
                    pygame.draw.rect(SCREEN,COLOR_INCORRECT,curr_rect)
                else:
                    pygame.draw.rect(SCREEN, GREY, curr_rect)

                # Draws the letter in the middle of the square
                SCREEN.blit(font.render(alphabet[i][j], True, WHITE), (curr_rect[0]+7,curr_rect[1]+5))
