from Core.Objects.Base import Base
from Core.settings import cell_size, map_size
import random


class Apple(Base):
    def __init__(self, game, img):
        super().__init__(game, img, [0, 0])
        self.change_pos()

    def change_pos(self):
        pos = [random.randrange(map_size[0]) * cell_size, random.randrange(map_size[1]) * cell_size]
        while pos in self.game.snake.body:
            pos = [random.randrange(map_size[0]) * cell_size, random.randrange(map_size[1]) * cell_size]
        self.set_pos(pos)
