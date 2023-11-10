class Board:
    def __init__(self):
        # 8x8 grid initialized with None
        self.board = [[None for _ in range(8)] for _ in range(8)]