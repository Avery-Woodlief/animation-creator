from file_io.file_ops import *
from window_package.window import *
from window_package.children.button import *

file_ops = FileHandler()

settings = file_ops.get_file_settings()
pygame.init()
screen_settings = settings["display"]["screen"]
screen = pygame.display.set_mode((screen_settings["width"], screen_settings["height"]))
pygame.display.set_caption("start")
clock = pygame.time.Clock()

window_names = ["start", "animation player", "drawer", "selection"]




# ---------------------- BUTTONS START --------------------------


window_buttons = {name : [] for name in window_names}



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
    return Button(screen, (0, screen_settings["height"]-50), (50, 50), (50,50,50), go_to_prev_window, current, "images/left_arrow2.png",click_events= [(pygame.MOUSEBUTTONDOWN, -1), (pygame.KEYDOWN, pygame.K_LEFT)])

def create_next_page_btn(current):
    return Button(screen, (screen_settings["width"]-50, screen_settings["height"]-50),(50, 50), (150,100,75), go_to_next_window, current, "images/right_arrow2.png", click_events = [(pygame.MOUSEBUTTONDOWN, -1), (pygame.KEYDOWN, pygame.K_RIGHT)])

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


# ---------------------- BUTTONS END --------------------------

window_images = {name : [] for name in window_names}

