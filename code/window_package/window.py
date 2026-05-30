import pygame

class Window:

    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.children = {"buttons":[], "static_images":[]}
        self.current_events = []


    def run(self, event, events):
        #print("running window...")
        #print("ITERATION")
        for button in self.children["buttons"]:
            if (not button):
                continue
            if (not button.clickable):
                continue
            if (button.check_state(event) == "clicked" and (event.type != pygame.MOUSEBUTTONUP)):
                self.settings["mouse-settings"]["active cursor"] = pygame.SYSTEM_CURSOR_HAND
                #print("click button down")
                #self.settings["mouse-settings"]["active cursor"] = pygame.SYSTEM_CURSOR_HAND
                try:
                    events.remove(event)
                except (ValueError): # already removed
                    return button.action()
                return button.action()
            elif (button.check_state(event) == "hovering"):
                self.settings["mouse-settings"]["active cursor"] = pygame.SYSTEM_CURSOR_HAND
                #print("hovering")
        return

    def kill(self): # for semantics
        print("killed window...")
        return
