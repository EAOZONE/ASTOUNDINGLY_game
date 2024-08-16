from animate_words import *
def instruction():
    global instructions_used
    # Fill the screen with the background color
    SCREEN.fill(DARK_GREY)

    # Sets each part of the instructions to a different variable
    instructions_1_surface = "Instructions:"
    instructions_2_surface = "The game consists of 12 levels"
    instructions_3_surface = "Each level you will be given 6 tries"
    instructions_4_surface = "to guess the word."
    instructions_5_surface = "If the letter is yellow"
    instructions_6_surface = "It is in the word "
    instructions_7_surface = "but is in the wrong spot."
    instructions_8_surface = "If the letter is green"
    instructions_9_surface = "it is in the word and in the correct spot."
    instructions_10_surface = "If the word is guessed correctly"
    instructions_11_surface = "press space to continue on to the"
    instructions_12_surface = "next level which will have one"
    instructions_13_surface = "more letter in the correct word"
    instructions_14_surface = "Press '1' anytime to come back to the instructions"
    instructions_15_surface = "Press '2' to get a hint"
    instructions_16_surface = "Press 'Enter' to guess the word"
    instructions_17_surface = "Press 'Backspace' to delete letters"
    instructions_18_surface = "Press 'Q' to go back from whence you came"

    # Consolidates all the instruction variables into a single list
    insturctions_words = [instructions_1_surface, instructions_2_surface, instructions_3_surface, instructions_4_surface,
                 instructions_5_surface, instructions_6_surface, instructions_7_surface, instructions_8_surface,
                 instructions_9_surface, instructions_10_surface, instructions_11_surface, instructions_12_surface,
                 instructions_13_surface, instructions_14_surface, instructions_15_surface, instructions_16_surface,
                 instructions_17_surface, instructions_18_surface]

    # Checks to see if the instructions have been called before
    if instructions_used == False:

        # If the instructions have yet to be called it shows the instructions in an animated style
        for i in range(len(insturctions_words)):
            display_text_animation(insturctions_words[i], i )
            SCREEN.fill(DARK_GREY)
        instructions_used = True
    # Else it just shows the instructions
    for j in range(len(insturctions_words)):
        SCREEN.blit(instruction_font.render(insturctions_words[j], True, WHITE), (40, BASE_OFFSET_Y - 180 + 45*(j-1)))
    pressed = True
    pygame.display.update()
    while pressed:
        # Handle keyboard events
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