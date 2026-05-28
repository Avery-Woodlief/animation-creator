import pygame

class AnimationPlayer:

    def __init__(self, settings, screen):
        self.animation_settings = settings["animation"]
        self.color_settings = settings["display"]["colors"]
        self.screen = screen
        

    def play_animation(self, raw_points):
        R = 2
        for point in raw_points:
        
            pygame.time.Clock().tick(self.animation_settings["FPS-animation-player"])

            self.screen.fill(self.color_settings["color-white"])
            pygame.draw.circle(self.screen, self.color_settings["color-black"], point, R)
            pygame.display.flip()
    
