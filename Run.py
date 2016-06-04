import string
import pickle
import time
import threading
import re
from urllib.request import urlopen
from Socket import openSocket,sendMessage,joinRoom,getUser,getMessage
from Settings import CHANNEL,MBALL,COOLDOWNCMD,VERSION
#from pastebin import getChangelog

s=openSocket("#"+CHANNEL)
joinRoom(s)
#w=openSocket("$[whisper]")
#joinRoom(w)
""" INIT
MODOS=["tanook_leduc","aiki_","faiscla","orso5895","vambok","tanook_lebot"]
REGULARS=["tanook_leduc","aiki_","faiscla","orso5895","vambok","tanook_lebot","magicdiner","landulyk","imsouseless","hikarichan73","sednegi","aruthekbr","davissyon","plumeblanche","neg_eggs","reidmercury__","massiste2","ptiteframboise71","rhyouk","les_survivants","perblez60"]
SLAVES=["vambok","landulyk","faiscla","rhyouk","perblez60","piouman"]
UPTIMES={'tanook_leduc':10,'tanook_lebot':10,'vambok':10}
MSGCOUNT={'tanook_leduc':10,'tanook_lebot':10,'vambok':10}
fichier=open("viewers","wb")
pickle.dump([MODOS,REGULARS,SLAVES,UPTIMES,MSGCOUNT],fichier)
fichier.close()
"""
fichier=open("viewers","rb")
gens=pickle.load(fichier)
fichier.close()
MODOS=gens[0]
REGULARS=gens[1]
SLAVES=gens[2]
UPTIMES=gens[3]
MSGCOUNT=gens[4]
""" LVLS
LEVELS={}
for viewer in UPTIMES:
	if viewer in MSGCOUNT:
		LEVELS[viewer]=int((UPTIMES[viewer]/40+MSGCOUNT[viewer]/10)**0.5)
	else:
		LEVELS[viewer]=int((UPTIMES[viewer]/40)**0.5)
"""
def textDelay(msg,delai):
	time.sleep(delai)
	for ligne in msg.split("\n"):
		sendMessage(s,ligne)
	return True
def uptimeUpdate(multiplicateur):
	presentViewers=urlopen("http://tmi.twitch.tv/group/user/"+CHANNEL+"/chatters").read(100000).decode("utf-8")
	if presentViewers.find("\"moderators\": []") > -1:
		presentMods=[]
	else:
		presentMods=presentViewers.split("\"moderators\": [\n      \"")[1]
		presentMods=presentMods.split("\"\n    ],")[0]
		presentMods=presentMods.split("\",\n      \"")
	if presentViewers.find("\"viewers\": []") > -1:
		presentViewers=[]
	else:
		presentViewers=presentViewers.split("\"viewers\": [\n      \"")[1]
		presentViewers=presentViewers.split("\"\n    ]")[0]
		presentViewers=presentViewers.split("\",\n      \"")
	present=presentMods+presentViewers
	if CHANNEL in present:
		for viewer in present:
			if viewer in UPTIMES:
				UPTIMES[viewer]+=multiplicateur
""" LVLS
				if viewer in MSGCOUNT:
					nbMsg=MSGCOUNT[viewer]
				else:
					nbMsg=0
				nextLvl=int((UPTIMES[viewer]/40+nbMsg/10)**0.5)
				if nextLvl > LEVELS[viewer]:
					LEVELS[viewer]=nextLvl
					if viewer not in MODOS:
						sendMessage(s,"Et "+viewer+" atteint le niveau "+str(nextLvl)+" de chien de la casse-ance ! Bravo :)")
"""
			else:
				UPTIMES[viewer]=multiplicateur
		fichier=open("viewers","wb")
		pickle.dump([MODOS,REGULARS,SLAVES,UPTIMES,MSGCOUNT],fichier)
		fichier.close()
		print("Uptimes and msgs updated")
