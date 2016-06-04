import string
import socket
from Settings import HOST,PORT,PASS,NICK,CHANNEL

def openSocket(adresse):
	s=socket.socket()
	s.connect((HOST,PORT))
	s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
	s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
	s.send("JOIN {}\r\n".format(adresse).encode("utf-8"))
	return s
def sendMessage(s,message):
	messageTemp="PRIVMSG #"+CHANNEL+" :"+message
	s.send("{}\r\n".format(messageTemp).encode("utf-8"))
	print(bytes("Sent: "+messageTemp,"ascii","ignore"))

#Initialize.py
def joinRoom(s):
	readbuffer=""
	Loading=True
	while Loading:
		readbuffer=readbuffer+s.recv(1024).decode('utf-8')
		temp=readbuffer.split("\n")
#		temp=string.split(readbuffer,"\n")
		readbuffer=temp.pop()
		for line in temp:
			print(line)
			Loading=loadingComplete(line)
def loadingComplete(line):
	if("End of /NAMES list" in line):
		return False
	else:
		return True

#Read.py
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