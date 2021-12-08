#For initalizing our characters and questions
spider = ["acquired", "calm", "social", "good"]
cyclops = ["latent", "erratic", "social", "good"]
mysterio = ["aquired", "calm", "isolated", "bad"]
carnage = ["acquired", "erratic", "isolated", "bad"]

characters = ["spider-man", "cyclops", "mysterio", "carnage"]

question = {
	0: "Is your character's power latent or acquired?",
	1: "What is your character's temperament: Calm or Erratic?",
	2: "Does your character have a good social life? Yes or No :",
	3: "Is your character good or bad?"
}

def questionAsk (number):

	question[number]
	print(question)