def standbymode():
	global EMOTELIST
	global ouaisCpt
	global ggCpt
	global lastUptimeUpdate
	global lastCommande
	standby=True
	readbuffer=""
	while standby:
		readbuffer+=s.recv(1024).decode('utf-8')
		temp=readbuffer.split("\n")
		readbuffer=temp.pop()
		for line in temp:
			user=getUser(line)
			if user==CHANNEL or user=="vambok":
				actualtime=time.time()
				EMOTELIST=[":)",":(",":D",">(",":|","O_o","B)",":O","<3",":/",";)",":P",";P","R)"]
				data=urlopen("https://twitchemotes.com/api_cache/v2/global.json").read(40000).decode("utf-8")
				data=data.split("\"emotes\":{\"")[1]
				data=data.split("},\"")
				for emoteline in data:
					EMOTELIST.append(emoteline.split("\":{")[0])
#				for user in SEEN:
#					if actualtime-SEEN[user] > 36000:
#						SEEN.pop(user,None)
				for user in PERMITTED:
					if actualtime-PERMITTED[user] > 120:
						PERMITTED.pop(user,None)
				ouaisCpt=0
				ggCpt=0
				lastUptimeUpdate=actualtime
				lastCommande=0
				standby=False
				print("Starting Tanook_Os V"+VERSION+": Hello world!")
			elif line=="PING :tmi.twitch.tv\r":
				s.send("PONG :tmi.twitch.tv\r\n".encode())
PERMITTED={}
#SEEN={}#"vambok":time.time(),"piouman":time.time(),"vutking":time.time(),"landulyk":time.time(),"neg_eggs":time.time(),"pilodermann":time.time(),"faiscla":time.time(),"walhkyng":time.time(),"bloodskysony":time.time(),"massiste2":time.time(),"ptiteframboise71":time.time(),"maflak":time.time(),"death83974":time.time(),"wolfgrey49":time.time(),"khalid_riyadh":time.time(),"kaesor":time.time(),"mathb1709":time.time()}
lastFollow=urlopen("https://api.twitch.tv/kraken/channels/"+CHANNEL+"/follows").read(1000).decode("utf-8")
lastFollow=lastFollow.split("kraken/users/")[1]
lastFollow=lastFollow.split("/follows/")[0]
def checkFollows():
	global lastFollow
	follow=urlopen("https://api.twitch.tv/kraken/channels/"+CHANNEL+"/follows").read(1000).decode("utf-8")
	follow=follow.split("kraken/users/")[1]
	follow=follow.split("/follows/")[0]
	if follow!=lastFollow:
		sendMessage(s,"Merci "+follow+" pour le follow ! Bienvenue parmi les chiens de la casse ! :)")
		lastFollow=follow
readbuffer=""
EMOTELIST=[]
ouaisCpt=0
ggCpt=0
lastUptimeUpdate=time.time()
lastCommande=0
standbymode()
while True:
	readbuffer+=s.recv(1024).decode('utf-8')
	temp=readbuffer.split("\n")
	readbuffer=temp.pop()
