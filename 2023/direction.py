from enum import Flag, auto

class Direction(Flag):
    UP = auto()
    RIGHT = auto()
    DOWN = auto()
    LEFT = auto()

    def rotate(self, clockwise = True):
        if clockwise:
            if self == Direction.UP:
                return Direction.RIGHT
            elif self == Direction.RIGHT:
                return Direction.DOWN
            elif self == Direction.DOWN:
                return Direction.LEFT
            else:
                return Direction.UP
        else:
            if self == Direction.UP:
                return Direction.LEFT
            elif self == Direction.RIGHT:
                return Direction.UP
            elif self == Direction.DOWN:
                return Direction.RIGHT
            else:
                return Direction.DOWN

    def flip(self):
        if self == Direction.UP:
            return Direction.DOWN
        elif self == Direction.RIGHT:
            return Direction.LEFT
        elif self == Direction.DOWN:
            return Direction.UP
        else:
            return Direction.RIGHT
            
    def move_forward(self, x, y, moves=1):
        if self == Direction.UP:
            return x, y - moves
        elif self == Direction.RIGHT:
            return x + moves, y
        elif self == Direction.DOWN:
            return x, y + moves
        else:
            return x - moves, y

    def in_direction_total(self, direction_total):
        if self in direction_total:
            return True

    def add_to_direction_total(self, direction_total):
        return self | direction_total
    
    @classmethod
    def direction_from_arrow(cls, symbol):
        if symbol == ">":
            return cls.RIGHT
        elif symbol == "<":
            return cls.LEFT
        elif symbol == "v":
            return cls.DOWN