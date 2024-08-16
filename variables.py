# Import necessary libraries
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set the window title
pygame.display.set_caption("CUSTOMISABLE")

# Set the window size
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the frames per second
FPS = 30

# Define some colors
GREY = (100, 100, 100)
DARK_GREY = (20, 20, 20)
WHITE = (255, 255, 255)
RED = (255, 108, 108)
COLOR_INCORRECT = (50, 50, 50)
COLOR_MISPLACED = (255, 193, 0)
COLOR_CORRECT = (0, 185, 6)

# Set up game level variables
lvl_num = 5
instructions_used = False
TEXT_TIMER = 2
NUM_COLS = lvl_num
NUM_ROWS = 6
LETTER_LENGTH = NUM_COLS
NUM_GUESSES = 0
RECT_WIDTH = 50
RECT_HEIGHT = 50
KEY_WIDTH = 50
KEY_HEIGHT = 50

# Set up the alphabet for the keyboard
alphabet = ['QWERTYUIOP','ASDFGHJKL','ZXCVBNM']

# Set up lists to track letters
misplaced_letters = []
correct_letters = []
wrong_letters = []

# Set up pixel distances between rectangles
DX = 10
DY = 10
X_PADDING = 5
Y_PADDING = 5

# Calculate the leftmost and topmost coordinates for the first rectangle
BASE_OFFSET_X = (WIDTH / 2) - ((NUM_COLS / 2) * DX) - ((NUM_COLS / 2) * RECT_WIDTH) + (((NUM_COLS + 1) % 2) * (DX / 2))
BASE_OFFSET_Y = (HEIGHT / 2) - ((NUM_ROWS / 2) * DY) - ((NUM_ROWS / 2) * RECT_HEIGHT) + (((NUM_ROWS + 1) % 2) * (DY / 2))

# Set up font sizes
font = pygame.font.Font(None, 65)
instruction_font = pygame.font.Font(None, 45)