#	checkFollows()
	for line in temp:
		actualtime=time.time()
		if actualtime-lastUptimeUpdate > 60:
			nbUpdate=int((actualtime-lastUptimeUpdate)/60)
			uptimeUpdate(nbUpdate)
			lastUptimeUpdate+=nbUpdate*60
		print(line.encode("ascii","ignore"))
		user=getUser(line)
		message=getMessage(line)
		messagelc=message.lower()
		noCommande=False
		cooldown=actualtime-lastCommande
		if user not in MODOS and cooldown < COOLDOWNCMD:
			noCommande=True
		else:
			if messagelc=="!help" or messagelc=="!commands" or messagelc=="!commandlist" or messagelc=="!commandes":
				sendMessage(s,"Ici Tanook_Lebot version bêta ! Je peux vous donner le !planning de la chaîne, les réseaux sociaux (!twitter, !youtube, !discord), les !pb Isaac de Tanook ainsi que les !starters et !mods du jeu, votre !uptime vos !messages et la liste des !modos. Vous pouvez tenter la !roulette, la !8ball et le !love, et j'ai quelques notions de base en modérations. :)")
			elif messagelc=="!ffz":
				sendMessage(s,"Extension www.FrankerFaceZ.com pour avoir les émotes chaloupées !")#goo.gl/ycz20N")
			elif messagelc=="!isaacmods" or messagelc=="!isaacsmods" or messagelc=="!mods":
				sendMessage(s,"Instant-Start : github.com/Zamiell/instant-start-mod ; Jud6s : github.com/Zamiell/jud6s ; Diversity : github.com/Zamiell/diversity-mod")
			elif messagelc=="!ladder":
				sendMessage(s,"Pour vous inscrire au Ladder c'est ici ! : goo.gl/forms/6bhNPqGwyRBfXbTD3")
			elif messagelc=="!diversity":
				sendMessage(s,"Diversity mod download + info: github.com/Zamiell/diversity-mod")
			elif messagelc=="!instantstart" or messagelc=="!instant-start":
				sendMessage(s,"Instant Start mod download + info: github.com/Zamiell/instant-start-mod")
			elif messagelc=="!jud6s" or messagelc=="!judasd6":
				sendMessage(s,"Jud6s mod download + info: github.com/Zamiell/jud6s")
			elif messagelc=="!starters":
				sendMessage(s,"Le guide des starters sur Isaac c'est ici : bit.ly/22lCM6i !")
			elif messagelc=="!srl" or messagelc=="!speedrunslive":
				sendMessage(s,"Pour regarder les races sur SRL allez sur ce site : www.speedrunslive.com/races")# ; Pour participer aux races vous avez un excellent tuto ici : www.youtube.com/watch?v=vOsnV8S81uI")
			elif messagelc=="!discord":
				sendMessage(s,"L'adresse de notre serveur Discord communautaire : discord.gg/0tsKaAs4vaCMwU0y ! Si tu veux venir papoter avec nous !")
#			elif messagelc=="!multitwitch" or messagelc=="!mt" or messagelc=="!multi-twitch":
#				sendMessage(s,"Voici le lien du multi-twitch où vous pouvez suivre la race de MagicDiner en parallèle : www.multitwitch.tv/tanook_leduc/magicdiner")
			elif messagelc=="!planning":
				sendMessage(s,"Tu peux retrouver le planning de la chaîne ici : t.co/GaF8wOJxnv !")
			elif messagelc=="!pb" or messagelc=="!pbs":
				sendMessage(s,"Les PB de Tanook sur TBoI:Afterbirth sont de 9mn02 en 1char et 1h49mn56 en 7char. N'hésites pas à revoir ce dernier ici : www.speedrun.com/run/wzp9jlrm !")
			elif messagelc=="!twitter":
				sendMessage(s,"Pour suivre Tanook sur Twitter c'est ici : www.twitter.com/tanook_leduc !")
			elif messagelc=="!youtube" or messagelc=="!yt":
				sendMessage(s,"Pour voir les VOD de Tanook sur Youtube c'est ici : goo.gl/hxEJqh !")
#			elif messagelc=="!instagram":
#				sendMessage(s,"Pour suivre Tanook sur Instagram c'est ici : instagram.com/tanook_leduc !")
#			elif messagelc=="!google+" or messagelc=="!g+":
#				sendMessage(s,"Pour suivre Tanook sur Google+ c'est ici : goo.gl/KL6Ixj !")
			elif messagelc=="!facebook" or messagelc=="!fb":
				sendMessage(s,"Check this out! www.facebook.com/patricksebastienofficiel Kappa")
			elif messagelc=="!twitch":
				sendMessage(s,"Pour voir Tanook en live sur Twitch... wait, that's not funny ! FailFish")
			elif messagelc=="!myuptime" or messagelc=="!uptime" or messagelc=="!ut":
				if user in UPTIMES:
					sendMessage(s,user+" a été présent "+str(int(UPTIMES[user]/6)/10)+" heures sur le live ! (depuis le 21/5)")
			elif messagelc=="!mymessages" or messagelc=="!messages" or messagelc=="!mymess" or messagelc=="!msgs":
				if user in MSGCOUNT:
					sendMessage(s,user+" a écrit "+str(MSGCOUNT[user])+" messages sur le live ! (depuis le 21/5)")
