class Bitmap:
    def __init__(self, filename) -> None:
        self.filename = filename
        print(f"loading file '{self.filename}' from disk")

    def draw(self):
        print(f'drawing image {self.filename}')


class LazyBitmap:
    def __init__(self, filename) -> None:
        self.filename = filename
        self._bitmap = None
    
    def draw(self):
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)
        print(f'drawing image {self.filename}')

def draw_image(image):
    print('About to draw image')
    image.draw()
    print('Done drawing image')



if __name__ == '__main__':
    # image = Bitmap('Great Bay Area')
    # draw_image(image)

    print('\n------------------ using virtual proxy to do lazy loading ------------------')
    image = LazyBitmap('Great Bay Area')
    draw_image(image)
    draw_image(image) # only loading once