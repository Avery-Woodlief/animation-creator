#import json
import pygame
#import os
from drawer.drawer import *
from animation_player.animation_player import *
from math_.math_helper import *
from window_package.event_handler import *

from window_package.window_handler import *
from decorate_windows import *

def init_dynamic_settings(settings):

    settings["animation"]["points per segment"] = lambda pps_num : pps_num
    settings["animation"]["smooth"] = lambda smoothness_bool : smoothness_bool
    settings["drawing"]["connect points"] = lambda connect_points_bool : connect_points_bool
    settings["drawing"]["continuous"] = lambda continuous_bool:continuous_bool
    settings["display"]["fonts"]["arial"] = lambda x: pygame.font.SysFont('arial', x)
    settings["display"]["fonts"]["custom"] = lambda name, size : pygame.font.SysFont(name, size)
    settings["display"]["font-sizes"]["custom"] = lambda x: x
    settings["display"]["colors"]["color-custom-rgb"] = lambda r,g,b : (r, g, b)
    settings["display"]["colors"]["color-custom-rgba"] = lambda r,g,b,a : (r, g, b,a)
    settings["general"]["frame cap custom"] = lambda x : x

init_dynamic_settings(settings)






draw_helper = Drawer(settings, screen)


animation_name = ""#input("choose name for first animation: ") # TODO: uncomment
draw_helper.init_animation(animation_name)

animation_player = AnimationPlayer(settings, screen)

math_helper = MathMixin(settings["animation"])



window_handler = WindowHandler(screen, settings, window_names)
for win in window_handler.acceptable_window_names:
    
    window_handler.build(win, window_buttons[win], window_images[win])

event_handler = EventHandler(settings["general"]["key bindings"], draw_helper, animation_player, window_handler)
#, settings["animation"]