#			elif messagelc=="!mylevel" or messagelc=="!level" or messagelc=="!lc":
#				if user in LEVELS:
#					sendMessage(s,user+" est un chien de la casse de niveau "+str(LEVELS[user])+" !")
			elif messagelc=="!modos" or messagelc=="!modérateurs" or messagelc=="!moderateurs":
				sendMessage(s,"Le chat est géré avec justesse par "+', '.join(list(set(MODOS)-set(["tanook_leduc","tanook_lebot"])))+" et moi même. Ne testez pas trop notre humour vous pourriez le regretter Keepo")
#			elif messagelc=="!regulars" or messagelc=="!reguliers" or messagelc=="!réguliers":
#				sendMessage(s,"J'ai plein de copains ! "+', '.join(list(set(REGULARS)-set(MODOS)))+" et mes collègues modos débizou à vous :D Les autres j'ai hâte de faire votre connaissance :)")
#			elif messagelc=="!slaves":
#				sendMessage(s,"L'Emergent. Ce fier vaisseau de FTL dirigé d'une main de fer par dame Tanook, abrite un équipage aussi vaillant que couard, aussi efficace que fainéant, aussi dévoué qu'en manque d'oxygène... j'ai nommé : "+', '.join(SLAVES))
			elif messagelc=="!boss":
				sendMessage(s,"Ici c'est Tanook le boss ! SwiftRage")
			elif messagelc=="!patron":
				sendMessage(s,"Et le patron... c'est Tanook aussi ! SwiftRage")
			elif messagelc=="!papa" or messagelc=="!chef" or messagelc=="!alpha" or messagelc=="!proprio" or messagelc=="!dieu" or messagelc=="!général" or messagelc=="!roi" or messagelc=="!reine" or messagelc=="!commandant" or messagelc=="!toutpuissant":
				sendMessage(s,"Bon faudrait pas pousser hein Kappa !boss suffit !")
#			elif messagelc=="!aiki_" or messagelc=="!aiki":
#				sendMessage(s," ")
#			elif messagelc=="!faiscla":
#				sendMessage(s," ")
#			elif messagelc=="!orso5895" or messagelc=="!orso":
#				sendMessage(s," ")
#			elif messagelc=="!vambok":
#				sendMessage(s," ")
			elif (messagelc=="!standby" or messagelc=="!sleep") and (user=="vambok" or user==CHANNEL):
				sendMessage(s,"Sleep mode activated. Memory dump: \"Bonne nuit les amis !\"")
				standbymode()
			elif messagelc=="!bordel" and user in MODOS:
				sendMessage(s,"/slowoff")
			elif messagelc=="!uptimes" and user in MODOS:
				uptimesMessage=""
				for viewerUt in UPTIMES:
					uptimesMessage+=viewerUt+":"+str(UPTIMES[viewerUt])+", "
				sendMessage(s,uptimesMessage[:-2])
			elif messagelc=="*ouais*":
				if ouaisCpt > 1:
					sendMessage(s,"*ouais*")
					ouaisCpt=0
				else:
					ouaisCpt+=1
			elif messagelc=="!roulette":
				tirage=int((actualtime % 1)*12)
				if user=="orso5895":
					sendMessage(s,"/me voit Orso pointer son gros Remington sur lui. \"Ne me teste pas tas de ferraille !\" WutFace")			
				elif user in MODOS:
					sendMessage(s,"/me n'oserait pas pointer une arme à feu sur "+user+".")
				elif user in REGULARS:
					sendMessage(s,"/me lève lentement le Remington d'Orso vers la tempe de "+user+". Sorry bro but you asked for it...")
					if tirage==0:
						roulette="/timeout "+user+" 5\nNoooooooon ! "+user+" est retrouvé étendu sur le sol :("
					elif tirage==1:
						roulette="La détente est pressée mais du sang séché encrasse le Remington. "+user+" survit miraculeusement ! \\o/"
					else:
						roulette="La détente est pressée, le Remington émet un \"clic\". "+user+" a survécu ! Ouf !"
					t=threading.Thread(target=textDelay(roulette,5))
					t.start()
				else:
					sendMessage(s,"/me place le Remington d'Orso sur la tempe de "+user+".")
					if tirage==0:
						roulette="/timeout "+user+" 10\nBOOM ! "+user+" est retrouvé étendu sur le sol"
					elif tirage==1:
						roulette="La détente est pressée mais du sang séché encrasse le Remington. "+user+" survit miraculeusement !"
					else:
						roulette="La détente est pressée, le Remington émet un \"clic\". "+user+" a survécu !"
					t=threading.Thread(target=textDelay(roulette,5))
					t.start()
