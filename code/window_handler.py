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

    def build(self, name, buttons, text):
        if (name not in self.acceptable_window_names):
            raise ValueError(f"{name} is not a listed window!")

        self.windows[name] = Window(self.screen, self.settings)
        self.windows[name].children["buttons"] = buttons
        self.windows[name].children["text"].append(text)
        

    def run(self, name, event, events):
        if (name not in self.acceptable_window_names):
            raise ValueError(f"{name} is not a listed window!")
        pygame.display.set_caption(name)
        return self.windows[name].run(event, events)

    def turn_off(self, name):
        if (name not in self.acceptable_window_names):
            raise ValueError(f"{name} is not a listed window!")
        for button in self.windows[name].children["buttons"]:
            if (not button):
                continue
            button.toggle_visibility()

    def turn_on(self, name):
        self.screen.fill(self.settings["display"]["colors"]["color-white"])
        self.turn_off(name)
