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