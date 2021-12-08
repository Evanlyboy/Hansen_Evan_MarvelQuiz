from gameComponents import characters

def questionSort(answer):
	if answer == "good":
		characters.spider += 1
		characters.cyclops += 1
	elif answer == "bad":
		characters.mysterio += 1
		characters.carnage += 1
	elif answer == "yes":
		characters.spider += 1
		characters.cyclops += 1
	elif answer == "no":
		characters.mysterio += 1
		characters.carnage += 1
	elif answer == "calm":
		characters.spider += 1
		characters.mysterio += 1
	elif answer == "erratic":
		characters.cyclops += 1
		characters.carnage += 1
	elif answer == "acquired":
		characters.spider += 1
		characters.mysterio += 1
		characters.carnage += 1
	elif answer == "latent":
		characters.cyclops += 1


def probabilityAnalyser(maxValue):
	if characters.characterCount["spider"] >= maxValue:
		maxValue = characters.characterCount["spider"]
	elif
		characters.characterCount.pop("spider")
	
	if characters.characterCount["cyclops"] >= maxValue:
		maxValue = characters.characterCount["cyclops"]
	elif
		characters.characterCount.pop("cyclops")

	if characters.characterCount["mysterio"] >= maxValue:
		maxValue = characters.characterCount["mysterio"]
	elif
		characters.characterCount.pop("mysterio")

	if characters.characterCount["carnage"] >= maxValue:
		maxValue = characters.characterCount["carnage"]
	elif
		characters.characterCount.pop("carnage")

	print(characterCount.keys())