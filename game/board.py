from .pieces import Pawn, Rook, Knight, Bishop, Queen, King

class Board:
    def __init__(self):
        self.board = [
            [Rook('Black'), Knight('Black'), Bishop('Black'), Queen('Black'), King('Black'), Bishop('Black'), Knight('Black'), Rook('Black')],
            [Pawn('Black') for _ in range(8)],
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [Pawn('White') for _ in range(8)],
            [Rook('White'), Knight('White'), Bishop('White'), Queen('White'), King('White'), Bishop('White'), Knight('White'), Rook('White')]
        ]
        self.current_turn = 'White'

    def move_piece(self, start_row, start_col, end_row, end_col):
        selected_piece = self.board[start_row][start_col]

        if selected_piece and selected_piece.color != self.current_turn:
            print(f"It's not {selected_piece.color}'s turn.")
            return False

        # Get all legal moves for the selected piece
        legal_moves = selected_piece.get_legal_moves((start_row, start_col), self.board)

        if legal_moves:
            self.board[start_row][start_col] = None
            self.board[end_row][end_col] = selected_piece

            if hasattr(selected_piece, 'first_move'):
                selected_piece.first_move = False

            self.current_turn = 'White' if self.current_turn == 'Black' else 'Black'
            return True
        else:
            print("Illegal move.")
            return False
