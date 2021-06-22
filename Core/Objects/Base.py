class Base:
    def __init__(self, game, img, pos):
        self.game = game
        self._img = img
        self._pos = pos

    def set_pos(self, pos):
        self._pos = pos

    def get_pos(self):
        return self._pos

    def update(self):
        pass

    def draw(self):
        self.game.screen.blit(self._img, self._pos)
