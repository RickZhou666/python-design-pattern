# LSP

class Rectangle:
    # our constructor and attributes
    def __init__(self, width, height) -> None:
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height
    
    def __str__(self) -> str:
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @width.setter
    def height(self, value):
        self._height = value


# this break LSP
# make sure square is a square, whenever width change, heigh should also be changed
class Square(Rectangle):
    def __init__(self, size) -> None:
        Rectangle.__init__(self, size, size)

    # these setter violates LSP 
    # decorator
    @Rectangle.width.setter
    def width(self,  value):
        self._width = self._height = value
    
    @Rectangle.height.setter
    def height(self,  value):
        self._width = self._height = value

# this method only works on rectange BUT NOT any derived class
def use_it(rc): # (2, 3)
    w = rc.width # 2 this breaks lsp
    rc.height = 10
    expected = int(w * 10) # 20                 # 20
    print(f'Expected an area of {expected}, get {rc.area}')


rc = Rectangle(2,3)
use_it(rc)

sq = Square(5)
use_it(sq)