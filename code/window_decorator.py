import pygame

class WindowDecorator:

    def __init__(self, settings, screen):
        self.fonts = settings["display"]["fonts"]
        self.font_sizes = settings["display"]["font-sizes"]
        self.color_settings = settings["display"]["colors"]
        self.screen = screen
        self.title_text = ""

    def update_window_text(self, title):
        self.title_text = title

    def put_text_on_window(self):
        text_surface = self.fonts["arial"](self.font_sizes["x-large"]).render(
                self.title_text,
                True,              # antialiasing
                self.color_settings["color-custom-rgb"](20, 40, 255)    # color
            )
        # Draw text
        self.screen.blit(text_surface, (100, 100))
