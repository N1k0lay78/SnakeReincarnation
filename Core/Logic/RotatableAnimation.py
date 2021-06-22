from Core.Logic.Animation import Animation


class RotatableAnimation(Animation):
    def __init__(self, tile_set, width, **animations):
        super().__init__(tile_set, **animations)
        self.width = width
        self.rotate = 0

    def set_rotate(self, rotate):
        self.rotate = rotate

    def get(self, name):
        if name in self.animations:
            pos = self.animations[name][int(self.step % len(self.animations[name]))][:]
            pos[0] += self.width * self.rotate
            return self.tile_set.get(*pos)
        print(f"Error: Does not have animation '{name}'!")
