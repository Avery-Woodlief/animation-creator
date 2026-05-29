import pygame
from window_handler import *

class EventHandler:

    def __init__(self, settings, drawer, animation_player, window_handler):
        self.drawer = drawer
        self.animation_player = animation_player
        self.window_handler = window_handler
        self.window_names = self.window_handler.acceptable_window_names
        # ------------------ Move to Drawer class?
        self.drawing_commands = settings["drawing-commands"]
        self.animation_commands = settings["animation-commands"]
        # ------------------
        self.window_options = settings["window-commands"]
        

        self.current_window = ""
        self.mod_keys = settings["mod key references"]
        self.nonmod_keys = settings["nonmod key references"]
        self.command = "start"
        self.events = []
        self.running = True

        self.drag_has_begun = False
        self.drag_has_ended = False
    


    def check_window_state(self):
        
        if (self.command not in self.window_names):
            #print(f"{self.command} not a window name")
            return
        

        if (self.current_window == self.command):
            #print("staying on same window, do nothing to change windows")
            return

        if (self.command in self.window_names):
            #print(f"In check_window_state...\n\ncommand = {self.command}\ncurrent_window = {self.current_window}")
            #self.current_window = self.command
            try:
                self.window_handler.turn_off(self.current_window)
            except (ValueError):
                _ = None # do nothing at all
            self.window_handler.turn_on(self.command)
            self.current_window = self.command
            self.command = ""
         
        self.do_window()

    def do_window(self):
        #self.window = None
        if (self.current_window not in self.window_names):
            #print(self.current_window)
            #print(self.window_names)
            return
        for e in self.events:
            return_val = self.window_handler.run(self.current_window, e, self.events)
            if (return_val in self.window_names):
                if (return_val != self.current_window):
                    try:
                        self.window_handler.turn_off(self.current_window)
                        self.window_handler.turn_on(return_val)
                        self.current_window = return_val
                    except (ValueError):
                        return
        return
        

    def get_pressed_keys(self, mods, keys):
        
        mods_pressed = [bit for bit, name in self.mod_keys.items() if mods & int(bit)] # LALT, LCTRL, LSHIFT, RALT, RCTRL, RSHIFT, ...
        keys_pressed = [bit for bit, name in self.nonmod_keys.items() if keys[int(bit)]] # l, o, p, z, ...
        menu_key_pressed = [bit for bit, name in self.window_options.items() if keys[int(bit)]] # 1, 2, 3
        self.pressed = mods_pressed + keys_pressed + menu_key_pressed
        command = ""
        for bit in self.pressed:
            if bit in mods_pressed:
                command += self.mod_keys[bit] + " "
            if bit in keys_pressed:
                command += self.nonmod_keys[bit] + " "
            if bit in menu_key_pressed:
                command += self.window_options[bit] + " "
        self.command = command.rstrip()
        #print(self.command)
        if (self.command == "ESC"):
            self.running = False
        
        
    def get_event(self, event):
        
        if (len(event)):
            for e in event:
                #print(e)
                self.events.append(e)
                
        self.process_event()

    def process_event(self):
        for e in self.events:
            if e.type == pygame.QUIT:
                self.running = False
            
            if e.type == pygame.KEYDOWN:
                mods = e.mod
                keys = pygame.key.get_pressed()
                self.get_pressed_keys(mods, keys)
            
            self.check_window_state()
            self.do_window()
            
            try:
                self.events.remove(e)
            except (ValueError): # already removed
                continue
        


