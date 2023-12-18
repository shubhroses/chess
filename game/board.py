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
        legal_moves = selected_piece.get_legal_moves((start_row, start_col), self)

        if (end_row, end_col) in legal_moves:
            # If the move is a castling move, move the rook
            if isinstance(selected_piece, King) and abs(start_col - end_col) == 2:
                direction = int((end_col - start_col) / 2)
                rook_col = 0 if direction == -1 else 7
                rook = self.board[start_row][rook_col]
                self.board[start_row][rook_col] = None
                self.board[start_row][start_col + direction] = rook

            self.board[start_row][start_col] = None
            self.board[end_row][end_col] = selected_piece

            # Check if the move puts the king in check
            if self.is_check(selected_piece.color):
                # If the move puts the king in check, undo the move and return False
                self.board[start_row][start_col] = selected_piece
                self.board[end_row][end_col] = None
                print("Cannot move into check.")
                return False

            selected_piece.first_move = False

            self.current_turn = 'White' if self.current_turn == 'Black' else 'Black'
            return True
        else:
            print("Illegal move.")
            return False
    
    def is_check(self, color):
        # Find the king
        king = None
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if isinstance(piece, King) and piece.color == color:
                    king = piece
                    king_pos = (row, col)
                    break
            if king:
                break

        # Check if any of the opponent's pieces can move to the king's position
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.color != color:
                    if king_pos in piece.get_legal_moves((row, col), self):
                        return True

        return False

    def is_square_under_attack(self, row, col, color):
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece and piece.color != color:
                    if (row, col) in piece.get_legal_moves((i, j), self):
                        return True
        return False
