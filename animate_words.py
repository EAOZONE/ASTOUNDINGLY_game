
from variables import *

def display_text_animation(string, y_var):
    # Display text animation on the screen
    text = ''
    for i in range(len(string)):
        # Fill the screen with the background color
        SCREEN.fill(DARK_GREY)

        # Add the next character to the text and create a text surface
        text += string[i]
        text_surface = instruction_font.render(text, True, WHITE)

        # Set the position of the text surface and display it on the screen
        text_rect = text_surface.get_rect()
        text_rect.midleft = (40, BASE_OFFSET_Y - 165 + 45 * (y_var-1))
        SCREEN.blit(text_surface, text_rect)
        pygame.display.update()

        # Pause for a short period of time
        pygame.time.wait(70)

        # Handle keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
