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
            if (button.check_state(event) == "clicked" and (event.type != pygame.MOUSEBUTTONUP)):
                try:
                    events.remove(event)
                except (ValueError): # already removed
                    return button.action()
                return button.action()
        return

    def kill(self): # for semantics
        print("killed window...")
        return
