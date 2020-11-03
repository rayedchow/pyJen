# IMPORTING PACKAGES/MODULES
import log as logger
from learningCore import makeDecision, askQuestion

import matplotlib.pyplot as plt
import json



# MAIN FUNCTION
def main():

	# LOGGING START
	logger.logInit()
	logger.log("Started Latest Logs")

	# Testing Minimalistic ML with Decision Making

	# Setting up data & labels for graph
	data = [0, 0, 0, 0, 0]
	dataLabels = ["Yes", "Maybe", "I have no idea", "Maybe Not", "No"]

	# Looping the decisions
	for i in range(0, 10):
		data[makeDecision(["Yes", "Maybe", "I have no idea", "Maybe Not", "No"], True)] += 1

	# Graphing data
	plt.bar(dataLabels, data)
	plt.savefig("logs/latest.png")

	convo = 1
	while convo == 1:
		convo = askQuestion()



main()
