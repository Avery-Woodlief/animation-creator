import pygame

'''
def drawing(settings, assigned_points, event, continuous):

    if (continuous):
        mouse = pygame.mouse.get_pressed()
    screen.fill(settings["screen"]["bg-color"])
    for point in assigned_points:
        pygame.draw.circle(screen, (0, 0, 255), point, 10)
        #x, y = point
        #pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
    if (continuous):
        if (mouse[0]):
            #x, y = pygame.mouse.get_pos()
            #pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
            pygame.draw.circle(screen, (255, 0, 0), pygame.mouse.get_pos(), 2)
            assigned_points.append(pygame.mouse.get_pos())
    elif (not continuous):
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (event.button == 1):  
                #x, y = pygame.mouse.get_pos()
                #pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
                pygame.draw.circle(screen, (255, 0, 0), pygame.mouse.get_pos(), 2)
                assigned_points.append(pygame.mouse.get_pos())
                
    if (not continuous):
        assigned_points = list(dict.fromkeys(assigned_points))
        #print(len(assigned_points))
'''


class Drawer:

    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings
        self.raw_animations = {}
        self.formatted_animations = {}
        self.names = []
        self.current_working_name = ""

    def create_animation(self, name):
        self.names.append(name)
        self.raw_animations[name] = []
        self.formatted_animations[name] = []

    def select_animation(self, name):
        self.current_working_name = name

    def init_animation(self, name):
        self.create_animation(name)
        self.select_animation(name)

    def drawing(self, event, continuous=0):
        if (continuous):
            mouse = pygame.mouse.get_pressed()
        self.screen.fill(self.settings["screen"]["bg-color"])
            
        for point in self.raw_animations[self.current_working_name]:#assigned_points:
            pygame.draw.circle(self.screen, (0, 0, 255), point, 10)
            #x, y = point
            #pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
        if (continuous):
            if (mouse[0]):
                #x, y = pygame.mouse.get_pos()
                #pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
                pygame.draw.circle(self.screen, (255, 0, 0), pygame.mouse.get_pos(), 2)
                #assigned_points.append(pygame.mouse.get_pos())
                self.raw_animations[self.current_working_name].append(pygame.mouse.get_pos())
        elif (not continuous):
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (event.button == 1):  
                    #x, y = pygame.mouse.get_pos()
                    #pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
                    pygame.draw.circle(self.screen, (255, 0, 0), pygame.mouse.get_pos(), 2)
                    #assigned_points.append(pygame.mouse.get_pos())
                    self.raw_animations[self.current_working_name].append(pygame.mouse.get_pos())
                    
        if (not continuous):
            # removes duplicate positions but preserves order
            self.raw_animations[self.current_working_name] = list(dict.fromkeys(self.raw_animations[self.current_working_name]))
            
