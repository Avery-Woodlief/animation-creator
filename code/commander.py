import pygame
import re

class Commander:

    def __init__(self, settings):
        self.command = ""
        self.menu_options_names = ["play current work", "drawing", "selection"] 
        self.menu_states = {"selection" : False, "drawing":False, "play current work": False}
        self.current_menu_state = ""

    def exec_command(self):
        if (self.command in self.menu_options_names):
            self.current_menu_state = self.command
            for name, state in self.menu_states.items():
                if (name != self.current_menu_state):
                    self.menu_states[name] = False
            self.menu_states[self.current_menu_state] = True
        print(self.current_menu_state)
            
