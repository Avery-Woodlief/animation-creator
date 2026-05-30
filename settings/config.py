import json
import pygame


settings = {}

settings["display"] = {}

settings["display"]["screen"] = {"width" : 1500, "height" : 850}
settings["display"]["screen"]["background color"] = (150, 150, 150)
settings["display"]["screen"]["borderless"] = pygame.NOFRAME
settings["display"]["screen"]["bordered"] = 0
settings["display"]["screen"]["active flag"] = 0

settings["display"]["colors"] = {}
settings["display"]["colors"]["color-white"] = (255, 255, 255)
settings["display"]["colors"]["color-black"] = (0, 0, 0)
settings["display"]["colors"]["color-grey"] = (50, 50, 50)
settings["display"]["colors"]["color-bright-red"] = (255, 0, 0)
settings["display"]["colors"]["color-bright-green"] = (0, 255, 0)
settings["display"]["colors"]["color-bright-blue"] = (0, 0, 255)
settings["display"]["colors"]["color-custom-rgb"] = ""
settings["display"]["colors"]["color-custom-rgba"] = ""


settings["display"]["font-sizes"] = {"small":10, "medium":20, "large":30, "x-large":40}
settings["display"]["font-sizes"]["custom"] = ""
settings["display"]["fonts"] = {}
settings["display"]["fonts"]["arial"] = ""
settings["display"]["fonts"]["custom"] = ""


settings["general"] = {"frame cap":60}
settings["general"]["frame cap custom"] = "" 

settings["general"]["key bindings"] = {}
settings["general"]["key bindings"]["mod key references"] = {}
settings["general"]["key bindings"]["mod key references"][pygame.KMOD_LCTRL] = "LCTRL"
settings["general"]["key bindings"]["mod key references"][pygame.KMOD_LSHIFT] = "LSHIFT"
settings["general"]["key bindings"]["mod key references"][pygame.KMOD_LALT] = "LALT"
settings["general"]["key bindings"]["mod key references"][pygame.KMOD_RCTRL] = "RCTRL" 
settings["general"]["key bindings"]["mod key references"][pygame.KMOD_RSHIFT] = "RSHIFT"
settings["general"]["key bindings"]["mod key references"][pygame.KMOD_RALT] = "RALT"


settings["general"]["key bindings"]["nonmod key references"] = {ord('a')+i:chr(ord('a')+i) for i in range(26)}
settings["general"]["key bindings"]["nonmod key references"][pygame.K_DELETE] = "DEL"
settings["general"]["key bindings"]["nonmod key references"][pygame.K_ESCAPE] = "ESC"


settings["general"]["key bindings"]["window-commands"] = {}
settings["general"]["key bindings"]["window-commands"]["ESC"] = "quits program"
settings["general"]["key bindings"]["window-commands"]["LSHIFT b"] = "making window borderless"
settings["general"]["key bindings"]["window-commands"]["LCTRL LSHIFT b"] = "making window bordered"


settings["general"]["key bindings"]["drawing-commands"] = {}
settings["general"]["key bindings"]["drawing-commands"]["LSHIFT s"] = "begin drawing animation"
settings["general"]["key bindings"]["drawing-commands"]["LCTRL LSHIFT s"] = "stop drawing animation"
settings["general"]["key bindings"]["drawing-commands"]["LSHIFT e"] = "erasor mode"
settings["general"]["key bindings"]["drawing-commands"]["LSHIFT DEL"] = "delete entire animation"
settings["general"]["key bindings"]["drawing-commands"]["LCTRL LSHIFT n"] = "create new animation"
settings["general"]["key bindings"]["drawing-commands"]["LCTRL LSHIFT c"] = "open shape"
settings["general"]["key bindings"]["drawing-commands"]["LSHIFT c"] = "close shape" 
settings["general"]["key bindings"]["drawing-commands"]["LCTRL o"] = "toggle overlay" 
settings["general"]["key bindings"]["drawing-commands"]["LSHIFT l v"] = "toggle vertical line" 
settings["general"]["key bindings"]["drawing-commands"]["LSHIFT l h"] = "toggle horizontal line" 
settings["general"]["key bindings"]["drawing-commands"]["LCTRL z"] = "undo last node" 


settings["general"]["key bindings"]["drawing-commands"]["LCTRL LSHIFT z"] = "redo last undo" 
settings["general"]["key bindings"]["drawing-commands"]["LCTRL DEL"] = "delete selected node" 
settings["general"]["key bindings"]["drawing-commands"]["LSHIFT d"] = "make disjoint" 
# seperates what is on screen to own animation value in the json file

settings["general"]["key bindings"]["animation-commands"] = {}

settings["general"]["key bindings"]["animation-commands"]["LCTRL LSHIFT r"] = "reverse animation direction"

settings["general"]["key bindings"]["animation-commands"]["LCTRL LSHIFT c"] = "customize animation direction" # TODO
#settings["general"]["key bindings"]["animation-commands"][pygame.K_LCTRL and LEFT_MOUSE] = "select node" # TODO



settings["animation"] = {"FPS-normal":120, "FPS-mouse-click":20, "frames count":10}
settings["animation"]["FPS-animation-player"] = 120
settings["animation"]["FPS-mouse-drag"] = 60
settings["animation"]["lifetime"] = settings["animation"]["frames count"]/settings["animation"]["FPS-normal"] # lifetime measured in seconds

# TODO
# if set to True, program will try to interpolate extra points
settings["animation"]["smooth"] = ""
settings["animation"]["smooth - static"] = False
# this is effectively how detailed each line will be for smoothness 
settings["animation"]["points per segment"] = ""
settings["animation"]["points per segment - static"] = 5
#settings["animation"]["continuous"] = False


# TODO
settings["drawing"] = {"connect points":"", "continuous":""}
settings["drawing"]["connect points - static"] = False
settings["drawing"]["continuous - static"] = False

settings["mouse-settings"] = {}
settings["mouse-settings"]["active cursor"] = pygame.SYSTEM_CURSOR_ARROW
settings["mouse-settings"]["cursor types"] = {}
settings["mouse-settings"]["cursor types"]["cursor-arrow"] = pygame.SYSTEM_CURSOR_ARROW
settings["mouse-settings"]["cursor types"]["cursor-hand"] = pygame.SYSTEM_CURSOR_HAND

'''
button.img_path = "images/effect_cube.png"
                button.load_img()
                # toggle_visibility done twice so it returns to visibility state as before
                button.toggle_visibility()
                button.toggle_visibility()
'''

with open("config.json", "w+") as file:
    json.dump(settings, file, indent=4)



