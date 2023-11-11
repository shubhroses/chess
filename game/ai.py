import random
from .board import Board

class AI:
    def __init__(self, board):
        self.board = board

    def choose_move(self):
        legal_moves = []

        for row in range(8):
            for col in range(8):
                piece = self.board.board[row][col]
                if piece and piece.color == 'Black':
                    possible_moves = piece.get_legal_moves((row, col), self.board.board)
                    for end_row, end_col in possible_moves:
                        legal_moves.append(((row, col), (end_row, end_col)))

        if legal_moves:
            return random.choice(legal_moves)
        else:
            return None  # No legal moves available


    def make_move(self):
        chosen_move = self.choose_move()
        if chosen_move:
            start_pos, end_pos = chosen_move
            self.board.move_piece(start_pos[0], start_pos[1], end_pos[0], end_pos[1])
