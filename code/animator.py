import json
import pygame
import os
from drawer.drawer import *
from animation_player.animation_player import *
from math_.math_helper import *
from window_package.event_handler import *
from file_io.file_ops import *
from window_package.window_handler import *



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
screen_settings = settings["display"]["screen"]
screen = pygame.display.set_mode((screen_settings["width"], screen_settings["height"]))
pygame.display.set_caption("start")
clock = pygame.time.Clock()



draw_helper = Drawer(settings, screen)


animation_name = ""#input("choose name for first animation: ") # TODO: uncomment
draw_helper.init_animation(animation_name)

animation_player = AnimationPlayer(settings, screen)

math_helper = MathMixin(settings["animation"])


window_names = ["start", "animation player", "drawer", "selection"]


window_buttons = {name : [] for name in window_names}
window_images = {name : [] for name in window_names}


def go_to_next_window(current):

    names = ["start", "animation player", "drawer", "selection"]
    try:
        return names[(names.index(current) + 1) % len(names)]
    except:
        return

def go_to_prev_window(current):

    names = ["start", "animation player", "drawer", "selection"]
    try:
        return names[(names.index(current) - 1) % len(names)]
    except:
        return

def create_prev_page_btn(current):
    return Button(screen, (0, screen_settings["height"]-50), (50, 50), (50,50,50), go_to_prev_window, current, "images/left_arrow2.png", (pygame.KEYDOWN, pygame.K_LEFT))

def create_next_page_btn(current):
    return Button(screen, (screen_settings["width"]-50, screen_settings["height"]-50),(50, 50), (150,100,75), go_to_next_window, current, "images/right_arrow2.png", (pygame.KEYDOWN, pygame.K_RIGHT))

def create_background():
    return Button(screen, (0, 0), (1500, 800), (255, 0, 255, 0), None, "","images/welcome_screen.png", clickable=False)

def create_border(img_path):

    left_color = (50, 50, 50)
    right_color = (50, 50, 50)
    top_color = (50, 50, 50)
    bottom_color = (50, 50, 50)

    return [Button(screen, (screen_settings["width"]-12, 0), (12.5, screen_settings["height"]-50), right_color, None, "",img_path, clickable=False), 
            Button(screen, (0, screen_settings["height"]-50-12), (screen_settings["width"], 12.5), bottom_color, None, "",img_path, clickable=False), 
            Button(screen, (0, 0), (screen_settings["width"], 12.5), top_color, None, "",img_path,clickable=False), 
            Button(screen, (0, 0), (12.5, screen_settings["height"]-50), left_color, None, "",img_path, clickable=False)]

#screen, position, size, color, func, args = "", img_path = None

border = "images/block.png"
bottom_thing = "images/block.png"


window_buttons["start"] = [Button(screen, (50, 50), (0, 0), (0, 255, 255),lambda : print("start window") , ""),
                           create_background(),
                           Button(screen, (0, screen_settings["height"]-50), (screen_settings["width"], 50),(50, 50, 50), None, "",img_path=bottom_thing, clickable=False),
                           create_prev_page_btn("\'start\'"), 
                           create_next_page_btn("\'start\'")] + create_border(border)

#window_images["start"] = [Image(screen, (100, 100), (screen_settings["width"], screen_settings["height"]-50), "images/welcome_screen.png")]


window_buttons["animation player"] = [Button(screen, (50, 50), (50, 50), (0, 255, 255),lambda : print("animation player button") , "", cursor = pygame.SYSTEM_CURSOR_HAND),
                                      Button(screen, (0, screen_settings["height"]-50), (screen_settings["width"], 50),(50, 50, 50), None, "",img_path=bottom_thing, clickable=False),
                                      create_prev_page_btn("\'animation player\'"), 
                                      create_next_page_btn("\'animation player\'")] + create_border(border)

window_buttons["drawer"] = [Button(screen, (50, 50), (50, 50), (0, 255, 0), lambda : print("drawer button"), ""),
                            Button(screen, (0, screen_settings["height"]-50), (screen_settings["width"], 50),(50, 50, 50), None, "",img_path=bottom_thing, clickable=False),
                            create_prev_page_btn("\'drawer\'"), 
                            create_next_page_btn("\'drawer\'")] + create_border(border)

window_buttons["selection"] = [Button(screen, (0, screen_settings["height"]-50), (screen_settings["width"], 50),(50, 50, 50), None, "",img_path=bottom_thing, clickable=False),
                               create_prev_page_btn("\'selection\'"), 
                               create_next_page_btn("\'selection\'")] + create_border(border)

window_handler = WindowHandler(screen, settings, window_names)
for win in window_handler.acceptable_window_names:
    
    window_handler.build(win, window_buttons[win], window_images[win])

event_handler = EventHandler(settings["general"]["key bindings"], draw_helper, animation_player, window_handler)
#, settings["animation"]





while event_handler.running:
    
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()

    clock.tick(settings["animation"]["FPS-normal"])

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
