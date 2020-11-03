# IMPORTING PACKAGES/MODULES
from os.path import isfile
from time import strftime, localtime
from os import remove, rename

# LOGGER
def log(log):
	logs.write("\n{" + strftime("%H:%M:%S", localtime()) + "} " + log + ";")

# LOGGING INITIALIZER
def logInit():

	# MANAGING PREVIOUS LOGS
	if isfile("logs/latest.log"):

		# GETTING DATA FROM PREVIOUS LATEST LOG
		prevLogs = open("logs/latest.log", "r").read()

		# CREATING NEW LOG FILE FOR PREVIOUS LATEST LOG
		open("logs/past/" + prevLogs.split(" - LOG DATE")[0] + ".log", "w").write(prevLogs)
		open("logs/latest.log", "w").write("")
	
		if isfile("logs/latest.png"):
		
			# GETTING DATA FROM PREVIOUS LATEST IMG
			rename("logs/latest.png", "logs/past/" + prevLogs.split(" - LOG DATE")[0] + ".png")



	# STARTING LOGS
	global logs
	logs = open("logs/latest.log", "a")
	logs.write(strftime("%Y-%m-%d-%H-%M-%S") + " - LOG DATE")
