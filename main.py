from random import randint
from gameComponents import characters, processing
import random
import time

#This was a doozy to figure out, wowie. Much frustration

print("------> Welcome to Evan's Marvel Quiz <------")
print("You there...in the shadows...I cannot see before me but I sense your presence. Who are you?")
time.sleep(2)
print("...")
time.sleep(2)
print("Ah, I cannot see nor hear. But I can read your mind. Tell me...")
print("")
time.sleep(3)
#generate our random sequence for questioning
#Generating a number sequence
numberSequence = [0, 1, 2, 3]
#had to learn how to do this after the number generator being too complicated. Much simpler
random.shuffle(numberSequence)
for x in range(4):
	pass
	#Asks the question in a random order
	currentQuestion = input(characters.question[numberSequence[x]])
	print("")
	print("...")
	processing.questionSort(currentQuestion)
	print("")
	time.sleep(2)
	print(characters.characterCount)



#Sort the character count from most to least
maxValue = 0
processing.probabilityAnalyser(maxValue)

#If there is more than one character left in the list somehow, randomly get rid of one to have one character to present to the player
if len(characters.characterCount) > 1:
		characters.characterCount.popitem()

for key, value in characters.characterCount.items() :
    print ("You are..." + key)