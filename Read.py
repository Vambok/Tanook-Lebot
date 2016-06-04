import string

def getUser(line):
	separate=line.split(":",2)
	user=separate[1].split("!",1)[0]
	return user
def getMessage(line):
	separate=line.split(":",2)
	if len(separate) > 2:
		message=separate[2].rstrip()
	else:
		message=""
	return message