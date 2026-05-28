import numpy as np
from math import floor, ceil

class MathMixin:

    def __init__(self, settings):
        self.settings = settings

    def round_to_nearest_integer(self, x):
	    return (floor(x + 0.5) + ceil((2*x - 1)/4) - floor((2*x - 1)/4) - 1)

    def interpolate(self, raw_points_dict, names):
        if (self.settings["smooth - static"]):
            interpolated_points_dict = {}
            for name in names:
                interpolated_points = []
                for i in range(1, len(raw_points_dict[name])):
                    pointA = raw_points_dict[name][i - 1]
                    pointB = raw_points_dict[name][i]
                    segmented_points = np.linspace(pointA, pointB, self.settings["points per segment - static"])
                    for point in segmented_points:
                        a = point[0]
                        b = point[1]
                        p = (int(self.round_to_nearest_integer(a)), int(self.round_to_nearest_integer(b))) # might be a numpy int type without int
                        interpolated_points.append(p)
                interpolated_points_dict[name] = interpolated_points
            return interpolated_points_dict
        else:
            return raw_points_dict

    def make_abstract_motions(self, draw_helper):
        for name in draw_helper.names:
            draw_helper.formatted_animations[name] = []
            for raw_point in draw_helper.raw_animations[name]:
                dx = raw_point[0] - draw_helper.raw_animations[name][0][0]
                dy = raw_point[1] - draw_helper.raw_animations[name][0][1]
                draw_helper.formatted_animations[name].append([dx, dy])
