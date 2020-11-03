# IMPORTING PACKAGES/MODULES
from log import log
from random import randrange
import json


moduleData = json.loads(open("modules/moduleData.json", "r").read())

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
	module = getModule()
	if module == None:
		print('Jen: Was nice meeting you!')
		return 0

	moduleJSON = json.loads(open("modules/module" + module + ".json", "r").read())
	moduleQuestion = makeDecision(moduleJSON["moduleQuestion"], False) + "?"



	log("Used module: '" + module + "'" + " with question '" + moduleQuestion + "''")

	# Using Header Keywords Depending on Conversation Data
	if conversation["questionData"]["amount"] == 0:
		response = input("Jen: " + makeDecision(moduleData["conversationStartKeywords"], False) + ", " + moduleQuestion + "\nYou: ")
	else:
		response = input("Jen: " + makeDecision(moduleData["responseKeywords"], False) + ", " + moduleQuestion + "\nYou: ")

	log("Response: '" + response + "'")

	# Updating Conversation Data
	conversation["questionData"]["amount"] += 1
	conversation["questionData"]["list"].append(
		{
			"module": module,
			"response": response
		}
	)
	return 1



def getModule():

	# Initializing Module List
	moduleList = moduleData["modules"]

	# Filtering out all used modules
	for question in conversation["questionData"]["list"]:
		if question["module"] in moduleList:
			moduleList.remove(question["module"])

	# Returning Random Module out of Unused Modules
	if moduleList != []:
		return makeDecision(moduleList, False)

	# IF moduleList is empty (If all modules were used)
	return None
