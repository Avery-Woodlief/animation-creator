import pygame
from animation_player.animation_player import *
from drawer.drawer import *

from window_package.window import *
from window_package.children.button import *

class WindowHandler:

    def __init__(self, screen, settings, window_names):
        self.screen = screen
        self.settings = settings
        self.screen_settings = self.settings["display"]["screen"]
        self.acceptable_window_names = window_names
        self.windows = {}

    def update_screen(self):
        self.screen = pygame.display.set_mode((self.screen_settings["width"], self.screen_settings["height"]), self.screen_settings["active flag"])
        return


    def refresh_screen(self, event_handler):
        saved = event_handler.current_window
        if (event_handler.current_window != "start"):
            event_handler.command = "start"
        else:
            event_handler.command = "animation player" # just because it's next page on right

        event_handler.check_window_state()
        event_handler.command = saved
        event_handler.check_window_state() # twice because if just once then turns the page off, so need to do a swap
        return
            
    def make_screen_borderless(self, event_handler):
        self.screen_settings["active flag"] = pygame.NOFRAME
        self.update_screen()
        self.refresh_screen(event_handler)
        
        #event_handler.do_window()
        return

    def make_screen_bordered(self, event_handler):
        self.screen_settings["active flag"] = 0
        self.update_screen()
        self.refresh_screen(event_handler)
        return

    def build(self, name, buttons, static_images):
        if (name not in self.acceptable_window_names):
            raise ValueError(f"{name} is not a listed window!")

        self.windows[name] = Window(self.screen, self.settings)
        self.windows[name].children["buttons"] = buttons
        self.windows[name].children["static-images"] = static_images
        

    def run(self, name, event, events):
        self.settings["mouse-settings"]["active cursor"] = pygame.SYSTEM_CURSOR_ARROW
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
        self.screen.fill(self.settings["display"]["screen"]["background color"])
        self.turn_off(name)

