import pygame
from .board import Board
from .ai import AI


class ChessGUI:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Chess Game")
        self.board = Board()

        # Colors and Fonts
        self.light_square = (240, 217, 181)
        self.dark_square = (181, 136, 99)
        self.selected_square_highlight_color = (255, 255, 0)
        self.incorrect_turn_highlight_color = (255, 0, 0)
        self.incorrect_turn_selected = False

        self.font = pygame.font.SysFont("Arial", 32)

        # Load Images
        self.piece_images = self.load_images()

        # Game State Variables
        self.selected_piece = None
        self.selected_row = None
        self.selected_col = None
        self.game_over = False

        self.ai = AI(self.board)

        self.clock = pygame.time.Clock()

    def load_images(self):
        # Load all the images here
        images = {}

        # Assume piece names are like "WPawn.png", "BPawn.png", etc.
        pieces = ["Pawn", "Knight", "Bishop", "Rook", "Queen", "King"]

        for piece in pieces:
            for color in ["W", "B"]:
                images[color + piece] = pygame.transform.scale(
                    pygame.image.load(f"assets/images/{color}{piece}.png"), (50, 50)
                )  # Scale images to fit your grid

        return images

    def draw_board(self):
        square_size = 50
        for row in range(8):
            for col in range(8):
                color = self.light_square if (row + col) % 2 == 0 else self.dark_square
                pygame.draw.rect(
                    self.screen,
                    color,
                    (col * square_size, row * square_size, square_size, square_size),
                )

                if self.selected_piece and (row, col) == (self.selected_row, self.selected_col):
                    highlight_color = self.selected_square_highlight_color
                    if self.selected_piece.color != self.board.current_turn:
                        highlight_color = self.incorrect_turn_highlight_color
                    
                    pygame.draw.rect(
                        self.screen,
                        highlight_color,
                        (col * square_size, row * square_size, square_size, square_size),
                        5  # Border thickness
                    )

    
    def draw_pieces(self):
        square_size = 50
        for row in range(8):
            for col in range(8):
                piece = self.board.board[row][col]  # Get the piece object at this position
                if piece:
                    # Construct the key for the piece_images dictionary
                    piece_image_key = piece.color[0] + type(piece).__name__
                    # Draw the piece
                    self.screen.blit(self.piece_images[piece_image_key], (col * square_size, row * square_size))

    
    def draw(self):
        self.draw_board()
        self.draw_pieces()
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            # AI's turn to move
            if self.board.current_turn == "Black" and not self.game_over:
                print("AI's turn")
                self.ai.make_move()
                print("AI moved")
                self.board.current_turn = "White"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and self.board.current_turn == "White":
                    self.handle_mouse_click(event)

            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


    def handle_mouse_click(self, event):
        if event.button == 1: # Left mouse click
            x, y = event.pos
            row, col = y // 50, x // 50
            self.select_square(row, col)
    

    def select_square(self, row, col):
        clicked_piece = self.board.board[row][col]

        if clicked_piece and clicked_piece.color == self.board.current_turn:
            # If a piece of the current turn's color is clicked, select it
            self.selected_piece = clicked_piece
            self.selected_row, self.selected_col = row, col
            self.incorrect_turn_selected = False
        elif self.selected_piece:
            # If a piece is already selected and the clicked square is different,
            # attempt to move the piece
            if (row, col) in self.selected_piece.get_legal_moves((self.selected_row, self.selected_col), self.board.board):
                self.board.move_piece(self.selected_row, self.selected_col, row, col)
            # Deselect after attempting a move
            self.selected_piece = None
            self.selected_row, self.selected_col = None, None
            self.incorrect_turn_selected = False
        else:
            # If the clicked piece is of the opposite color, mark it as an incorrect turn selection
            self.incorrect_turn_selected = clicked_piece is not None
