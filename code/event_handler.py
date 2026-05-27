import pygame
from commander import *

class EventHandler:

    def __init__(self, settings):
        self.drawing_commands = settings["drawing-commands"]
        self.animation_commands = settings["animation-commands"]
        self.menu_options = settings["menu-commands"]
        self.mod_keys = settings["mod key references"]
        self.nonmod_keys = settings["nonmod key references"]
        #print(self.mod_keys)
        self.cmd_line = Commander(settings)
        #self.command = ""

    def get_pressed_keys(self, mods, keys):
        mods_pressed = [bit for bit, name in self.mod_keys.items() if mods & int(bit)]
        keys_pressed = [bit for bit, name in self.nonmod_keys.items() if keys[int(bit)]]
        menu_key_pressed = [bit for bit, name in self.menu_options.items() if keys[int(bit)]]
        self.pressed = mods_pressed + keys_pressed + menu_key_pressed
        command = ""
        for bit in self.pressed:
            if bit in mods_pressed:
                command += self.mod_keys[bit] + " "
            if bit in keys_pressed:
                command += self.nonmod_keys[bit] + " "
            if bit in menu_key_pressed:
                command += self.menu_options[bit] + " "
        self.cmd_line.command = command.rstrip()
        #print(self.cmd_line.command)
        self.cmd_line.exec_command()
        

    def change_menu_state(self, key):
        self.current_menu_state = self.menu_options[key]
