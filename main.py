from random import randint
from gameComponents import characters, processing
import random

print("------> Welcome to Evan's Marvel Quiz <------")
#generate our random sequence for questioning

#Generating a number sequence
numberSequence = [0, 1, 2, 3]
#had to learn how to do this after the number generator being too complicated. Much simpler
random.shuffle(numberSequence)
print(numberSequence)
#processing.probabilityAnalyser()
for x in range(4):
	pass
	#Asks the question in a random order
	print(numberSequence[x])
	currentQuestion = input(characters.question[numberSequence[x]])
	processing.questionSort(currentQuestion)
	print(characters.spider)
	print(characters.cyclops)
	print(characters.mysterio)
	print(characters.carnage)

#Sort the character count from most to least
maxValue = 0
processing.probabilityAnalyser(maxValue)
#for x in range(4):
	#if characters.characterCount[x] >= maxValue:
		#maxValue = characters.characterCount[x]
	#else:
		#maxValue = maxValue
		#characters.characterCount

print(maxValue)

print("Your character is " + characters.characterCount.keys())