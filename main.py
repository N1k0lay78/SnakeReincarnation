import pygame as pg
import os
from win32api import GetSystemMetrics

from Core.Game import Game
from Core.Logic.TileSet import TileSet
from Core.Logic.check_object import check_object
from Core.Tools.TileSetRotation import TileSetRotation
from Core.settings import *

# print(os.getlogin(), os.cpu_count())

# default settings
screen_size = get_window_size()
nickname = "Nickname"

# tests
# get size
try:
    print(f"Window size: {GetSystemMetrics(0)} X {GetSystemMetrics(1)}")
    update_map_size([GetSystemMetrics(1) * 0.6 // cell_size, GetSystemMetrics(1) * 0.6 // cell_size])
    screen_size = get_window_size()
except Exception:
    print("Error on get window size")

# get username
try:
    nickname = os.getlogin()
except Exception:
    print("Error on read system nickname")

# PyGame init
try:
    pg.init()
except Exception:
    print("Error on PyGame init")
    pg.quit()
    quit()

# check files
if not check_object("Image", "Apple"):
    print("Error does not have Apple.png")

if not check_object("Image", "Icon"):
    print("Error does not have Icon.png")

if not check_object("Image", "Snake"):
    print("Error does not have Snake.png")

if not check_object("Image", "Tile"):
    print("Error does not have Tile.png")

if not check_object("Image", "Snake4"):
    print("Generating snake animations")
    TileSetRotation(TileSet("Snake", (64, 64))).save("Snake4")

# print settings
print("Settings")
print(f"Nickname: {nickname}")
print(f"window size: {screen_size[0]} X {screen_size[1]}")

game = Game(nickname, screen_size, map_size)
game.run()
