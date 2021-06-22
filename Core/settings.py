cell_size = 64
map_size = [10, 10]
shake_move_time = 0.5


def update_map_size(size):
    global map_size
    map_size = size


def get_window_size():
    return [int(map_size[0] * cell_size), int(map_size[1] * cell_size)]
