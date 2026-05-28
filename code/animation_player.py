import pygame

class AnimationPlayer:

    def __init__(self, settings, screen, window_decorator):
        self.animation_settings = settings["animation"]
        self.fonts = settings["display"]["fonts"]
        self.font_sizes = settings["display"]["font-sizes"]
        self.color_settings = settings["display"]["colors"]
        self.screen = screen
        self.window_decorator = window_decorator
        
    

    def play_animation(self, raw_points):
        R = 2
        for point in raw_points:
        
            pygame.time.Clock().tick(self.animation_settings["FPS-animation-player"])

            self.screen.fill(self.color_settings["color-white"])
            self.window_decorator.put_text_on_window()
            pygame.draw.circle(self.screen, self.color_settings["color-black"], point, R)
            pygame.display.flip()
    
