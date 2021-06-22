from pygame import Surface, transform

from Core.Logic.TileSet import TileSet
from Core.Logic.save_image import save_image


class TileSetRotation:
    def __init__(self, tile_set):
        self.tile_set = tile_set
        self.res = Surface((self.tile_set.get_width()*4, self.tile_set.get_height()))
        self.make_rotations()

    def make_rotations(self):
        for i in range(4):
            for y in range(self.tile_set.count_y):
                for x in range(self.tile_set.count_x):
                    self.res.blit(transform.rotate(self.tile_set.get(x, y), 90*i),
                                  [x * self.tile_set.tile_size[0] + i * self.tile_set.get_width(),
                                   y * self.tile_set.tile_size[0]])

    def save(self, filename):
        save_image(self.res, filename)

    def get_tile_set(self):
        return TileSet(self.res, self.tile_set.tile_size)
