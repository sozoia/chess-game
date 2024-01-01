import gui_set

gui_set.init()

# Set up the display
width, height = 700, 700
screen = gui_set.display.set_mode((width, height))
gui_set.display.set_caption('Chessboard')

# Load the chessboard image (replace with your own chessboard image)
# chessboard_image = pygame.image.load('board.jpg')

# Determine the size of each square based on the window dimensions
square_size = min(width // 8, height // 8)

# Main game loop
running = True
while running:
    for event in gui_set.event.get():
        if event.type == gui_set.QUIT:
            running = False

    # Fill the screen with the chessboard pattern:
    for row in range(8):
        for col in range(8):
            # Calculate the position for each square
            x = col * square_size
            y = row * square_size

            # Alternate the color of squares to create a chessboard pattern
            color = (255, 255, 255) if (row + col) % 2 == 0 else (0, 0, 0)

            # Draw the square on the screen
            gui_set.draw.rect(screen, color, (x, y, square_size, square_size))

    # Add other game elements here

    gui_set.display.flip()

gui_set.quit()
