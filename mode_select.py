from variables import *
def mode():
    num_lvls = -1
    num_guesses = 0
    num_lvls_words = ['Choose the number of levels:', 'Press the number on the keyboard corresponding to ', 'the number of levels you want up to 8']
    num_guesses_words = ['Choose the number of guesses per level:', 'Press the number on the keyboard corresponding to', 'the number of guesses you want up to 6']
    SCREEN.fill(DARK_GREY)

    # Asks for and gets number of levels for game
    while num_lvls == -1:
        for j in range(len(num_lvls_words)):
            SCREEN.blit(instruction_font.render(num_lvls_words[j], True, WHITE),
                        (40, 355 + 45 * (j - 1)))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_1:
                    num_lvls = 0
                if event.key == pygame.K_2:
                    num_lvls = 1
                if event.key == pygame.K_3:
                    num_lvls = 2
                if event.key == pygame.K_4:
                    num_lvls = 3
                if event.key == pygame.K_5:
                    num_lvls = 4
                if event.key == pygame.K_6:
                    num_lvls = 5
                if event.key == pygame.K_7:
                    num_lvls = 6
                if event.key == pygame.K_8:
                    num_lvls = 7
    SCREEN.fill(DARK_GREY)

    # Asks for and gets number of guesses per level
    while num_guesses == 0:
        for j in range(len(num_guesses_words)):
            SCREEN.blit(instruction_font.render(num_guesses_words[j], True, WHITE),
                        (40, 355 + 45 * (j - 1)))
        pygame.display.update()

        # Handle keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_1:
                    num_guesses = 1
                if event.key == pygame.K_2:
                    num_guesses = 2
                if event.key == pygame.K_3:
                    num_guesses = 3
                if event.key == pygame.K_4:
                    num_guesses = 4
                if event.key == pygame.K_5:
                    num_guesses = 5
                if event.key == pygame.K_6:
                    num_guesses = 6
    return num_lvls, num_guesses