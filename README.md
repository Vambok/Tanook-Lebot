### Tanook Lebot
Source code of a twitch chat bot for Tanook Leduc

### Changelog:
##### 0.1 (infdev):
>**+Run.py  
+Socket.py  
+Settings.py  
+Initialize.py  
+Read.py**

##### 0.2 (indev):
>Changed all "string.split(str,"\n")" by "str.split("\n")" to match Python 3.5  
Changed server string request to "str.format(elmnt).encode("utf-8")" to match Python 3.5

##### 0.3 (indev):
>**Read.py:** +"if len(separate) > 2:" to deal with server pings  
**+viewers.py**

##### 1.0 (command update):
>**Run.py:** +!discord ; +!planning ; +emote spam handling ; +link handling, +!permit ; +!love ; +!boss, +!patron, +!papa ; +!roulette, +!love, +!8ball, +!2balls ; +"\*ouai\*" count and answer ; +!pb ; +!twitter, +!youtube, +!instagram, +!g+, +!twitch, +!facebook ; +!modos, +!addmodo, +!removemodo ; +!regular, +!addregular, +!removeregular ; +!slave, +!addslave, +!removeslave  
**Settings.py:** +MBALL  
**-viewers.py  
+viewers**

##### 1.1 (moderation update):
>**Run.py:** +response to "@tanook_lebot" ; +caps handling ; -response to "you suck" ; +!ban, +!unban, +!calm, +!bordel ; +!help / *commands are case insensitive ; emergency fix of caps and link handling*

##### 1.2 (greeting update):
>**Run.py:** +!mt ; +seen handling, +greeting, +"re"ing / *-!g+ ; -!instagram ; emote spam to 3,3 instead of 2,4 ; fixed "!love @tanook_lebot"*  
**Settings.py:** +special MBALL answer

##### 1.3 (uptime update):
>**Run.py:** +uptime handling, +uptimeUpdate, +myuptime and !uptimes ; +"Mais T où ? O\_o" and "Pas là !" answer ; +"gg" count and answer ; +mod specific answer to @tanook\_lebot ; +messages count and +!messages ; +!starters / *fixed console printing ; fixed caps handling ; fixed !uptime to minute based ; merged lists SEEN/SEENTS and PERMITTED/PERMITTS to dictionaries ; -text answer to !permit ; !help updated ; fixed uptimeUpdate when a category is empty*

##### 1.4 (isaac update):
>**Run.py:** +isaacmods ; +!instantstart ; +!jud6s ; +!diversity ; +!uptime[] ; +!messages[] ; +!srl ; +"@tanook\_lebot attaque" ; +variable answers to "@tanook\_lebot" / *updated !uptime and !messages with starting date ; !help updated and simplified ; handle null or multi-case command[1] ; -"http://" in URLs ; -greeting CHANNEL ; +uptimeUpdate console notice*

##### 1.4.1 (emergency patch):
>**Run.py:** -!regulars / *!help updated*

##### 1.5 (cooldown update):
>**Run.py:** +commands cooldown ; grouped moderation commands by permission  
**Settings.py:** +COOLDOWNCMD

##### 1.5.1 (pre-whisp patch):
>**Run.py:** bases of whisp handling via multiple sockets ; -!slaves / *!starters updated*  
**Socket.py:** +"adresse" arg to openSocket

##### 1.5.2 (emotes patch):
>**Run.py:** -SRL tutorial in !srl ; caps limit increased to 30 ; +0.5s timeout delay to handle twitch message display delay / *now correctly handle emote spam ; full caps with emote handling*

##### 1.5.3 (adjust patch):
>**Run.py:** Tanook list of regulars set ; caps limit to 30 for regular or 20 ; uptimeUpdate running only if CHANNEL is online and corrected UPTIME values

##### 1.6 (standby update):
>**Run.py:** +standby mode ; lengthened "re"ing delay to 2h / *PERMITTED->dictionary*  
**Settings.py:** +version number  
**+changelog.txt**

##### 1.6.1 (moderation patch):
>**Run.py:** +!ffz / *+smileys to handled emotes ; fixed case of "@tanook\_lebot," ; fixed some moderation skills broken by 1.6*  
**Settings.py:** COOLDOWNCMD set to 30 instead of 60

##### 1.6.2 (ascii patch):
>**Run.py:** +handling of special char and ascii spam (every message>10 without 2[a-zA-Z])

##### 1.6.3 (ungreeting patch):
>**Run.py:** -seen handling, -greeting, -"re"ing / *+!changelog*  
**+pastebin.py**

##### 1.7 (follows update):
>**Run.py:** +!ladder ; +checkFollows, +answer to follows / *-booting message from standby mode ; fixed link handling and added e-mail handling*

##### 1.7.1 (follows patch):
>**Run.py:** / *-checkFollows until it works fine ; fixed some special !love cases*

##### 1.8 (levelling update):
>**Run.py:** +-levelling system based on uptimes and messages ; +-!lc ; put project on Github ; merged Socket.py, Initialize.py and Read.py / *!ut and !msgs now mention the user ; -!changelog*  
**-Initialize.py  
-Read.py  
-pastebin.py**

##### 1.8.1 (warcraft patch):
>**Run.py:** +!spotify / *+!alliance +!horde +!splits*