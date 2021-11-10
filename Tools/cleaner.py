import json

og_file = "./exercise_list.json"

file = open(og_file, "r")
og_content = file.read()
og_json = json.loads(og_content)
file.close()

exercises_output = dict()
musclegroup_output = dict()
equipment_output = dict()
mechanics_output = dict()
experience_output = dict()
type_output = dict()

for key in og_json.keys():
    entry = og_json[key]
    new_entry = dict()

    musclegroup = entry["musclegroup"][0].upper() + entry["musclegroup"][1:]
    link = entry["link"]
    name = entry["name"]
    type = entry["Type"][5] + entry["Type"][6:].lower()
    equipment = entry["Equipment"][10] + entry["Equipment"][11:].lower()
    mechanics = entry["Mechanics"][10] + entry["Mechanics"][11:].lower()
    exp = entry["Exp. Level"][11] + entry["Exp. Level"][12:].lower()

    new_entry["MuscleGroup"] = musclegroup
    new_entry["Link"] = link
    new_entry["Name"] = name
    new_entry["Type"] = type
    new_entry["Equipment"] = equipment
    new_entry["Mechanics"] = mechanics
    new_entry["Experience"] = exp

    exercises_output[key] = new_entry

    if not(musclegroup in musclegroup_output.values()):
        musclegroup_output[len(musclegroup_output) + 1] = musclegroup
    if not(equipment in equipment_output.values()):
        equipment_output[len(equipment_output) + 1] = equipment 
    if not(mechanics in mechanics_output.values()):
        mechanics_output[len(mechanics_output) + 1] = mechanics 
    if not(exp in experience_output.values()):
        experience_output[len(experience_output) + 1] = exp
    if not(type in type_output.values()):
        type_output[len(type_output) + 1] = type

print(musclegroup_output, end="\n\n")
print(equipment_output, end="\n\n")
print(mechanics_output, end="\n\n")
print(experience_output, end="\n\n")
print(type_output, end = "\n\n")

output = dict()

output["Exercises"] = exercises_output
output["MuscleGroups"] = musclegroup_output
output["Equipment"] = equipment_output
output["Mechanics"] = mechanics_output
output["Experience"] = experience_output
output["Types"] = type_output

json_output = json.dumps(output)
file = open("db.json", "w")
file.write(json_output)
file.close()
