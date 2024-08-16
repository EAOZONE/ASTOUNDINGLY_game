from instructions import *
def start(font, font_instructions):
    # Show the title screen
    pressed = True
    while pressed:
        # Fill the screen with the background color
        SCREEN.fill(DARK_GREY)

        # Create and display the text for the title screen
        name_surface = font.render("Welcome to CUSTOMISABLE!", True, WHITE)
        start_surface = font.render("Press 'SPACE' to start", True, WHITE)
        instruction_surface = font.render("Press '1' for instructions", True, WHITE)
        SCREEN.blit(name_surface, (95, BASE_OFFSET_Y - 70))
        SCREEN.blit(start_surface, (180, BASE_OFFSET_Y))
        SCREEN.blit(instruction_surface, (140, BASE_OFFSET_Y + 70))
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
                if event.key == pygame.K_SPACE:
                    pressed = False
                if event.key == pygame.K_1:
                    instruction()
