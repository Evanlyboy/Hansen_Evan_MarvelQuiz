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
	currentQuestion = input(characters.question[numberSequence[x]])
	processing.questionSort(currentQuestion)

#Sort the character count from most to least
maxValue = 0
processing.probabilityAnalyser(maxValue)

#If there is more than one character left in the list somehow, randomly get rid of one to have one character to present to the player
if len(characters.characterCount) > 1:
	characters.characterCount.popitem()

for key, value in characters.characterCount.items() :
    print ("Your character is " + key)