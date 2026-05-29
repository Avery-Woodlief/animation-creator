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
        #self.window_options_names = ["play current work", "drawing", "selection"] 
        

        self.current_window = "selection"
        self.mod_keys = settings["mod key references"]
        self.nonmod_keys = settings["nonmod key references"]
        self.command = ""
        self.events = []
        self.running = True

        self.drag_has_begun = False
        self.drag_has_ended = False

    
    


    def check_window_state(self):
        if (self.command in self.window_names):
            
            self.current_window = self.command
            #self.do_menu()
            self.command = ""

    def do_window(self):
        #self.window = None
        for e in self.events:
            self.window_handler.run(self.current_window, e)
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
        print(self.command)
        try:
            print(self.drawing_commands[self.command])
        except:
            print()
        
        
    def get_event(self, event):
        if (len(event)):
            for e in event:
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
            
            self.events.remove(e)
        


