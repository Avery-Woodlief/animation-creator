import pygame
from animation_player import *
from drawer import *

from window import *
from button import *

class WindowHandler:

    def __init__(self, screen, settings, window_names):
        self.screen = screen
        self.settings = settings
        self.acceptable_window_names = window_names
        self.windows = {}

    def build(self, name, children):
        if (name not in self.acceptable_window_names):
            raise ValueError(f"{name} is not a listed window!")

        self.windows[name] = Window(self.screen, self.settings)
        self.windows[name].children = children
        

    def run(self, name, event):
        if (name not in self.acceptable_window_names):
            raise ValueError(f"{name} is not a listed window!")
        pygame.display.set_caption(name)
        self.windows[name].run(event)
