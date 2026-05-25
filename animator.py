import json
import pygame

my_animation = {}

name_of_animation = input("name your animation (careful of overrides!): ")


def drawing(settings, assigned_points, event, continuous):

    if (continuous):
        mouse = pygame.mouse.get_pressed()
    screen.fill(settings["screen"]["bg-color"])
    for point in assigned_points:
        pygame.draw.circle(screen, (0, 0, 255), point, 10)
        #x, y = point
        #pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
    if (continuous):
        if (mouse[0]):
            #x, y = pygame.mouse.get_pos()
            #pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
            pygame.draw.circle(screen, (255, 0, 0), pygame.mouse.get_pos(), 2)
            assigned_points.append(pygame.mouse.get_pos())
    elif (not continuous):
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (event.button == 1):  
                #x, y = pygame.mouse.get_pos()
                #pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
                pygame.draw.circle(screen, (255, 0, 0), pygame.mouse.get_pos(), 2)
                assigned_points.append(pygame.mouse.get_pos())
                
    if (not continuous):
        assigned_points = list(dict.fromkeys(assigned_points))
        print(len(assigned_points))

def play_animation(settings, path):

    R = 2

    for point in path:
        
        clock.tick(settings["animation"]["FPS"])

        screen.fill(tuple(settings["screen"]["bg-color"]))
        pygame.draw.circle(screen, (0, 0, 0), point, R)
        pygame.display.flip()

'''
def play_animation2(settings, changes, start):

    R = 2

    for change in changes:
        
        dx, dy = change

        clock.tick(settings["animation"]["FPS"])

        screen.fill(tuple(settings["screen"]["bg-color"]))
        pygame.draw.circle(screen, (0, 0, 0), (start[0] + dx, start[1] + dy), R)
        pygame.display.flip()
'''

with open("settings/config.json", "r") as file:
    settings = json.load(file)

#path = [(i + 100, 100) for i in range(0, 120, 2)]
assigned_points = []

#print(len(path))


pygame.init()
screen = pygame.display.set_mode((settings["screen"]["width"], settings["screen"]["height"]))

clock = pygame.time.Clock()

running = True

menu = {"selection" : False, "drawing":False, "play current work": False}

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

    if (menu["drawing"]):
        continuous = 0
        drawing(settings, assigned_points, event, continuous)
        if (not continuous):
            assigned_points = list(dict.fromkeys(assigned_points))
    elif (menu["play current work"]):
        play_animation(settings, assigned_points)
        #play_animation2(settings, my_animation["path position independent"], (50, 50))
        menu["play current work"] = False
    elif (menu["selection"]):
        screen.fill((0, 0, 0))
    pygame.display.flip()

#print(assigned_points)


position_differences = []

for i in range(1, len(assigned_points)):
    point_i_MINUS_ONE = assigned_points[i - 1]
    point_i = assigned_points[i]
    position_differences.append((point_i[0] - point_i_MINUS_ONE[0], point_i[1] - point_i_MINUS_ONE[1]))


formatted = []

for i in range(len(position_differences)):
    dx = position_differences[i][0]
    dy = position_differences[i][1]
    for j in range(i):
        dx += position_differences[j][0]
        dy += position_differences[j][1]
    formatted.append((dx, dy))

my_animation["path raw"] = assigned_points
my_animation["path position independent"] = formatted#position_differences

import os

parent = "animations"

folder_name = f"{name_of_animation}"

path = os.path.join(parent, folder_name)

os.makedirs(path, exist_ok=True)


with open(f"animations/{name_of_animation}/raw.json", "w+") as file:
    json.dump(my_animation["path raw"], file, indent=4)

with open(f"animations/{name_of_animation}/abstract_motion.json", "w+") as file:
    json.dump(my_animation["path position independent"], file, indent=4)

# default is to have it run at 60 frames per second


pygame.quit()
