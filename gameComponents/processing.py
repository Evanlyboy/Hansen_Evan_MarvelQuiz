from gameComponents import characters

def questionSort(answer):
	if answer == "good":
		characters.characterCount["Spider-Man"] += 1
		characters.characterCount["Cyclops"] += 1
	elif answer == "bad":
		characters.characterCount["Mysterio"] += 1
		characters.characterCount["Carnage"] += 1
	elif answer == "yes":
		characters.characterCount["Spider-Man"] += 1
		characters.characterCount["Cyclops"] += 1
	elif answer == "no":
		characters.characterCount["Mysterio"] += 1
		characters.characterCount["Carnage"] += 1
	elif answer == "calm":
		characters.characterCount["Spider-Man"] += 1
		characters.characterCount["Mysterio"] += 1
	elif answer == "erratic":
		characters.characterCount["Cyclops"] += 1
		characters.characterCount["Carnage"] += 1
	elif answer == "acquired":
		characters.characterCount["Spider-Man"] += 1
		characters.characterCount["Mysterio"] += 1
		characters.characterCount["Carnage"] += 1
	elif answer == "latent":
		characters.characterCount["Cyclops"] += 1


def probabilityAnalyser(maxValue):
	maxValue = 0
	if characters.characterCount["Spider-Man"] >= maxValue:
		maxValue = characters.characterCount["Spider-Man"]
	else:
		characters.characterCount.pop("Spider-Man")
	
	print(maxValue)
	if characters.characterCount["Cyclops"] >= maxValue:
		maxValue = characters.characterCount["Cyclops"]
	else:
		characters.characterCount.pop("Cyclops")

	if characters.characterCount["Mysterio"] >= maxValue:
		maxValue = characters.characterCount["Mysterio"]
	else:
		characters.characterCount.pop("Mysterio")

	if characters.characterCount["Carnage"] >= maxValue:
		maxValue = characters.characterCount["Carnage"]
	else:
		characters.characterCount.pop("Carnage")

	#print(characters.characterCount.values())