from pygame import Rect

from Core.Logic.load_image import load_image


class TileSet:
    def __init__(self, img, tile_size):
        if type(img) != str:
            self.tile_set = img
        else:
            self.tile_set = load_image(img)
        self.tile_size = tile_size
        self.count_x = int(self.tile_set.get_width() / tile_size[0])
        self.count_y = int(self.tile_set.get_height() / tile_size[1])

    def get_width(self):
        return self.tile_set.get_width()

    def get_height(self):
        return self.tile_set.get_height()

    def get(self, x, y):
        return self.tile_set.subsurface(Rect(x * self.tile_size[0], y * self.tile_size[0], *self.tile_size))
