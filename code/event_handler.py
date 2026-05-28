import pygame

class EventHandler:

    def __init__(self, settings, drawer, animation_player):
        self.drawer = drawer
        self.animation_player = animation_player
        # ------------------ Move to Drawer class?
        self.drawing_commands = settings["drawing-commands"]
        self.animation_commands = settings["animation-commands"]
        # ------------------
        self.menu_options = settings["menu-commands"]
        self.menu_options_names = ["play current work", "drawing", "selection"] 

        self.current_menu_state = "main"
        self.mod_keys = settings["mod key references"]
        self.nonmod_keys = settings["nonmod key references"]
        self.command = ""
        self.events = []
        self.running = True
        self.window = self.window_start()

        self.drag_has_begun = False
        self.drag_has_ended = False

    def window_player(self):
        #print("playing current working animation")
        for e in self.events:
            #print(e)
            if (e.type == pygame.TEXTINPUT):
                if (e.text == ' '):
                    #print(e)
                    self.animation_player.play_animation(self.drawer.raw_animations[self.drawer.current_working_name])
                    self.events.remove(e)
    def window_drawer(self):
        #print("in the drawing menu")
        
        for e in self.events:
            if (not self.drag_has_begun): # condition for next dragging iteration
                self.drag_has_ended = False
            if (e.type == pygame.MOUSEBUTTONDOWN and (not self.drag_has_begun)):
                self.drag_has_begun = True
            elif ((e.type == pygame.MOUSEBUTTONUP) and (self.drag_has_begun)):
                self.drag_has_begun = False
                self.drag_has_ended = True

            if (self.drag_has_begun and (not self.drag_has_ended)):
                
                self.drawer.drawing(e)
        #print(f"self.drag_has_begun: {self.drag_has_begun}\nself.drag_has_ended: {self.drag_has_ended}")
        #print(f"\\self.drag_has_begun: {self.drag_has_begun}\nself.drag_has_ended: {self.drag_has_ended}\\")
    def window_3(self):
        print("in the selection menu")
        #TODO: used for selecting what animation to load in
    def window_start(self):
        print("in start menu")
        self.drawer.screen.fill(self.drawer.display_settings["colors"]["color-white"])
        #TODO: ???


    def check_menu_state(self):
        if (self.command in self.menu_options_names):
            self.current_menu_state = self.command
            #self.do_menu()
            self.command = ""

    def do_menu(self):
        #self.window = None
        if (self.current_menu_state == "play current work"):
            self.window = self.window_player()
        if (self.current_menu_state == "drawing"):
            self.window = self.window_drawer()
        if (self.current_menu_state == "selection"):
            self.window = self.window_3()
        if (self.window):
            self.window()

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
        self.command = command.rstrip()
        #print(self.command)
        
        
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
            
            self.check_menu_state()
            self.do_menu()
            
            self.events.remove(e)
        


