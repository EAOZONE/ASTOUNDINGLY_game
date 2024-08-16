from main import *
# Main function to run the game by first showing the start icon than asking for num_lvls and guesses
# Finally plays real game
start(font, instruction_font)
num_lvls, guesses = mode()
main(lvl_num, num_lvls, guesses)