#			elif messagelc=="!truc": currentsong nextsong songlist wrongsong skipsong%...
#				sendMessage(s,"truc")
			else:
				noCommande=True
		if noCommande: # symbols spam
			if user not in MODOS and ((re.search(":\/\/[a-zA-Z1-9]{2,}\.[a-zA-Z1-9]{2,}",message) is not None) or (re.search("[a-zA-Z1-9]{2,}\.[a-zA-Z1-9]{3,}\.[a-zA-Z1-9]{2,}",message) is not None) or (re.search("[a-zA-Z1-9]{2,}\.[a-zA-Z1-9]{2,}\/[a-zA-Z1-9]+",message) is not None) or (re.search("[a-zA-Z1-9]{3,}@[a-zA-Z1-9]{3,}\.[a-zA-Z1-9]{2,}",message) is not None)):
				if user not in PERMITTED:
					textDelay("/timeout "+user+" 1",0.5)
#					sendMessage(s,"/timeout "+user+" 1")
					sendMessage(s,"C'est quoi ça ? Encore un site 18+ ? SwiftRage")
					continue
				else:
					permitExpire=actualtime-PERMITTED[user]-120
					PERMITTED.pop(user,None)
					if permitExpire > 0:
						textDelay("/timeout "+user+" 1",0.5)
#						sendMessage(s,"/timeout "+user+" 1")
						sendMessage(s,"Ta permission est expirée depuis "+permitExpire+" secondes ! RT")
						continue
			emoteSpam=0
			messageSansEmotes=message
			for emote in EMOTELIST:
				if emote in message:
					emoteSpam+=message.count(emote)
					messageSansEmotes=messageSansEmotes.replace(emote,"")
			if user not in MODOS and emoteSpam > 3:
				textDelay("/timeout "+user+" 1",0.5)
#				sendMessage(s,"/timeout "+user+" 1")
				sendMessage(s,"Du calme avec les émotes, tu t'es cru sur MSN ? SwiftRage")
				continue
			if (user not in MODOS) and (re.search("([A-Z]{2,}.*){3}",messageSansEmotes) is not None) and ((len(messageSansEmotes) > 20 and user not in REGULARS) or len(messageSansEmotes) > 30) and (messageSansEmotes==messageSansEmotes.upper()):
				textDelay("/timeout "+user+" 1",0.5)
#				sendMessage(s,"/timeout "+user+" 1")
				sendMessage(s,user+" ARRETE DE CRIER ! SwiftRage")
				continue
			if (user not in MODOS) and (re.search("[a-zA-Z]{2}",messageSansEmotes) is None) and (len(messageSansEmotes) > 10):
				textDelay("/timeout "+user+" 1",0.5)
				sendMessage(s,"@"+user+" J'ai rien compris Kappa")
				continue
""" greetings
			if user[:13]!="tmi.twitch.tv" and user!=CHANNEL and user!="vambok":
				if user not in SEEN:
					if user in MODOS:
						sendMessage(s,"@"+user+" Hey collègue ! o/")
					elif user in REGULARS:
						sendMessage(s,"Salut "+user+" :D")
					else:
						sendMessage(s,"Bonjour "+user+" !")
				else:
					if actualtime-SEEN[user] > 7200:
						if user in MODOS:
							sendMessage(s,"@"+user+" re :)")
						elif user in REGULARS:
							sendMessage(s,"Wb "+user+" ^^")
						else:
							sendMessage(s,"Re "+user+" !")
				SEEN[user]=actualtime
"""
			commande=message.split(" ",1)
			if len(commande)<2:
				commande.append("")
			commande[0]=commande[0].lower()
			if user in MODOS or cooldown >= COOLDOWNCMD:
				noCommande=False
				if commande[0]=="!2balls":
					sendMessage(s,"La commande c'est !8ball petit malin Kappa")
				elif commande[0]=="!8ball" and commande[1]!="":
					tirage=int((actualtime % 1)*len(MBALL))
					sendMessage(s,MBALL[tirage])
				elif commande[0]=="!love":
					if commande[1][0]=="@":
						paramLove=commande[1][1:].lower()
					else:
						paramLove=commande[1].lower()
					if paramLove=="tanook_lebot":
						sendMessage(s,"Stupide humain, les robots ne connaissent pas l'amour ! BibleThump")
					elif paramLove==CHANNEL:
						sendMessage(s,"Il y a [IntegerOverflowError(CWE-190)]% d'amour entre "+user+" et Tanook Leduc !")
					else:
						if paramLove in MODOS or paramLove=="aiki" or paramLove=="orso":
							loveOffset=50
						elif paramLove in REGULARS:
							loveOffset=10
						else:
							loveOffset=0
						tirage=100-int((actualtime % 1)*(101-loveOffset))
						sendMessage(s,"Il y a "+str(tirage)+"% d'amour entre "+user+" et "+commande[1]+" !")
				else:
					noCommande=True
			if noCommande:
				if commande[0][:13]=="@tanook_lebot":
					tirage=int((actualtime % 1)*2)
					if user==CHANNEL and commande[1][:7]=="attaque":
