import json
import pygame
import os
from drawer import *
from animation_player import *
from math_helper import *
from event_handler import *
from file_ops import *
from window_handler import *


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

file_ops = FileHandler()
#file_ops.init_animation_dir()




settings = file_ops.get_file_settings()

init_dynamic_settings(settings)


pygame.init()
screen_settings = settings["display"]["screen-size"]
screen = pygame.display.set_mode((screen_settings["width"], screen_settings["height"]))
pygame.display.set_caption("Animation Creator")
clock = pygame.time.Clock()


animation_name = ""#input("choose name for first animation: ") # TODO: uncomment

#window_decorator = WindowDecorator(screen, settings)

draw_helper = Drawer(settings, screen)
draw_helper.init_animation(animation_name)

animation_player = AnimationPlayer(settings, screen)

math_helper = MathMixin(settings["animation"])


window_names = ["start", "animation player", "drawer", "selection"]


window_buttons = {name : [] for name in window_names}

window_buttons["animation player"] = [Button(screen, (50, 50), (50, 50), (0, 255, 255),lambda : print("animation player button") , "")]
window_buttons["drawer"] = [Button(screen, (50, 50), (50, 50), (0, 255, 0), lambda : print("drawer button"), "")]
window_buttons["selection"] = [Button(screen, (50, 50), (50, 50), (0, 0, 255), lambda : print("selection"), "", "images/effect_cube.png")]

window_handler = WindowHandler(screen, settings, window_names)
for win in window_handler.acceptable_window_names:
    
    window_handler.build(win, window_buttons[win], None)

event_handler = EventHandler(settings["general"]["key bindings"], draw_helper, animation_player, window_handler)
#, settings["animation"]


FPS = settings["animation"]["FPS-normal"]





while event_handler.running:
    
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()

    clock.tick(120)

    event_handler.get_event(pygame.event.get())

    pygame.display.flip()

math_helper.make_abstract_motions(draw_helper)


raw_paths = {}
abstract_motion_paths = {}

for name in draw_helper.names:
    
    raw_paths[name] = draw_helper.raw_animations[name]
    abstract_motion_paths[name] = draw_helper.formatted_animations[name]

raw_paths = math_helper.interpolate(raw_paths, draw_helper.names)
abstract_motion_paths = math_helper.interpolate(abstract_motion_paths, draw_helper.names)



if (len(file_ops.name_of_animation_dir) > 0):
    file_ops.dump_data(raw_paths, abstract_motion_paths)





pygame.quit()
