import json
import pygame

'''
For the mouse

    LEFT_MOUSE = 1
    MIDDLE_MOUSE = 2
    RIGHT_MOUSE = 3

'''

LEFT_MOUSE = 1
MIDDLE_MOUSE = 2
RIGHT_MOUSE = 3

#pygame.init()

settings = {}

settings["display"] = {}

settings["display"]["screen-size"] = {"width" : 1000, "height" : 700}

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
settings["general"]["key bindings"]["mod key references"][pygame.KMOD_LCTRL] = "LCTRL" # 64
settings["general"]["key bindings"]["mod key references"][pygame.KMOD_LSHIFT] = "LSHIFT" # 1

settings["general"]["key bindings"]["nonmod key references"] = {}
settings["general"]["key bindings"]["nonmod key references"][pygame.K_c] = "c"
settings["general"]["key bindings"]["nonmod key references"][pygame.K_o] = "o"
settings["general"]["key bindings"]["nonmod key references"][pygame.K_l] = "l"
settings["general"]["key bindings"]["nonmod key references"][pygame.K_v] = "v"
settings["general"]["key bindings"]["nonmod key references"][pygame.K_h] = "h"
settings["general"]["key bindings"]["nonmod key references"][pygame.K_DELETE] = "del"
settings["general"]["key bindings"]["nonmod key references"][pygame.K_z] = "z"

settings["general"]["key bindings"]["menu-commands"] = {}
settings["general"]["key bindings"]["menu-commands"][pygame.K_1] = "play current work"
settings["general"]["key bindings"]["menu-commands"][pygame.K_2] = "drawing"
settings["general"]["key bindings"]["menu-commands"][pygame.K_3] = "selection"


settings["general"]["key bindings"]["drawing-commands"] = {}
settings["general"]["key bindings"]["drawing-commands"][pygame.K_LSHIFT and pygame.K_c] = "close shape"
settings["general"]["key bindings"]["drawing-commands"][pygame.K_LCTRL and pygame.K_o] = "toggle overlay"
settings["general"]["key bindings"]["drawing-commands"][pygame.K_LSHIFT and pygame.K_l and pygame.K_v] = "toggle vertical line"
settings["general"]["key bindings"]["drawing-commands"][pygame.K_LSHIFT and pygame.K_l and pygame.K_h] = "toggle horizontal line"
settings["general"]["key bindings"]["drawing-commands"][pygame.K_LCTRL and pygame.K_z] = "undo last node"
settings["general"]["key bindings"]["drawing-commands"][pygame.K_LCTRL and pygame.K_LSHIFT and pygame.K_z] = "redo last undo"
settings["general"]["key bindings"]["drawing-commands"][pygame.K_LCTRL and pygame.K_DELETE] = "delete selected node"

settings["general"]["key bindings"]["animation-commands"] = {}
settings["general"]["key bindings"]["animation-commands"][pygame.K_LCTRL and pygame.K_LSHIFT and pygame.K_r] = "reverse animation direction"
settings["general"]["key bindings"]["animation-commands"][pygame.K_LCTRL and pygame.K_LSHIFT and pygame.K_c] = "customize animation direction" # TODO
#settings["general"]["key bindings"]["animation-commands"][pygame.K_LCTRL and LEFT_MOUSE] = "select node" # TODO



settings["animation"] = {"FPS-normal":60, "FPS-mouse-click":20, "frames count":10}
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

#settings["mouse-settings"]["sensitivity"] = 1

with open("config.json", "w+") as file:
    json.dump(settings, file, indent=4)