#						if tirage==0:
						sendMessage(s,"/me se jette furieusement sur l'impie et le déchiquette de ses griffes d'acier accérées.")
#						else:
#							sendMessage(s,"/me empoigne fermement le scélérat par le col et lui fait manger 2kg de boulgour.")
					elif user in MODOS:
						if tirage==0:
							sendMessage(s,"C'est pas faux")
						else:
							sendMessage(s,"Je vous crois")
					else:
						if tirage==0:
							sendMessage(s,"@"+user+" les robots ne répondent pas aux @mentions. Je vais donc simplement t'ignorer B)")
						else:
							sendMessage(s,"Quelqu'un a dit quelque chose ? Ah non rien, il y a du vent B)")
				elif user==CHANNEL:
					if commande[0]=="!addmodo":
						commande[1]=commande[1].lower()
						if commande[1] in MODOS:
							sendMessage(s,commande[1]+" est déjà modo ! @"+commande[1]+" Tanook t'aime bien Kappa")
						else:
							MODOS.append(commande[1])
							fichier=open("viewers","wb")
							pickle.dump([MODOS,REGULARS,SLAVES,UPTIMES,MSGCOUNT],fichier)
							fichier.close()
							sendMessage(s,"All hail to "+commande[1]+" ! o// o_")
					elif commande[0]=="!removemodo":
						commande[1]=commande[1].lower()
						if commande[1] in MODOS:
							MODOS.remove(commande[1])
							fichier=open("viewers","wb")
							pickle.dump([MODOS,REGULARS,SLAVES,UPTIMES,MSGCOUNT],fichier)
							fichier.close()
							sendMessage(s,"Adieu "+commande[1]+" BibleThump")
						else:
							sendMessage(s,"Y a pas de modo nommé "+commande[1]+". RT")
					elif commande[0]=="!addslave":
						commande[1]=commande[1].lower()
						if commande[1] in SLAVES:
							sendMessage(s,commande[1]+" est déjà esclave à bord de l'Emergent ! Dois-je l'envoyer à la baille ? Kappa")
						else:
							SLAVES.append(commande[1])
							fichier=open("viewers","wb")
							pickle.dump([MODOS,REGULARS,SLAVES,UPTIMES,MSGCOUNT],fichier)
							fichier.close()
							sendMessage(s,"@"+commande[1]+" prépare toi à mourir asphixié ! EleGiggle")
					elif commande[0]=="!removeslave":
						commande[1]=commande[1].lower()
						if commande[1] in SLAVES:
							SLAVES.remove(commande[1])
							fichier=open("viewers","wb")
							pickle.dump([MODOS,REGULARS,SLAVES,UPTIMES,MSGCOUNT],fichier)
							fichier.close()
							sendMessage(s,"Plus besoin de "+commande[1]+". Et hop dans l'espace !")
						else:
							sendMessage(s,commande[1]+" était à bord clandestinement apparemment...")
				elif user in MODOS:
					if commande[0]=="!addregular":
						commande[1]=commande[1].lower()
						if commande[1] in REGULARS:
							sendMessage(s,"Mais je connais déjà "+commande[1]+" ! o/ "+commande[1])
						else:
							REGULARS.append(commande[1])
							fichier=open("viewers","wb")
							pickle.dump([MODOS,REGULARS,SLAVES,UPTIMES,MSGCOUNT],fichier)
							fichier.close()
							sendMessage(s,"@"+commande[1]+" Chouette un nouvel ami pour moi ! :D")
					elif commande[0]=="!removeregular":
						commande[1]=commande[1].lower()
						if commande[1] in REGULARS:
							REGULARS.remove(commande[1])
							fichier=open("viewers","wb")
							pickle.dump([MODOS,REGULARS,SLAVES,UPTIMES,MSGCOUNT],fichier)
							fichier.close()
							sendMessage(s,"@"+commande[1]+" Tu m'as déçu :|")
						else:
							sendMessage(s,"C ki "+commande[1]+" ? o_O")
					elif commande[0]=="!permit":
						commande[1]=commande[1].lower()
						if commande[1] in MODOS:
							sendMessage(s,commande[1]+" a déjà tous les droits ;)")
						else:
							PERMITTED[commande[1]]=actualtime
