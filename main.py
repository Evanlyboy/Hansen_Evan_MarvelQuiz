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

for x in range(4):
	pass
	#Asks the question in a random order
	print(numberSequence[x])
	currentQuestion = input(characters.question[numberSequence[x]])
	processing.questionSort(currentQuestion)


#Sort the character count from most to least
characters.characterCount.sort()
print("Your character is " + characters.characterCount(0))