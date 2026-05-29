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

    def build(self, name, buttons, static_images):
        if (name not in self.acceptable_window_names):
            raise ValueError(f"{name} is not a listed window!")

        self.windows[name] = Window(self.screen, self.settings)
        self.windows[name].children["buttons"] = buttons
        self.windows[name].children["static-images"] = static_images
        

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
        for image in self.windows[name].children["static-images"]:
            if (not image):
                continue
            image.toggle_visibility()
            #print(image.img_path)

    def turn_on(self, name):
        #self.screen.fill(self.settings["display"]["colors"]["color-white"])
        self.screen.fill((150, 150, 150))
        self.turn_off(name)