#							sendMessage(s,"@"+commande[1]+" dans sa grande bôônté "+user+" te donne 2mn de permission pour un lien.")
					elif commande[0]=="!uptime" or commande[0]=="!ut":
						if commande[1].lower() in UPTIMES:
							sendMessage(s,"/w "+user+" "+commande[1]+" a été présent "+str(int(UPTIMES[commande[1].lower()]/6)/10)+" heures ("+str(UPTIMES[commande[1].lower()])+"mn) sur le live ! (21/5)")
					elif commande[0]=="!messages" or commande[0]=="!msgs":
						if commande[1].lower() in MSGCOUNT:
							sendMessage(s,"/w "+user+" "+commande[1]+" a écrit "+str(MSGCOUNT[commande[1].lower()])+" messages sur le live ! (21/5)")
					elif commande[0]=="!to" or commande[0]=="!ko":
						params=commande[1].split(" ",1)
						if len(params) > 1:
							sendMessage(s,"/timeout "+params[0]+" "+int(params[1]))
						else:
							sendMessage(s,"/timeout "+params[0]+" 1")
					elif commande[0]=="!ban" or commande[0]=="!rekt" or commande[0]=="!kill":
						sendMessage(s,"/ban "+commande[1])
					elif commande[0]=="!unban" or commande[0]=="!revive":
						sendMessage(s,"/unban "+commande[1])
					elif commande[0]=="!calm" or commande[0]=="!calme" or commande[0]=="!calmos" or commande[0]=="!chut":
						params=commande[1].split(" ",1)
						if len(params) > 1:
							sendMessage(s,"/slow "+int(params[1]))
						else:
							sendMessage(s,"/slow 10")
						tcalm=threading.Thread(target=textDelay("/slowoff",int(params[0])))
						tcalm.start()
#				elif commande[0]=="!truc": songrequest
#					sendMessage(s,"truc")
				if line=="PING :tmi.twitch.tv\r":
					s.send("PONG :tmi.twitch.tv\r\n".encode())
				elif messagelc.find("t'es pas là") > -1 or messagelc.find(" t pas là") > -1:
					sendMessage(s,"Mais T où ? O_o")
				elif messagelc.find("mais t'es où ?") > -1 or messagelc.find("mais t'es ou ?") > -1 or messagelc.find("mais t où ?") > -1 or messagelc.find("mais t ou ?") > -1 or messagelc.find(" mé t où ?") > -1 or messagelc.find(" mé t ou ?") > -1 or messagelc=="mé t où ?" or messagelc=="mé t ou ?":
					sendMessage(s,"Pas là !")
				if messagelc[:2]=="gg":
					if ggCpt > 1:
						sendMessage(s,"GG !")
						ggCpt=0
					else:
						ggCpt+=1
#				if "truc" in message:
#					sendMessage(s,"truc")
				if user in MSGCOUNT:
					MSGCOUNT[user]+=1
				else:
					MSGCOUNT[user]=1
		if not noCommande:
			lastCommande=actualtime