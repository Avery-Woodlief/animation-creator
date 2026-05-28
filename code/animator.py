import json
import pygame
import os
from drawer import*
from math_helper import *
from event_handler import *


# TODO: uncomment
''' 
def init_animation_dir():

    name_of_animation_dir = input("name your animation directory: ")
    parent = "../animations"
    folder_name = f"{name_of_animation_dir}"
    path = os.path.join(parent, folder_name)

    already_exists = True
    while (already_exists):
        try:
            os.makedirs(path, exist_ok=False)
            already_exists = False
        except (FileExistsError) as e:
            print(e)
            resp = input("Are you sure you want to override (Y or N)?")
            if (resp == "Y"):
                os.makedirs(path, exist_ok=True)
                already_exists = False
            elif (resp == "N"):
                name_of_animation_dir = input("name your animation directory: ")
                continue
    return name_of_animation_dir

my_animation = {}
name_of_animation_dir = init_animation_dir()
'''

def play_animation(settings, path):

    R = 2

    for point in path:
        
        clock.tick(settings["animation"]["FPS"])

        screen.fill(tuple(settings["display"]["colors"]["color-white"]))
        pygame.draw.circle(screen, (0, 0, 0), point, R)
        pygame.display.flip()


with open("../settings/config.json", "r") as file:
    settings = json.load(file)



pygame.init()
screen_settings = settings["display"]["screen-size"]
screen = pygame.display.set_mode((screen_settings["width"], screen_settings["height"]))

clock = pygame.time.Clock()

#menu = {"selection" : False, "drawing":False, "play current work": False}


animation_name = ""#input("choose name for first animation: ") # TODO: uncomment

draw_helper = Drawer(settings["display"], screen)
draw_helper.init_animation(animation_name)

math_helper = MathMixin(settings["animation"])
event_handler = EventHandler(settings["general"]["key bindings"])


FPS = settings["animation"]["FPS-normal"]

while event_handler.running:
    
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()

    clock.tick(FPS)

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


with open(f"../animations/{name_of_animation_dir}/raw.json", "w") as file:

    json.dump(raw_paths, file, indent=4)

with open(f"../animations/{name_of_animation_dir}/abstract_motion.json", "w") as file:

    json.dump(abstract_motion_paths, file, indent=4)



pygame.quit()
