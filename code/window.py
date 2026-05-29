
class Window:

    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.children = {"buttons":[], "text":[]}
        self.current_events = []


    def run(self, event):
        print("running window...")
        for button in self.children["buttons"]:
            button.check_state(event)
        return

    def kill(self): # for semantics
        print("killed window...")
        return
