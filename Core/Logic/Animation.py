class Animation:
    def __init__(self, tile_set, **animations):
        self.tile_set = tile_set
        self.step = 0
        self.animations = animations

    def update(self, step):
        self.step = step

    def get(self, name):
        if name in self.animations:
            return self.tile_set.get(*self.animations[name][int(self.step % len(self.animations[name]))])
        print(f"Error: Does not have animation '{name}'!")
