import pygame

class Button:

    def __init__(self, screen, position, size, color, func, args = "", img_path = None, click_event = (pygame.MOUSEBUTTONDOWN, -1), cursor = pygame.SYSTEM_CURSOR_ARROW, clickable = True):
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
        self.click_event = click_event[0] # this is same as clicking
        self.key = click_event[1]
        self.acceptable_event_types = [pygame.MOUSEMOTION, click_event[0]]
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
        if (self.click_event == pygame.MOUSEBUTTONDOWN):
            if (not self.body.collidepoint(event.pos)):
                return
        if (event.type == pygame.MOUSEMOTION):
            
            if (self.body.collidepoint(event.pos)):
                if (self.clickable):
                    return "hovering"

        if (event.type == self.click_event):
            if (self.key == -1): # just the mouse
                #pygame.mouse.set_cursor(self.cursor)
                #pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                return "clicked"
            else:
                try:
                    if (event.key == self.key):
                        #pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND) not for mouse
                        return "clicked"
                except:
                    return
                

    def action(self): # what does the button do
        #print("clicked")
        if (not self.function):
            return
            
        if (len(self.args) == 0):
            self.function()
        else:
            return self.function(eval(self.args))
       
