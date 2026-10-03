from chess_engine import Direction


class Piece:
    def __init__(
            self,
            color,
            position,
            has_moved=False
            ):
        self.color = color
        self.position = position
        self.has_moved = has_moved

class King(Piece):
    symbol = 'K'
    movement = (
        Direction.N, Direction.NE, Direction.E, Direction.SE,
        Direction.S, Direction.SW, Direction.W, Direction.NW
    )
    range_of_motion = 1

class Queen(Piece):
    symbol = 'Q'
    movement = (
        Direction.N, Direction.NE, Direction.E, Direction.SE,
        Direction.S, Direction.SW, Direction.W, Direction.NW
    )
    range_of_motion = 7

class Bishop(Piece):
    symbol = 'B'
    movement = (
        Direction.NE, Direction.SE, Direction.SW, Direction.NW
    )
    range_of_motion = 7

class Knight(Piece):
    symbol = 'N'
    movement = (
        (2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)
    )
    range_of_motion = 1

class Rook(Piece):
    symbol = 'R'
    movement = (
        Direction.N, Direction.E, Direction.S, Direction.W
    )
    range_of_motion = 7

class Pawn(Piece):
    symbol = ''
    range_of_motion = 1

    def forward(self):
        return Direction.N if self.color == 'White' else Direction.S

    def capture_direction(self):
        return (
            (Direction.NE, Direction.NW)
            if self.color == 'White' else
            (Direction.SE, Direction.SW)
        )

