# IMPORTING PACKAGES/MODULES
from log import log
from random import randrange
import json


# Conversation Data for Machine Learning Algorithms
conversation = {
	"questionData": {
		"amount": 0,
		"list": []
	}
}


# Decision Maker
def makeDecision(decisions, returnInt):

	decision = randrange(0, len(decisions))
	log("Made decision: '" + decisions[decision] + "'")

	if returnInt:
		return decision
	else:
		return decisions[decision]



# Machine Learning QA Algorithm
def askQuestion():

	# Initializing Module Data
	moduleJSON = json.loads(open("modules/moduleDay.json", "r").read())
	moduleQuestion = makeDecision(moduleJSON["moduleQuestion"], False) + "?"
	moduleData = json.loads(open("modules/moduleData.json", "r").read())



	log("Asked Question: '" + moduleQuestion + "'")

	# Using Header Keywords Depending on Conversation Data	
	if conversation["questionData"]["amount"] == 0:
		response = input(makeDecision(moduleData["conversationStartKeywords"], False) + ", " + moduleQuestion + "\n")
	else:
		response = input(makeDecision(moduleData["responseKeywords"], False) + moduleQuestion + "\n")
	
	log("Response: '" + response + "'")

	# Updating Conversation Data
	conversation["questionData"]["amount"] += 1
	conversation["questionData"]["list"].append(
		{
			"module": moduleQuestion,
			"response": response
		}
	)



def getModule():
	
	# Initializing Module Data & List
	moduleData = json.loads(open("modules/moduleData.json", "r").read())
	moduleList = moduleData["modules"]

	# Filtering out all used modules
	for question in conversation["questionData"]["list"]:
		list(filter((question["module"]).__ne__, moduleList))
	
	# Returning Random Module out of Unused Modules
	if moduleList != []:
		return makeDecision(moduleList, False)
	
	# IF moduleList is empty (If all modules were used)
	return None
