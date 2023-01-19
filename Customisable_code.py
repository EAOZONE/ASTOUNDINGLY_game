import pygame, sys, random
# Initillizes pygame
pygame.init()
pygame.display.set_caption("CUSTOMISABLE")
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 30

#Sets up variables
GREY = (100, 100, 100)
DARK_GREY = (20, 20, 20)
WHITE = (255, 255, 255)
RED = (255, 108, 108)
COLOR_INCORRECT = (50, 50, 50)
COLOR_MISPLACED = (255, 193, 53)
COLOR_CORRECT = (0, 185, 6)
lvl_num = 5
TEXT_TIMER = 2
NUM_ROWS = 6
NUM_COLS = lvl_num
LETTER_LENGTH = NUM_COLS
NUM_GUESSES = 0
RECT_WIDTH = 50
RECT_HEIGHT = 50
# Pixels between each Rect
DX = 10
DY = 10
X_PADDING = 5
Y_PADDING = 5
# Leftmost topmost coordinate where the first rect will be drawn, should be symmetrical. Accounts for number of rects, pixels between rects and rect sizes.
BASE_OFFSET_X = (WIDTH / 2) - ((NUM_COLS / 2) * DX) - ((NUM_COLS / 2) * RECT_WIDTH) + (((NUM_COLS + 1) % 2) * (DX / 2))
BASE_OFFSET_Y = (HEIGHT / 2) - ((NUM_ROWS / 2) * DY) - ((NUM_ROWS / 2) * RECT_HEIGHT) + (
            ((NUM_ROWS + 1) % 2) * (DY / 2))
def start(font, font_instructions):
    # Shows title screen when called
    SCREEN.fill(DARK_GREY)
    name_surface = font.render("Welcome to CUSTOMISABLE!", True, WHITE)
    start_surface = font.render("Press 'SPACE' to start", True, WHITE)
    instruction_surface = font.render("Press '1' for instructions", True, WHITE)
    SCREEN.blit(name_surface, (95, BASE_OFFSET_Y - 70))
    SCREEN.blit(start_surface, (180, BASE_OFFSET_Y))
    SCREEN.blit(instruction_surface, (140, BASE_OFFSET_Y + 70))
    pressed = True
    pygame.display.update()
    while pressed:
        SCREEN.fill(DARK_GREY)
        name_surface = font.render("Welcome to CUSTOMISABLE!", True, WHITE)
        start_surface = font.render("Press 'SPACE' to start", True, WHITE)
        instruction_surface = font.render("Press '1' for instructions", True, WHITE)
        SCREEN.blit(name_surface, (95, BASE_OFFSET_Y - 70))
        SCREEN.blit(start_surface, (180, BASE_OFFSET_Y))
        SCREEN.blit(instruction_surface, (140, BASE_OFFSET_Y + 70))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    pressed = False
                if event.key == pygame.K_1:
                    instruction(font_instructions)
