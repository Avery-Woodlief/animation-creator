import json
import os

class FileHandler:

    def __init__(self):
        self.name_of_animation_dir = ""
        

    def get_file_settings(self):
        with open("../settings/config.json", "r") as file:
            return json.load(file)

    def dump_data(self, raw, abstract):
        with open(f"../animations/{self.name_of_animation_dir}/raw.json", "w") as file:
            json.dump(raw, file, indent=4)

        with open(f"../animations/{self.name_of_animation_dir}/abstract_motion.json", "w") as file:
            json.dump(abstract, file, indent=4)

    def init_animation_dir(self):

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
        self.name_of_animation_dir = name_of_animation_dir
    
