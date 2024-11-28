import pygame
import sys
from level1 import *  # Assuming level1() is defined in another file

pygame.init()

# Define colors
white = (255, 255, 255)
green = (0, 155, 0)
blue = (0, 0, 128)
bg_open = pygame.image.load("background.jpg")  # Ensure this image is in the correct directory

# Set the screen width and height
X = 800
Y = 600
display_surface = pygame.display.set_mode((X, Y))

# Set the pygame window name
pygame.display.set_caption('Space Invaders')

# Create a font object
font = pygame.font.SysFont("comicsansms", 32)

def get_username():
    input_box = pygame.Rect(X // 2 - 250, Y // 2 - 12, 500, 50)  # Increased size for input box
    font = pygame.font.SysFont('comicsans', 30)
    input_label = font.render('Enter your name:', 1, (255, 255, 255))
    username = ''
    active = False
    while True:
        display_surface.blit(bg_open, (0, 0))  #
        #Use the same background image as the rest of the game
        display_surface.blit(input_label, (X // 2 - 100, Y // 2 - 100))  # Display the input label
        pygame.draw.rect(display_surface, (255, 255, 255), input_box, 2)  # Draw the input box
        
        # Render the username inside the input box
        text_surface = font.render(username, True, (255, 255, 255))
        display_surface.blit(text_surface, (input_box.x + 5, input_box.y + (input_box.height - text_surface.get_height()) // 2))  # Center username vertically

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return username  # Return the username when Enter is pressed
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]  # Remove the last character
                    else:
                        username += event.unicode  # Add the new character to the username

def game_intro():
    display_surface.fill(white)
    display_surface.blit(bg_open, (0, 0))

    # Title text
    title_font = pygame.font.SysFont("comicsansms", 64)  # Larger font size for "Space Invaders"
    text = font.render("Space Invaders", True, (255, 255, 255))
    display_surface.blit(text, (280, 155))

    # Instructions text
    text = font.render("Press Space To Start", True, (0, 255, 0))
    display_surface.blit(text, (240, 240))

    text = font.render("Press ESC to Quit", True, (10, 200, 255))
    display_surface.blit(text, (255, 345))

    text = font.render("Press I for Instructions", True, (0, 0, 255))
    display_surface.blit(text, (223, 450))

    pygame.display.update()

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                    username = get_username()  # Ask for username input when spacebar is pressed
                    # Proceed to the first level or a new screen with the username
                    print(f"Welcome, {username}!")
                    start_game(username)  # Start the game with the username

                # Show instructions when 'I' is pressed
                if event.key == pygame.K_i:
                    show_instructions()

                # Quit the game on ESC or quit event
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

# Placeholder function to start the game after username input
def start_game(username):
    # Add logic for starting the game or transitioning to the first level here
    print(f"Game started for {username}!")
    level1(username)# Start the game with the username (calls level1 function)

# Function to display instructions
def show_instructions():
    display_surface.fill(white)
    display_surface.blit(bg_open, (0, 0))

    # Instructions text
    instruction_text1 = font.render("Use arrow keys to move left and right", True, (0, 255, 0))
    display_surface.blit(instruction_text1, (100, 200))

    instruction_text2 = font.render("Use spacebar to shoot", True, (0, 255, 0))
    display_surface.blit(instruction_text2, (100, 270))

    # Back to intro message
    back_text = font.render("Press ESC to go back to the main menu", True, (255, 0, 0))
    display_surface.blit(back_text, (100, 350))

    pygame.display.update()

    instructions_active = True
    while instructions_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions_active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    instructions_active = False
                    game_intro()  # Go back to the intro screen

# Run the game intro
game_intro()