def instruction(font):
    # Shows instructions when called
    SCREEN.fill(DARK_GREY)
    instructions_1_surface = font.render("Instructions:", True, WHITE)
    instructions_2_surface = font.render("The game consists of 12 levels", True, WHITE)
    instructions_3_surface = font.render("Each level you will be given 6 tries", True, WHITE)
    instructions_4_surface = font.render("to guess the word.", True, WHITE)
    instructions_5_surface = font.render("If the letter is yellow", True, WHITE)
    instructions_6_surface = font.render("It is in the word ", True, WHITE)
    instructions_7_surface = font.render("but is in the wrong spot.", True, WHITE)
    instructions_8_surface = font.render("If the letter is green", True, WHITE)
    instructions_9_surface = font.render("it is in the word and in the correct spot.", True, WHITE)
    instructions_10_surface = font.render("If the word is guessed correctly", True, WHITE)
    instructions_11_surface = font.render("press space to continue on to the", True, WHITE)
    instructions_12_surface = font.render("next level which will have one", True, WHITE)
    instructions_13_surface = font.render("more letter in the correct word", True, WHITE)
    instructions_14_surface = font.render("Press '1' anytime to come back to the instructions", True, WHITE)
    instructions_15_surface = font.render("Press '2' to get a hint", True, WHITE)
    instructions_16_surface = font.render("Press 'Enter' to guess the word", True, WHITE)
    instructions_17_surface = font.render("Press 'Backspace' to delete letters", True, WHITE)
    instructions_18_surface = font.render("Press 'Q' to go back from whence you came", True, WHITE)
    variables = [instructions_1_surface, instructions_2_surface, instructions_3_surface, instructions_4_surface,
                 instructions_5_surface, instructions_6_surface, instructions_7_surface, instructions_8_surface,
                 instructions_9_surface, instructions_10_surface, instructions_11_surface, instructions_12_surface,
                 instructions_13_surface, instructions_14_surface, instructions_15_surface, instructions_16_surface,
                 instructions_17_surface, instructions_18_surface]
    for i in range(len(variables)):
        SCREEN.blit(variables[i], (40, BASE_OFFSET_Y - 180 + 45*(i-1)))
    pressed = True
    pygame.display.update()
    while pressed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_q:
                    pressed = False
