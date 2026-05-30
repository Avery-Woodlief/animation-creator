import pygame

class Button:

    def __init__(self, screen, position, size, color, func, args = "", img_path = None, click_events = [(pygame.MOUSEBUTTONDOWN, -1)], cursor = pygame.SYSTEM_CURSOR_ARROW, clickable = True, hover_img_path = None, click_img_path = None):
        self.screen = screen
        self.function = func
        self.args = args
        self.meta_data = {"position" : position, "size": size, "color": color}

        # default image (no events)
        self.default_img_path = img_path
        self.default_img = None      
        self.load_img('default_img_path', 'default_img')
        
        
        # hover image
        self.hover_img_path = hover_img_path
        self.hover_img = None
        self.load_img('hover_img_path', 'hover_img')

        # image for click event (for the event in 'click_events')
        self.click_img_path = click_img_path
        self.click_img = None
        self.load_img('click_img_path', 'click_img')
        

        # the image currently being used
        self.current_img = self.default_img
        
        self.body = pygame.draw.rect(self.screen, color, position + size)
        self.clickable = clickable
        self.cursor = cursor
        self.click_events = [click_events[i][0] for i in range(len(click_events))]
        self.keys = [click_events[i][1] for i in range(len(click_events))]
        self.acceptable_event_types = [pygame.MOUSEMOTION] + self.click_events
        self.bg_color = (255, 255, 255)
        self.visible = False
        


    def load_img(self, path, img_var): # treated as names of variables for the Button class, not the values
        try:
            if (eval(f"self.{path}")):
                exec(f"self.{img_var} = pygame.image.load(self.{path})")
                exec(f"self.{img_var} = pygame.transform.scale(self.{img_var}, self.meta_data['size'])")
                
        except (AttributeError):
            
            return

    def toggle_visibility(self):
        #print(self.default_img)
        if (self.visible):
            #self.body = pygame.draw.rect(self.screen, self.bg_color, self.meta_data["position"] + self.meta_data["size"])
            self.visible = False
        else:
            self.body = pygame.draw.rect(self.screen, self.meta_data["color"], self.meta_data["position"] + self.meta_data["size"])
            if (self.current_img):
                self.screen.blit(self.current_img, self.meta_data["position"])
                #self.current_img = self.default_img
            self.visible = True

    def reload_image(self):
        self.toggle_visibility()
        self.toggle_visibility()

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
                
                if (self.click_img):
                    self.current_img = self.click_img
                    self.reload_image()
                return "clicked"
        elif (event.type == pygame.MOUSEMOTION):
            
            if (self.body.collidepoint(event.pos)):
                if (self.clickable):
                    
                    if (self.hover_img):
                        self.current_img = self.hover_img
                        self.reload_image()

                    return "hovering"
            else:
                self.current_img = self.default_img
                self.reload_image()

        if (event.type in self.click_events): # NOT a mouse click
            if (event.key in self.keys):
                
                if (self.click_img):
                    self.current_img = self.click_img
                    self.reload_image()
                return "clicked"

        
                

    def action(self): # what does the button do
        #print("clicked")
        if (not self.function):
            return
            
        if (len(self.args) == 0):
            self.function()
        else:
            return self.function(eval(self.args))
       
