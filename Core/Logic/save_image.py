from pygame.image import save
import os


def save_image(surface, filename):
    save(surface, f"Source{os.altsep}Image{os.altsep}{filename}.png")