font = pygame.font.Font(None, 65)
instruction_font = pygame.font.Font(None, 45)
start(font, instruction_font)
def main(lvl_num):
    # Starts/controls game when called
    global NUM_GUESSES
    NUM_COLS = lvl_num
    LETTER_LENGTH = NUM_COLS
    clock = pygame.time.Clock()
    letter_font = pygame.font.Font(None, 65)
    text = pygame.font.Font(None, 40)
    used_words = []
    curr_word = ""
    word_count = 0
    curr_letter = 0
    rects = []
    flag_win = False
    flag_lose = False
    flag_invalid_word = False
    flag_hint_used = False
    dictionary= [word.replace("\n", "") for word in list(open("dictionary"))]
    flag_not_enough_letters = False
    timer_flag_1 = 0
    timer_flag_2 = 0
    timer_flag_3 = 0
    hint = '.'
    wordlist = []
    for i in dictionary:
        if len(i) == lvl_num:
            wordlist.append(i)
    guess_word = random.choice(wordlist)
    BASE_OFFSET_X = (WIDTH / 2) - ((NUM_COLS / 2) * DX) - ((NUM_COLS / 2) * RECT_WIDTH) + (
                ((NUM_COLS + 1) % 2) * (DX / 2))
    BASE_OFFSET_Y = (HEIGHT / 2) - ((NUM_ROWS / 2) * DY) - ((NUM_ROWS / 2) * RECT_HEIGHT) + (
            ((NUM_ROWS + 1) % 2) * (DY / 2))
    assert (len(guess_word) == LETTER_LENGTH)
    assert (guess_word.islower())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_1:
                    instruction(instruction_font)
                if event.key == pygame.K_2:
                    flag_hint_used = True
            # Option to restart game
            if flag_win or flag_lose:
                if flag_win:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if lvl_num < 12:
                                main(lvl_num + 1)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        main(5)
            else:
                # Upon keypress
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        # Prevents IndexErrors
                        if curr_word:
                            curr_word = curr_word[:-1]
                            curr_letter -= 1
                    elif event.key == pygame.K_RETURN:
                        if len(curr_word) == lvl_num:
                            NUM_GUESSES = NUM_GUESSES + 1
                            if curr_word.lower() in wordlist:
                                word_count += 1
                                used_words.append(curr_word)
                                curr_word = ""
                                curr_letter = 0
                            else:
                                flag_invalid_word = True
                                timer_flag_1 = 0
                        else:
                            flag_not_enough_letters = True
                            timer_flag_2 = 0
                    else:
                        if len(curr_word) < LETTER_LENGTH:
                            if event.unicode.isalpha():
                                curr_word += event.unicode.upper()
                                curr_letter += 1

        SCREEN.fill(DARK_GREY)
        # Draw title and underline
        draw_title(letter_font)
        # Draws base 5x6 grid for letters
        for y in range(NUM_ROWS):
            row_rects = []
            for x in range(NUM_COLS):
                x_pos = BASE_OFFSET_X + (x * DX) + (x * RECT_WIDTH)
                y_pos = BASE_OFFSET_Y + (y * DY) + (y * RECT_HEIGHT)
                curr_rect = pygame.Rect((x_pos, y_pos), (RECT_WIDTH, RECT_HEIGHT))
                pygame.draw.rect(SCREEN, GREY, curr_rect, 2)
                row_rects.append((x_pos, y_pos))
            rects.append(row_rects)

        # Alerts player that word is not in wordlist. Text appears for 2 seconds.
        if flag_invalid_word:
            timer_flag_2 = 0
            flag_not_enough_letters = False
            text_surface = text.render("Not in word list", True, RED)
            # Should be about center aligned. Use of magic numbers, but not serious.
            x_pos = BASE_OFFSET_X + (RECT_WIDTH * (NUM_COLS / 6))
            y_pos = BASE_OFFSET_Y - (DY * 4)
            SCREEN.blit(text_surface, (x_pos, y_pos))
            timer_flag_1 += 1
        if flag_hint_used:
            if timer_flag_3 == 1:
                hint = random.choice(guess_word)
            text_surface = text.render("One letter in the answer is " + str(hint), True, RED)
            # Should be about center aligned. Use of magic numbers, but not serious.
            x_pos = BASE_OFFSET_X
            y_pos = BASE_OFFSET_Y - (DY * 4)
            SCREEN.blit(text_surface, (x_pos, y_pos))
            timer_flag_3 += 1
        if flag_not_enough_letters:
            timer_flag_1 = 0
            flag_invalid_word = False
            text_surface = text.render("Not enough letters", True, RED)
            x_pos = BASE_OFFSET_X + (RECT_WIDTH * (NUM_COLS / 10))
            y_pos = BASE_OFFSET_Y - (DY * 4)
            SCREEN.blit(text_surface, (x_pos, y_pos))
            timer_flag_2 += 1
        if timer_flag_1 == TEXT_TIMER * FPS:
            flag_invalid_word = False
            timer_flag_1 = 0
        if timer_flag_2 == TEXT_TIMER * FPS:
            flag_not_enough_letters = False
            timer_flag_2 = 0
        if timer_flag_3 == TEXT_TIMER * FPS:
            NUM_GUESSES = NUM_GUESSES + 1
            flag_hint_used = False
            timer_flag_3 = 0

        if flag_win:
            if lvl_num < 12:
                text_surface = text.render("Correct! Press 'R' to play again", True, WHITE)
                continue_surface = text.render("Press 'Space' to continue", True, WHITE)
                x_pos = (RECT_WIDTH * (NUM_COLS / 6))
                y_pos = BASE_OFFSET_Y + (DY * 7) + (RECT_HEIGHT * NUM_ROWS)
                SCREEN.blit(text_surface, (x_pos, y_pos))
                SCREEN.blit(continue_surface, (x_pos, y_pos+50))
            else:
                text_surface = text.render("Correct! You finished all 12 levels it took you "+ str(NUM_GUESSES)+ ' guesses', True, WHITE)
                continue_surface = text.render("Press 'R' to play again", True, WHITE)
                x_pos = (RECT_WIDTH * (NUM_COLS / 6))
                y_pos = BASE_OFFSET_Y + (DY * 7) + (RECT_HEIGHT * NUM_ROWS)
                SCREEN.blit(text_surface, (x_pos-90, y_pos))
                SCREEN.blit(continue_surface, (x_pos+140, y_pos + 50))
        if flag_lose:
            if flag_win != True:
                text_surface = text.render("Try again! Press 'R' to play again", True, WHITE)
                word_was_text = text.render(f"The word was {guess_word.upper()}!", True, WHITE )
                x_pos = (RECT_WIDTH * (NUM_COLS / 6))
                y_pos = BASE_OFFSET_Y + (DY * 7) + (RECT_HEIGHT * NUM_ROWS)
                SCREEN.blit(text_surface, (x_pos, y_pos))
                SCREEN.blit(word_was_text, (x_pos, y_pos+50))

        if curr_word:
            for letter_index in range(len(curr_word)):
                word_surface = letter_font.render(curr_word[letter_index], True, WHITE)
                # [0] represents X coord, [1] Y.
                SCREEN.blit(word_surface, (
                rects[word_count][letter_index][0] + X_PADDING, rects[word_count][letter_index][1] + Y_PADDING))

        # Renders letters and rects of words already inputted by player.
        if used_words:
            for word_index in range(len(used_words)):
                remaining_letters = list(guess_word)
                num_correct = 0

                # Used to make sure that letters that appear more than once don't get counted if that letter appears in guess_word only once.
                # EG: guess_word = "proxy", word = "droop", and 'o' appears more than once. The second 'o' in droop does not get counted.
                same_indeces = [i for i, x in enumerate(zip(guess_word, used_words[word_index].lower())) if
                                all(y == x[0] for y in x)]
                # Same indeces - if guessword is "beast" and usedword[word_index] is "toast", same indeces contains the indeces where same letters in the same positions collide, in this case, "a","s","t" - which have indeces of [2,3,4] respectively.
                if same_indeces:
                    for index in range(len(same_indeces)):
                        num_correct += 1
                        remaining_letters[same_indeces[index]] = ""
                        curr_rect = pygame.Rect(
                            (rects[word_index][same_indeces[index]][0], rects[word_index][same_indeces[index]][1]),
                            (RECT_WIDTH, RECT_HEIGHT))
                        pygame.draw.rect(SCREEN, COLOR_CORRECT, curr_rect)
                        past_letter_surface = letter_font.render(used_words[word_index][same_indeces[index]].upper(),
                                                                 True, WHITE)
                        SCREEN.blit(past_letter_surface, (rects[word_index][same_indeces[index]][0] + X_PADDING,
                                                          rects[word_index][same_indeces[index]][1] + Y_PADDING))

                for letter_index in range(LETTER_LENGTH):
                    if letter_index not in same_indeces:
                        curr_rect = pygame.Rect(
                            (rects[word_index][letter_index][0], rects[word_index][letter_index][1]),
                            (RECT_WIDTH, RECT_HEIGHT))
                        cur_past_letter = used_words[word_index][letter_index].lower()
                        past_letter_surface = letter_font.render(cur_past_letter.upper(), True, WHITE)
                        # Incorrect Letters
                        if cur_past_letter not in remaining_letters:
                            pygame.draw.rect(SCREEN, COLOR_INCORRECT, curr_rect)
                        # Letter exists in word, but wrong position.
                        else:
                            pygame.draw.rect(SCREEN, COLOR_MISPLACED, curr_rect)
                            remaining_letters[remaining_letters.index(cur_past_letter)] = ""
                        SCREEN.blit(past_letter_surface, (
                        rects[word_index][letter_index][0] + X_PADDING, rects[word_index][letter_index][1] + Y_PADDING))

                # Win/lose condition
                if num_correct == lvl_num:
                    flag_win = True
                elif len(used_words) == NUM_ROWS:
                    flag_lose = True

        pygame.display.update()
        clock.tick(FPS)

    main(5)
def draw_title(font):
    pygame.draw.line(SCREEN, WHITE, (BASE_OFFSET_X - RECT_WIDTH, BASE_OFFSET_Y - RECT_HEIGHT), (
    BASE_OFFSET_X + (RECT_WIDTH * (NUM_COLS + 1)) + (DX * (NUM_COLS - 1)), BASE_OFFSET_Y - RECT_HEIGHT), width=1)
    title_surface = font.render("CUSTOMISABLE", True, WHITE)
    SCREEN.blit(title_surface, (220, BASE_OFFSET_Y - (RECT_HEIGHT * 2)))

if __name__ == "__main__":
    main(lvl_num)