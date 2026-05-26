import json
import pygame
import os
from drawer import*


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


def play_animation(settings, path):

    R = 2

    for point in path:
        
        clock.tick(settings["animation"]["FPS"])

        screen.fill(tuple(settings["screen"]["bg-color"]))
        pygame.draw.circle(screen, (0, 0, 0), point, R)
        pygame.display.flip()


with open("../settings/config.json", "r") as file:
    settings = json.load(file)


pygame.init()
screen = pygame.display.set_mode((settings["screen"]["width"], settings["screen"]["height"]))

clock = pygame.time.Clock()

running = True

menu = {"selection" : False, "drawing":False, "play current work": False}


animation_name = input("choose name for first animation: ")

draw_helper = Drawer(settings, screen)
draw_helper.init_animation(animation_name)

while running:

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()

    clock.tick(settings["general"]["frame cap"])

    if keys[pygame.K_1]:
        for k in menu.keys():
            menu[k] = False
        menu["play current work"] = True
    elif keys[pygame.K_2]:
        for k in menu.keys():
            menu[k] = False
        menu["drawing"] = True
    elif keys[pygame.K_3]:
        for k in menu.keys():
            menu[k] = False
        menu["selection"] = True
        animation_name = input("choose name for next animation: ")
        draw_helper.init_animation(animation_name)

    if (menu["drawing"]):
        continuous = 0
        draw_helper.drawing(event)
        if (not continuous):
            draw_helper.raw_animations[draw_helper.current_working_name] = list(dict.fromkeys(draw_helper.raw_animations[draw_helper.current_working_name]))
    elif (menu["play current work"]):
        play_animation(settings, draw_helper.raw_animations[draw_helper.current_working_name])

        menu["play current work"] = False
    elif (menu["selection"]):
        screen.fill((0, 0, 0))
    pygame.display.flip()



for name in draw_helper.names:

    position_differences = []

    for i in range(1, len(draw_helper.raw_animations[name])):
        point_i_MINUS_ONE = draw_helper.raw_animations[name][i - 1]
        point_i = draw_helper.raw_animations[name][i]
        position_differences.append((point_i[0] - point_i_MINUS_ONE[0], point_i[1] - point_i_MINUS_ONE[1]))

    for i in range(len(position_differences)):
        dx = position_differences[i][0]
        dy = position_differences[i][1]
        for j in range(i):
            dx += position_differences[j][0]
            dy += position_differences[j][1]
        draw_helper.formatted_animations[name].append((dx, dy))


raw_paths = {}
abstract_motion_paths = {}

for name in draw_helper.names:
    
    raw_paths[name] = draw_helper.raw_animations[name]
    abstract_motion_paths[name] = draw_helper.formatted_animations[name]

with open(f"../animations/{name_of_animation_dir}/raw.json", "w+") as file:
    json.dump(raw_paths, file, indent=4)
    file.close() 

with open(f"../animations/{name_of_animation_dir}/abstract_motion.json", "w+") as file:
    json.dump(abstract_motion_paths, file, indent=4)
    file.close()
    

# default is to have it run at 60 frames per second


pygame.quit()
