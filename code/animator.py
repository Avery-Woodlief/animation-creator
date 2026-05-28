import json
import pygame
import os
from drawer import *
from animation_player import *
from math_helper import *
from event_handler import *
from file_ops import *

file_ops = FileHandler()
#file_ops.init_animation_dir()




settings = file_ops.get_file_settings()


pygame.init()
screen_settings = settings["display"]["screen-size"]
screen = pygame.display.set_mode((screen_settings["width"], screen_settings["height"]))

clock = pygame.time.Clock()


animation_name = ""#input("choose name for first animation: ") # TODO: uncomment

draw_helper = Drawer(settings, screen)
draw_helper.init_animation(animation_name)

animation_player = AnimationPlayer(settings, screen)

math_helper = MathMixin(settings["animation"])
event_handler = EventHandler(settings["general"]["key bindings"], draw_helper, animation_player)
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
