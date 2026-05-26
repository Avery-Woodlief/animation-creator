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

        screen.fill(tuple(settings["display"]["colors"]["color-white"]))
        pygame.draw.circle(screen, (0, 0, 0), point, R)
        pygame.display.flip()


with open("../settings/config.json", "r") as file:
    settings = json.load(file)


pygame.init()
screen = pygame.display.set_mode((settings["display"]["screen-size"]["width"], settings["display"]["screen-size"]["height"]))

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
        continuous = 1
        draw_helper.drawing(event, continuous)
        #if (not continuous):
            #draw_helper.raw_animations[draw_helper.current_working_name] = list(dict.fromkeys(draw_helper.raw_animations[draw_helper.current_working_name]))
    elif (menu["play current work"]):
        play_animation(settings, draw_helper.raw_animations[draw_helper.current_working_name])

        menu["play current work"] = False
    elif (menu["selection"]):
        screen.fill(settings["display"]["colors"]["color-black"])
    pygame.display.flip()


for name in draw_helper.names:
    draw_helper.formatted_animations[name] = []
    for raw_point in draw_helper.raw_animations[name]:
        dx = raw_point[0] - draw_helper.raw_animations[name][0][0]
        dy = raw_point[1] - draw_helper.raw_animations[name][0][1]
        draw_helper.formatted_animations[name].append([dx, dy])
    #print(draw_helper.formatted_animations[name])

raw_paths = {}
abstract_motion_paths = {}

for name in draw_helper.names:
    
    raw_paths[name] = draw_helper.raw_animations[name]
    abstract_motion_paths[name] = draw_helper.formatted_animations[name]


#print("BEFORE DUMPING")
#print(abstract_motion_paths["circle"])

with open(f"../animations/{name_of_animation_dir}/raw.json", "w") as file:

    json.dump(raw_paths, file, indent=4)

with open(f"../animations/{name_of_animation_dir}/abstract_motion.json", "w") as file:

    json.dump(abstract_motion_paths, file, indent=4)
    

#with open(f"../animations/{name_of_animation_dir}/abstract_motion.json", "r") as file:
#    test = json.load(file)


#print("AFTER DUMPING")
#print(test)

#for name in draw_helper.names:
    #print(abstract_motion_paths[name])

# default is to have it run at 60 frames per second


pygame.quit()
