class Piece:
    def __init__(self, color):
        self.color = color

    # Common method for all pieces (e.g., position)


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.first_move = True
    
    def get_legal_moves(self, pos, board):
        # pos is a tuple (row, col)
        # board is the current state of the chess board
        # Return a list of legal moves as (row, col) tuples
        legal_moves = []
        direction = -1 if self.color == "White" else 1

        start_row, start_col = pos

        # Move forward one square
        if self.is_valid_move(board, start_row + direction, start_col):
            legal_moves.append((start_row + direction, start_col))
            # Move forward two squares if it's the pawn's first move
            if self.first_move and self.is_valid_move(board, start_row + 2 * direction, start_col):
                legal_moves.append((start_row + 2 * direction, start_col))
        
        # Capture diagonally
        for offset in [-1, 1]:
            if self.can_capture(board, start_row + direction, start_col + offset):
                legal_moves.append((start_row + direction, start_col + offset))
        
        return legal_moves
    

    def is_valid_move(self, board, row, col):
        # Check if the move is within the board and the target square is empty
        return 0 <= row < 8 and 0 <= col < 8 and board[row][col] == None
    
    def can_capture(self, board, row, col):
        # Check if the move is whithin the board and the target square has an opponent's piece
        return 0 <= row < 8 and 0 <= col < 8 and board[row][col] is not None and board[row][col].color != self.color


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def get_legal_moves(self, pos, board):
        # pos is a tuple (row, col)
        # board is the current state of the chess board
        # Return a list of legal moves as (row, col) tuples
        legal_moves = []
        start_row, start_col = pos

        # Relative positions for L-shaped moves
        move_offsets = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),(1, -2), (1, 2), (2, -1), (2, 1)]

        for offset in move_offsets:
            new_row, new_col = start_row + offset[0], start_col + offset[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                target_square = board[new_row][new_col]
                if target_square is None or target_square.color != self.color:
                    legal_moves.append((new_row, new_col))

        return legal_moves

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def get_legal_moves(self, pos, board):
        # pos is a tuple (row, col)
        # board is the current state of the chess board
        # Return a list of legal moves as (row, col) tuples
        legal_moves = []
        start_row, start_col = pos

        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for direction in directions:
            current_row, current_col = start_row, start_col
            while True:
                current_row += direction[0]
                current_col += direction[1]
                if 0 <= current_row < 8 and 0 <= current_col < 8:
                    target_square = board[current_row][current_col]
                    if target_square is None:
                        legal_moves.append((current_row, current_col))
                    elif target_square.color != self.color:
                        legal_moves.append((current_row, current_col))
                        break
                    else:
                        break
                else:
                    break
        
        return legal_moves



class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def get_legal_moves(self, pos, board):
        # pos is a tuple (row, col)
        # board is the current state of the chess board
        # Return a list of legal moves as (row, col) tuples
        legal_moves = []
        start_row, start_col = pos

        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        for direction in directions:
            current_row, current_col = start_row, start_col
            while True:
                current_row += direction[0]
                current_col += direction[1]
                if 0 <= current_row < 8 and 0 <= current_col < 8:
                    target_square = board[current_row][current_col]
                    if target_square is None:
                        legal_moves.append((current_row, current_col))
                    elif target_square.color != self.color:
                        legal_moves.append((current_row, current_col))
                        break
                    else:
                        break
                else:
                    break
        
        return legal_moves


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def get_legal_moves(self, pos, board):
        # pos is a tuple (row, col)
        # board is the current state of the chess board
        # Return a list of legal moves as (row, col) tuples
        legal_moves = []
        start_row, start_col = pos

        directions = [(-1, 0), (0, -1), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for direction in directions:
            current_row, current_col = start_row, start_col
            while True:
                current_row += direction[0]
                current_col += direction[1]
                if 0 <= current_row < 8 and 0 <= current_col < 8:
                    target_square = board[current_row][current_col]
                    if target_square is None:
                        legal_moves.append((current_row, current_col))
                    elif target_square.color != self.color:
                        legal_moves.append((current_row, current_col))
                        break
                    else:
                        break
                else:
                    break
        
        return legal_moves


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def get_legal_moves(self, pos, board):
        # pos is a tuple (row, col)
        # board is the current state of the chess board
        # Return a list of legal moves as (row, col) tuples
        legal_moves = []
        start_row, start_col = pos

        directions = [(-1, 0), (0, -1), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for direction in directions:
            new_row, new_col = start_row + direction[0], start_col + direction[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                target_square = board[new_row][new_col]
                if target_square is None or target_square.color != self.color:
                    legal_moves.append((new_row, new_col))
        
        return legal_moves
