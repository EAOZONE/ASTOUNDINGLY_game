from start import *
def draw_title(font):
    # Draws title and line underneath
    pygame.draw.line(SCREEN, WHITE, (BASE_OFFSET_X - RECT_WIDTH, BASE_OFFSET_Y - RECT_HEIGHT), (
    BASE_OFFSET_X + (RECT_WIDTH * (NUM_COLS + 1)) + (DX * (NUM_COLS - 1)), BASE_OFFSET_Y - RECT_HEIGHT), width=1)
    title_surface = font.render("CUSTOMISABLE", True, WHITE)
    SCREEN.blit(title_surface, (220, BASE_OFFSET_Y - (RECT_HEIGHT * 2)))