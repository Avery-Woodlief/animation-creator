import json

settings = {}

settings["display"] = {}

settings["display"]["screen-size"] = {"width" : 500, "height" : 500}

settings["display"]["colors"] = {}
settings["display"]["colors"]["color-white"] = (255, 255, 255)
settings["display"]["colors"]["color-black"] = (0, 0, 0)
settings["display"]["colors"]["color-grey"] = (50, 50, 50)
settings["display"]["colors"]["color-bright-red"] = (255, 0, 0)
settings["display"]["colors"]["color-bright-green"] = (0, 255, 0)
settings["display"]["colors"]["color-bright-blue"] = (0, 0, 255)




settings["general"] = {"frame cap":60}
settings["animation"] = {"FPS":60, "frames count":10}
settings["animation"]["lifetime"] = settings["animation"]["frames count"]/settings["animation"]["FPS"] # lifetime measured in seconds
settings["animation"]["smooth"] = False # if set to True, program will try to make the animation less 'blocky' in movement
settings["animation"]["points per segment"] = 5 # this is effectively how detailed each line will be for smoothness


with open("config.json", "w+") as file:
    json.dump(settings, file, indent=4)



