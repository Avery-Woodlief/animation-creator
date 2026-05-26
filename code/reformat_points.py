import re
import json

#f_type = "raw.json"
f_type = "abstract_motion.json"

with open(f"../animations/smoothness_test/{f_type}", "r") as file:
    FILE = json.load(file)

#print("BEFORE RE")
#print(FILE)

motion = FILE["circle"]


#maxX = max([point[0] for point in motion])
#maxY = max([point[1] for point in motion])

a = 0#motion[0][0]
b = 0#motion[0][1]
#"-?\d+\.\d+\,\s*-?\d+\.\d+"
pattern=r"^\[-?(\d+\.\d+|\.\d+|\d+)\,\s*-?(\d+\.\d+|\.\d+|\d+)\]$"
#pattern = r"^\[-?\d+\,\s*-?\d+\]$"

desmos_formatted_string = "["

if (re.fullmatch(pattern, str(motion[0]))):
    d1, d2 = re.findall(r"-?(\d+\.\d+|\.\d+|\d+)", str(motion[0]))
    try:
        d1 = int(d1)
    except (ValueError):
        d1 = float(d1)
    try:
        d2 = int(d2)
    except (ValueError):
        d2 = float(d2)
    desmos_formatted_string += f"({d1 - a}, {d2 - b})"

skip_first = True

for point in motion:

    if skip_first:
        skip_first = False
        continue

    if (re.fullmatch(pattern, str(point))):
        d1, d2 = re.findall(r"-?(\d+\.\d+|\.\d+|\d+)", str(point))
        try:
            d1 = int(d1)
        except (ValueError):
            d1 = float(d1)
        try:
            d2 = int(d2)
        except (ValueError):
            d2 = float(d2)
        desmos_formatted_string += f", ({d1 - a}, {d2 - b})"

desmos_formatted_string += "]"

print(desmos_formatted_string)
