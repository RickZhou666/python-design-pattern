class Square:
    def __init__(self, side=0):
        self.side = side

def calculate_area(rc):
    return rc.width * rc.height

class SquareToRectangleAdapter:
    def __init__(self, square):
        """
            convert square to rectangle, so it can be used in calculate_are
        """
        self.square = square

    @property
    def width(self):
        return self.square.side
    
    @property
    def height(self):
        return self.square.side


if __name__ == '__main__':
    sq = Square(5)
    rc = SquareToRectangleAdapter(sq)
    print(calculate_area(rc))