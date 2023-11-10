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
        self.captured_pieces = {'White': [], 'Black': []}
        self.current_turn = 'White'
    
    
    def change_turn(self):
        self.current_turn = 'Black' if self.current_turn == 'White' else 'White'


    def is_in_check(self, color):
        # Find the king's position
        king_pos = None
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and isinstance(piece, King) and piece.color == color:
                    king_pos = (row, col)
                    break

        # Check if any opponent's piece can attack the king
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.color != color:
                    if king_pos in piece.get_legal_moves((row, col), self.board):
                        return True  # King is in check

        return False  # King is not in check
    

    def is_checkmate(self, color):
        if not self.is_in_check(color):
            return False  # Not checkmate if the king is not in check

        # Check if any move can get the king out of check
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.color == color:
                    original_pos = (row, col)
                    original_piece = self.board[row][col]
                    for move in piece.get_legal_moves(original_pos, self.board):
                        # Simulate each move and check if the king is still in check
                        self.board[row][col] = None
                        self.board[move[0]][move[1]] = piece
                        if not self.is_in_check(color):
                            # Undo the move
                            self.board[row][col] = original_piece
                            self.board[move[0]][move[1]] = None
                            return False  # Found a move to escape check, not checkmate
                        # Undo the move
                        self.board[row][col] = original_piece
                        self.board[move[0]][move[1]] = None

        return True  # No moves left to escape check, checkmate
    

    def move_piece(self, start_row, start_col, end_row, end_col):
        selected_piece = self.board[start_row][start_col]
        target_piece = self.board[end_row][end_col]

        if selected_piece and selected_piece.color != self.current_turn:
            print(f"It's not {selected_piece.color}'s turn.")
            return False

        # Check if the move is legal
        if selected_piece and (end_row, end_col) in selected_piece.get_legal_moves((start_row, start_col), self.board):
            # Simulate the move
            self.board[start_row][start_col] = None
            self.board[end_row][end_col] = selected_piece

            # Check if the move puts or leaves the own king in check
            if self.is_in_check(selected_piece.color):
                # Undo the move and abort
                self.board[start_row][start_col] = selected_piece
                self.board[end_row][end_col] = target_piece
                print("Move not allowed: King would be in check.")
                return False

            # Handle capture
            if target_piece:
                self.captured_pieces[target_piece.color].append(target_piece)

            # Update 'first_move' attribute for pawns, if applicable
            if hasattr(selected_piece, 'first_move'):
                selected_piece.first_move = False

            # Change turns
            self.current_turn = 'White' if self.current_turn == 'Black' else 'Black'

            # Check for check or checkmate conditions for the opponent
            opponent_color = 'White' if selected_piece.color == 'Black' else 'Black'
            if self.is_checkmate(opponent_color):
                print(f"{selected_piece.color} wins by checkmate!")
            elif self.is_in_check(opponent_color):
                print(f"{opponent_color} is in check!")

            return True
        else:
            print("Illegal move.")
            return False
