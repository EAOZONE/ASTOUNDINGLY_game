from title import *
from keyboard import *
from mode_select import *
def main(lvl_num, num_lvls, guesses):
    # Starts/controls game when called
    global NUM_GUESSES
    NUM_ROWS = guesses
    NUM_COLS = lvl_num
    LETTER_LENGTH = NUM_COLS
    clock = pygame.time.Clock()
    letter_font = pygame.font.Font(None, 65)
    same_indeces = []
    other_list = []
    text = pygame.font.Font(None, 40)
    used_words = []
    correct_letters = []
    misplaced_letters = []
    wrong_letters = []
    curr_word = ""
    word_count = 0
    curr_letter = 0
    letters_removed = []
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
    # Creates viable wordlist
    for i in dictionary:
        if len(i) == lvl_num:
            wordlist.append(i)
    #Chooses correct word
    guess_word = random.choice(wordlist)
    BASE_OFFSET_X = (WIDTH / 2) - ((NUM_COLS / 2) * DX) - ((NUM_COLS / 2) * RECT_WIDTH) + (
                ((NUM_COLS + 1) % 2) * (DX / 2))
    BASE_OFFSET_Y = (HEIGHT / 2) - ((NUM_ROWS / 2) * DY) - ((NUM_ROWS / 2) * RECT_HEIGHT) + (
            ((NUM_ROWS + 1) % 2) * (DY / 2))
    assert (len(guess_word) == LETTER_LENGTH)
    assert (guess_word.islower())

    while True:
    #Starts level
        # Gets keyboard input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_1:
                    instruction()
                if event.key == pygame.K_2:
                    flag_hint_used = True
            # Option to restart game
            if flag_win or flag_lose:
                if flag_win:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if lvl_num < 5+num_lvls:
                                main(lvl_num + 1, num_lvls, guesses)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        num_lvls, guesses = mode()
                        main(5, num_lvls, guesses)
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
                            if curr_word.lower() in wordlist:
                                NUM_GUESSES = NUM_GUESSES + 1
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
        # Gives player hint
        if flag_hint_used:
            if timer_flag_3 == 1:
                k = list(guess_word)
                for j in correct_letters:
                    if j in k:
                        k.remove(j)
                for l in misplaced_letters:
                    if l in k:
                        k.remove(l)
                for i in letters_removed:
                    if i in k:
                        k.remove(i)
                if len(k) != 0:
                    hint = random.choice(k)
                    letters_removed.append(hint)
                    k.remove(hint)
                    for i in same_indeces:
                        other_list.append(guess_word[i])
                        if len(k) != 0:
                            if guess_word[i] in k:
                                k.remove(guess_word[i])
            text_surface = text.render("One letter in the answer is " + str(hint).upper(), True, RED)
            misplaced_letters.append(hint)
            # Should be about center aligned. Use of magic numbers, but not serious.
            x_pos = BASE_OFFSET_X - 40
            y_pos = BASE_OFFSET_Y - (DY * 4)
            SCREEN.blit(text_surface, (x_pos, y_pos))
            timer_flag_3 += 1
        # Alerts player that word is not long enough
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
        #Checks if game is over
        if flag_win:
            SCREEN.fill(DARK_GREY)
            if lvl_num < 5+num_lvls:
                text_surface = text.render("Correct! Press 'R' to play again", True, WHITE)
                continue_surface = text.render("Press 'Space' to continue", True, WHITE)
                x_pos = (RECT_WIDTH * (NUM_COLS / 6))
                y_pos = BASE_OFFSET_Y + (DY * 7) + (RECT_HEIGHT * NUM_ROWS)
                SCREEN.blit(text_surface, (x_pos, y_pos))
                SCREEN.blit(continue_surface, (x_pos, y_pos+50))
            else:
                text_surface = text.render("Correct! You finished all "+str(num_lvls+1)+ " levels it took you "+ str(NUM_GUESSES)+ ' guesses', True, WHITE)
                continue_surface = text.render("Press 'R' to play again", True, WHITE)
                x_pos = (40)
                y_pos = BASE_OFFSET_Y + (DY * 7) + (RECT_HEIGHT * NUM_ROWS)
                SCREEN.blit(text_surface, (x_pos, y_pos))
                SCREEN.blit(continue_surface, (x_pos+230, y_pos + 50))
        if flag_lose:
            if flag_win != True:
                SCREEN.fill(DARK_GREY)
                text_surface = text.render("Try again! Press 'R' to play again", True, WHITE)
                word_was_text = text.render(f"The word was {guess_word.upper()}!", True, WHITE )
                x_pos = (RECT_WIDTH * (NUM_COLS / 6))
                y_pos = BASE_OFFSET_Y + (DY * 7) + (RECT_HEIGHT * NUM_ROWS)
                SCREEN.blit(text_surface, (x_pos, y_pos))
                SCREEN.blit(word_was_text, (x_pos, y_pos+50))
        # Creates word entered
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
                    for i in same_indeces:
                        if guess_word[i] not in other_list:
                            other_list.append(guess_word[i])
                            correct_letters.append(guess_word[i])
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
                            wrong_letters.append(cur_past_letter)
                        # Letter exists in word, but wrong position.
                        else:
                            pygame.draw.rect(SCREEN, COLOR_MISPLACED, curr_rect)
                            misplaced_letters.append(cur_past_letter)
                            remaining_letters[remaining_letters.index(cur_past_letter)] = ""
                        SCREEN.blit(past_letter_surface, (
                        rects[word_index][letter_index][0] + X_PADDING, rects[word_index][letter_index][1] + Y_PADDING))

                # Win/lose condition
                if num_correct == lvl_num:
                    flag_win = True
                elif len(used_words) == NUM_ROWS:
                    flag_lose = True
        draw_keyboard(correct_letters, misplaced_letters, wrong_letters, flag_lose,flag_win)
        pygame.display.update()
        clock.tick(FPS)


    main(5, num_lvls, guesses)