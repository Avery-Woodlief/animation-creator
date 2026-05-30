import pygame

class Button:

    def __init__(self, screen, position, size, color, func, args = "", img_path = None, click_events = [(pygame.MOUSEBUTTONDOWN, -1)], cursor = pygame.SYSTEM_CURSOR_ARROW, clickable = True):
        self.screen = screen
        self.function = func
        self.args = args
        self.img_path = img_path
        self.default_img_path = self.img_path
        self.img = None
        self.meta_data = {"position" : position, "size": size, "color": color}
        self.load_img()
        
        self.body = pygame.draw.rect(self.screen, color, position + size)
        self.clickable = clickable
        self.cursor = cursor
        self.click_events = [click_events[i][0] for i in range(len(click_events))]
        self.keys = [click_events[i][1] for i in range(len(click_events))]
        self.acceptable_event_types = [pygame.MOUSEMOTION] + self.click_events
        self.bg_color = (255, 255, 255)
        self.visible = False
        


    def load_img(self):
        if (self.img_path):
            self.img = pygame.image.load(self.img_path)
            self.img = pygame.transform.scale(self.img, self.meta_data["size"])

    def toggle_visibility(self):
        if (self.visible):
            #self.body = pygame.draw.rect(self.screen, self.bg_color, self.meta_data["position"] + self.meta_data["size"])
            self.visible = False
        else:
            self.body = pygame.draw.rect(self.screen, self.meta_data["color"], self.meta_data["position"] + self.meta_data["size"])
            if (self.img):
                self.screen.blit(self.img, self.meta_data["position"])
            self.visible = True

    

    def check_state(self, event):
        if (not self.clickable):
            return
        if (not self.visible):
            return
        if (event.type not in self.acceptable_event_types):
            return
        # normal mouse event handling
        if ((event.type == pygame.MOUSEBUTTONDOWN) and (pygame.MOUSEBUTTONDOWN in self.click_events)):
            if (not self.body.collidepoint(event.pos)):
                return
            else:
                return "clicked"
        elif (event.type == pygame.MOUSEMOTION):
            
            if (self.body.collidepoint(event.pos)):
                if (self.clickable):
                    return "hovering"

        if (event.type in self.click_events): # NOT a mouse click
            if (event.key in self.keys):
                return "clicked"

        
                

    def action(self): # what does the button do
        #print("clicked")
        if (not self.function):
            return
            
        if (len(self.args) == 0):
            self.function()
        else:
            return self.function(eval(self.args))
       
