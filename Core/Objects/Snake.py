from Core.Objects.Base import Base
from Core.settings import shake_move_time, cell_size


class Snake(Base):
    def __init__(self, game, anim, pos):
        super().__init__(game, None, [pos[0] * cell_size, pos[1] * cell_size])
        self.animation = anim
        self.time = 0
        self.body = [[self._pos[0], self._pos[1] + cell_size], self._pos]

    def update(self):
        self.time += self.game.delta / 1000
        if self.time > shake_move_time:
            self.time = 0
            self.game.last_move = self.game.input

            if self.game.input == [0, 1]:
                self.set_pos([self._pos[0], self._pos[1] - cell_size])
            if self.game.input == [0, -1]:
                self.set_pos([self._pos[0], self._pos[1] + cell_size])
            if self.game.input == [1, 0]:
                self.set_pos([self._pos[0] + cell_size, self._pos[1]])
            if self.game.input == [-1, 0]:
                self.set_pos([self._pos[0] - cell_size, self._pos[1]])

            self.body.append(self._pos)
            if self._pos != self.game.apple.get_pos():
                self.body.pop(0)
            else:
                self.game.apple.change_pos()
                self.game.score += 10
            if not self.check_pos():
                self.game.restart()
        self.animation.update(self.time // (shake_move_time / 4))

    def check_pos(self):
        if self._pos in self.body[:-1]:
            return False
        elif self._pos[0] < 0 or self._pos[0] > self.game.screen_size[0]:
            return False
        elif self._pos[1] < 0 or self._pos[1] > self.game.screen_size[1]:
            return False
        return True

    def get_direction_back(self, num):
        direction = [0, 0]
        if self.body[num][0] < self.body[num-1][0]:
            direction[0] = -1
        elif self.body[num][0] > self.body[num-1][0]:
            direction[0] = 1
        if self.body[num][1] < self.body[num-1][1]:
            direction[1] = 1
        elif self.body[num][1] > self.body[num-1][1]:
            direction[1] = -1
        return direction

    def get_direction_top(self, num):
        direction = [0, 0]
        if self.body[num][0] < self.body[num+1][0]:
            direction[0] = -1
        elif self.body[num][0] > self.body[num+1][0]:
            direction[0] = 1
        if self.body[num][1] < self.body[num+1][1]:
            direction[1] = 1
        elif self.body[num][1] > self.body[num+1][1]:
            direction[1] = -1
        return direction

    def get_direction(self, num):
        dir_1 = self.get_direction_back(num)
        dir_2 = self.get_direction_top(num)
        head_direction = [0, 1]
        if dir_2 == [-1, 0]:
            self.animation.set_rotate(3)
            head_direction[0] = dir_1[1]
            head_direction[1] = dir_1[0]
        elif dir_2 == [1, 0]:
            self.animation.set_rotate(1)
            head_direction[0] = -dir_1[1]
            head_direction[1] = -dir_1[0]
        elif dir_2 == [0, 1]:
            self.animation.set_rotate(2)
            head_direction[0] = dir_1[0]
            head_direction[1] = -dir_1[1]
        elif dir_2 == [0, -1]:
            self.animation.set_rotate(0)
            head_direction[0] = -dir_1[0]
            head_direction[1] = dir_1[1]
        return head_direction

    def draw(self):
        if len(self.body) == 2:
            direction = self.get_direction_back(-1)
            if direction == [-1, 0]:
                self.animation.set_rotate(1)
            elif direction == [1, 0]:
                self.animation.set_rotate(3)
            elif direction == [0, 1]:
                self.animation.set_rotate(0)
            elif direction == [0, -1]:
                self.animation.set_rotate(2)
            self.game.screen.blit(self.animation.get("small_top"), self.body[1])
            self.game.screen.blit(self.animation.get("small_end"), self.body[0])
        else:
            direction = self.get_direction_back(-1)
            head_direction = [0, 0]
            if direction == [-1, 0]:
                self.animation.set_rotate(1)
                head_direction[1] = -self.game.input[0]
                head_direction[0] = self.game.input[1]
            elif direction == [1, 0]:
                self.animation.set_rotate(3)
                head_direction[1] = self.game.input[0]
                head_direction[0] = -self.game.input[1]
            elif direction == [0, 1]:
                self.animation.set_rotate(0)
                head_direction = self.game.input
            elif direction == [0, -1]:
                self.animation.set_rotate(2)
                head_direction[1] = -self.game.input[1]
                head_direction[0] = -self.game.input[0]
            if head_direction == [0, 1]:
                self.game.screen.blit(self.animation.get("head_top"), self.body[-1])
            if head_direction == [1, 0]:
                self.game.screen.blit(self.animation.get("head_right"), self.body[-1])
            if head_direction == [-1, 0]:
                self.game.screen.blit(self.animation.get("head_left"), self.body[-1])
            throat_dir = self.get_direction(-2)
            if len(self.body) == 3:
                if throat_dir == [0, 1]:
                    self.game.screen.blit(self.animation.get("throat_small_forward"), self.body[-2])
                if throat_dir == [1, 0]:
                    self.game.screen.blit(self.animation.get("throat_small_right"), self.body[-2])
                if throat_dir == [-1, 0]:
                    self.game.screen.blit(self.animation.get("throat_small_left"), self.body[-2])
            else:
                if throat_dir == [0, 1]:
                    self.game.screen.blit(self.animation.get("throat_forward"), self.body[-2])
                if throat_dir == [1, 0]:
                    self.game.screen.blit(self.animation.get("throat_right"), self.body[-2])
                if throat_dir == [-1, 0]:
                    self.game.screen.blit(self.animation.get("throat_left"), self.body[-2])
                for i in range(2, len(self.body) - 2):
                    direction = self.get_direction(i)
                    if direction == [0, 1]:
                        self.game.screen.blit(self.animation.get("body_forward"), self.body[i])
                    if direction == [1, 0]:
                        self.game.screen.blit(self.animation.get("body_right"), self.body[i])
                    if direction == [-1, 0]:
                        self.game.screen.blit(self.animation.get("body_left"), self.body[i])
                direction = self.get_direction(1)
                if direction == [0, 1]:
                    self.game.screen.blit(self.animation.get("tail_start_forward"), self.body[1])
                if direction == [1, 0]:
                    self.game.screen.blit(self.animation.get("tail_start_right"), self.body[1])
                if direction == [-1, 0]:
                    self.game.screen.blit(self.animation.get("tail_start_left"), self.body[1])
            direction = self.get_direction_top(0)
            if direction == [0, 1]:
                self.animation.set_rotate(2)
            elif direction == [0, -1]:
                self.animation.set_rotate(0)
            elif direction == [1, 0]:
                self.animation.set_rotate(1)
            elif direction == [-1, 0]:
                self.animation.set_rotate(3)
            self.game.screen.blit(self.animation.get("tail_end_forward"), self.body[0])

"""
        if len(self.body) == 1:
            self.game.screen.blit(self.animation.get("small"), self.body[0])
        elif len(self.body) == 2:
            self.game.screen.blit(self.animation.get("small_end"), self.body[0])
            self.game.screen.blit(self.animation.get("small_head"), self.body[1])
        elif len(self.body) == 3:
            self.game.screen.blit(self.animation.get("end_1"), self.body[0])
            self.game.screen.blit(self.animation.get("head_2"), self.body[1])
            self.game.screen.blit(self.animation.get("head_1"), self.body[2])
        elif len(self.body) == 4:
            self.game.screen.blit(self.animation.get("end_1"), self.body[0])
            self.game.screen.blit(self.animation.get("end_2"), self.body[1])
            self.game.screen.blit(self.animation.get("head_2"), self.body[-2])
            self.game.screen.blit(self.animation.get("head_1"), self.body[-1])
        else:
            self.game.screen.blit(self.animation.get("end_1"), self.body[0])
            self.game.screen.blit(self.animation.get("end_2"), self.body[1])
            for pos in self.body[2:-2]:
                self.game.screen.blit(self.animation.get("body_straight"), pos)
            self.game.screen.blit(self.animation.get("head_2"), self.body[-2])
            self.game.screen.blit(self.animation.get("head_1"), self.body[-1])
        """
