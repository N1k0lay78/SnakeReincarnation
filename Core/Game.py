import pygame as pg
import pygame.time

from Core.Logic.RotatableAnimation import RotatableAnimation
from Core.Logic.TileSet import TileSet
from Core.Logic.load_image import load_image
from Core.Objects.Apple import Apple
from Core.Objects.Base import Base
from Core.Objects.Snake import Snake
from Core.anims import snake_animations
from Core.settings import cell_size


class Game:
    def __init__(self, nickname, screen_size, map_size):
        # time
        self.delta = 0
        self.clock = pygame.time.Clock()
        # nickname
        self.nickname = nickname
        # sizes
        self.screen_size = screen_size
        self.map_size = map_size
        # display
        self.screen = pg.display.set_mode(self.screen_size)
        # default source
        self.tile = Base(self, load_image("Tile"), [0, 0])
        self.snake_anim = RotatableAnimation(TileSet(load_image("Snake4"), (64, 64)), 8, **snake_animations)
        # init game
        self.input = [0, 1]
        self.last_move = [0, 1]
        self.snake = Snake(self, self.snake_anim, [4, 4])
        self.apple = Apple(self, load_image("Apple"))
        self.score = 0

    def restart(self):
        self.input = [0, 1]
        self.last_move = [0, 1]
        self.snake = Snake(self, self.snake_anim, [4, 4])
        self.apple = Apple(self, load_image("Apple"))
        self.score = 0

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            keys = pg.key.get_pressed()
            if keys[pg.K_w] and self.last_move != [0, -1]:
                self.input = [0, 1]
            if keys[pg.K_s] and self.last_move != [0, 1]:
                self.input = [0, -1]
            if keys[pg.K_a] and self.last_move != [1, 0]:
                self.input = [-1, 0]
            if keys[pg.K_d] and self.last_move != [-1, 0]:
                self.input = [1, 0]
            for y in range(self.map_size[1]):
                for x in range(self.map_size[0]):
                    self.tile.set_pos([x * cell_size, y * cell_size])
                    self.tile.draw()
            self.apple.draw()
            self.snake.update()
            self.snake.draw()
            pg.display.update()
            self.delta = self.clock.tick(60)
