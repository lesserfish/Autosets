from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import json

url_list = [("https://www.muscleandstrength.com/exercises/abductors.html", "abductors"),
			("https://www.muscleandstrength.com/exercises/abs", "abs"),
			("https://www.muscleandstrength.com/exercises/abs?page=1", "abs"),
			("https://www.muscleandstrength.com/exercises/abs?page=2", "abs"),
			("https://www.muscleandstrength.com/exercises/adductors.html", "adductors"),
			("https://www.muscleandstrength.com/exercises/biceps", "biceps"),
			("https://www.muscleandstrength.com/exercises/biceps?page=1", "biceps"),
			("https://www.muscleandstrength.com/exercises/calves", "calves"),
			("https://www.muscleandstrength.com/exercises/calves?page=1", "calves"),
			("https://www.muscleandstrength.com/exercises/chest", "chest"),
			("https://www.muscleandstrength.com/exercises/chest?page=1", "chest"),
			("https://www.muscleandstrength.com/exercises/chest?page=2", "chest"),
			("https://www.muscleandstrength.com/exercises/chest?page=3", "chest"),
			("https://www.muscleandstrength.com/exercises/forearms", "forearms"),
			("https://www.muscleandstrength.com/exercises/forearms?page=1", "forearms"),
			("https://www.muscleandstrength.com/exercises/glutes", "glutes"),
			("https://www.muscleandstrength.com/exercises/glutes?page=1", "glutes"),
			("https://www.muscleandstrength.com/exercises/hamstrings", "hamstrings"),
			("https://www.muscleandstrength.com/exercises/hamstrings?page=1", "hamstrings"),
#			("https://www.muscleandstrength.com/exercises/hip-flexors", "hip flexor"),
#			("https://www.muscleandstrength.com/exercises/it-band", "it band"),
			("https://www.muscleandstrength.com/exercises/lats", "lats"),
			("https://www.muscleandstrength.com/exercises/lower-back", "lower back"),
			("https://www.muscleandstrength.com/exercises/middle-back", "upper back"),
			("https://www.muscleandstrength.com/exercises/middle-back?page=1", "upper back"),
			("https://www.muscleandstrength.com/exercises/neck.html", "neck"),
#			("https://www.muscleandstrength.com/exercises/obliques", "obliques"),
#			("https://www.muscleandstrength.com/exercises/palmar-fascia", "palmar fascia"),
#			("https://www.muscleandstrength.com/exercises/plantar-fascia", "plantar fascia"),
			("https://www.muscleandstrength.com/exercises/quads", "quads"),
			("https://www.muscleandstrength.com/exercises/quads?page=1", "quads"),
			("https://www.muscleandstrength.com/exercises/quads?page=2", "quads"),
			("https://www.muscleandstrength.com/exercises/quads?page=3", "quads"),
			("https://www.muscleandstrength.com/exercises/quads?page=4", "quads"),
			("https://www.muscleandstrength.com/exercises/shoulders", "shoulders"),
			("https://www.muscleandstrength.com/exercises/shoulders?page=1", "shoulders"),
			("https://www.muscleandstrength.com/exercises/shoulders?page=2", "shoulders"),
			("https://www.muscleandstrength.com/exercises/shoulders?page=3", "shoulders"),
			("https://www.muscleandstrength.com/exercises/shoulders?page=4", "shoulders"),
			("https://www.muscleandstrength.com/exercises/traps", "traps"),
			("https://www.muscleandstrength.com/exercises/triceps", "triceps"),
			("https://www.muscleandstrength.com/exercises/triceps?page=1", "triceps"),
			("https://www.muscleandstrength.com/exercises/triceps?page=2", "triceps")]


class_name = "bp600-6"
link_node = "node-image"
info_node = "exercise-meta"
info_ind = "cell"
driver = webdriver.Firefox()


workout_output = dict()

class exercise:
	name = ""
	link = ""
	exercise_type = ""
	equipment = ""
	muscles = ""
	experience = ""


i = 0
for url_tuple in url_list:
	url = url_tuple[0]
	driver.get(url)
	el = WebDriverWait(driver, timeout = 15).until(lambda d: d.find_element_by_class_name(class_name))

	output = driver.find_elements_by_class_name(class_name)
	for element in output:
		i = i + 1
		
		info_dict = dict()
		
		link_output = element.find_element_by_class_name(link_node)
		link = link_output.find_element_by_tag_name('a').get_attribute('href')
		
		name = element.find_element_by_class_name("node-title").get_attribute("innerText")
		

		info_dict["musclegroup"] = url_tuple[1]
		info_dict["link"] = link
		info_dict["name"] = name

		exercise_output = element.find_element_by_class_name(info_node)
		info_elements = exercise_output.find_elements_by_class_name(info_ind)
		for ie in info_elements:
			label = ie.find_element_by_class_name("meta-box").find_element_by_tag_name('label').get_attribute("innerHTML")
			value = ie.find_element_by_class_name("meta-box").get_attribute("innerText")
			info_dict[label] = value
		
		print(link)
		workout_output[str(i)] = info_dict

	print("There are " + str(i) + " elements.")



json_output = json.dumps(workout_output);

file_output = "exercise_list.json"
file = open(file_output, "w")
file.write(json_output)	
file.close()
driver.close()
