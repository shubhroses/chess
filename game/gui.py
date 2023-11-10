import pygame
from .board import Board

class ChessGUI:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Chess Game")
        self.board = Board()
        # Load images and other GUI initializations
    
    def draw_board(self):
        # Draw the 8x8 grid here
        pass

    def run(self):
        # Main loop for the GUI
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.draw_board()
            pygame.display.flip()
        
        pygame.quit()
