import json

settings = {}

settings["screen"] = {"width" : 500, "height" : 500, "bg-color":(255, 255, 255)}
settings["general"] = {"frame cap":60}
#settings["animation"] = {"frames":10, "lifetime":.5} # lifetime is in seconds # TODO
#settings["animation"]["FPS"] = (settings["animation"]["frames"])/(settings["animation"]["lifetime"])
settings["animation"] = {"FPS":60}

with open("config.json", "w+") as file:
    json.dump(settings, file, indent=4)



