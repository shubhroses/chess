import random
from .board import Board

class AI:
    def __init__(self, board):
        self.board = board

    def choose_move(self):
        in_check = self.board.is_in_check('Black')
        legal_moves = []

        for row in range(8):
            for col in range(8):
                piece = self.board.board[row][col]
                if piece and piece.color == 'Black':
                    possible_moves = piece.get_legal_moves((row, col), self.board.board)
                    for end_row, end_col in possible_moves:
                        if in_check:
                            # Simulate the move only if in check
                            original_piece = self.board.board[end_row][end_col]
                            self.board.board[row][col] = None
                            self.board.board[end_row][end_col] = piece

                            # Include the move if it resolves the check
                            if not self.board.is_in_check('Black'):
                                legal_moves.append(((row, col), (end_row, end_col)))

                            # Undo the simulated move
                            self.board.board[row][col] = piece
                            self.board.board[end_row][end_col] = original_piece
                        else:
                            # If not in check, include all possible moves
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
