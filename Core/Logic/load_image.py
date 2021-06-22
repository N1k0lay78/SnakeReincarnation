from pygame.image import load
import os


def load_image(filename):
    return load(f"Source{os.altsep}Image{os.altsep}{filename}.png")