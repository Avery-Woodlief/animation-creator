import pygame


'''
#x, y = pygame.mouse.get_pos()
#pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
'''


class Drawer:

    def __init__(self, settings, screen):
        self.screen = screen
        self.display_settings = settings["display"]
        self.fonts = self.display_settings["fonts"]
        self.font_sizes = self.display_settings["font-sizes"]
        self.color_settings = self.display_settings["colors"]
        self.draw_settings = settings["drawing"]

        self.raw_animations = {}
        self.formatted_animations = {}
        self.names = []
        self.current_working_name = ""
        
        # TODO: allow more shape options

    def create_animation(self, name):
        '''
        initializes the needed lists for the animation that is about to begun being worked on.
        '''
        self.names.append(name)
        self.raw_animations[name] = []
        self.formatted_animations[name] = []

    def select_animation(self, name):
        self.current_working_name = name

    def init_animation(self, name):
        '''
        Can only being working on animation was this is called
        '''
        self.create_animation(name)
        self.select_animation(name)

    def draw_already_existing_points(self):
        for point in self.raw_animations[self.current_working_name]:
            pygame.draw.circle(self.screen, (0, 0, 255), point, 10)

    def drawing(self, event):
        '''
        Uses event variable to draw what is being worked on in real time
        '''
        if (self.draw_settings["continuous - static"] in [False, True]):
            continuous = self.draw_settings["continuous - static"]
        else:
            raise ValueError("continuous in config not set properly")
        
        
        #self.screen.fill(self.display_settings["colors"]["color-white"])
        if (self.draw_settings["connect points - static"]):
            if (len(self.raw_animations[self.current_working_name]) >= 2):
                pygame.draw.lines(self.screen, (0, 0, 255), False, self.raw_animations[self.current_working_name], 10)
        
            
            
        try:
            pygame.draw.circle(self.screen, (255, 0, 0), event.pos, 2)
            self.raw_animations[self.current_working_name].append(event.pos)
        except (AttributeError):
            return # grabbed bad event
                    
        if (not continuous):
            # removes duplicate positions but preserves order
            self.raw_animations[self.current_working_name] = list(dict.fromkeys(self.raw_animations[self.current_working_name]))
            
