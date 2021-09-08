import time
from Board import *

# Blocksize, width and height
blockSize = 15
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 900

values = np.random.randint(0, 2, (int(WINDOW_WIDTH / blockSize), int(WINDOW_HEIGHT / blockSize)))

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Cellular Automata")

game = Board(values, WINDOW_WIDTH, WINDOW_HEIGHT, blockSize, screen)

# Game Loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # RGB SCREEN
    #screen.fill(BLACK)
    game.drawGrid()
    pygame.display.update()
    game.update_grid()
    time.sleep(0.0)
