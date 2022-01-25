import urllib.request
import json
import os
import urllib.request
import json


os.system('clear')

banner = ("""
\033[34m 

\t▄▀▀ █▀▄ ▀▄░▄▀ ▀ █▄░█ █▀ ▄▀▄ 
\t░▀▄ █░█ ░░█░░ █ █░▀█ █▀ █░█ 
\t▀▀░ █▀░ ░░▀░░ ▀ ▀░░▀ ▀░ ░▀░ 
		
		 	        [1.0.0v]



\033[33m [\033[36m1\033[33m]\033[36m - Пробив по номеру телефона

\033[33m [\033[36m2\033[33m]\033[36m - Пробив по IP

\033[33m [\033[36m0\033[33m]\033[36m - Выход

________________________________________________
""")
print(banner)
number = int(input("\n\n\n \033[33m[\033[31m!\033[33m] \033[36mВыберите вариант --->\033[32m "))
if number==1:
	phone = input("\n \033[33m[\033[32m+\033[33m] Введите телефон без + (пример: 7123456789):\033[32m ")
	getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone
	try:
	    infoPhone = urllib.request.urlopen( getInfo )
	except:
	    print( "\n[!] - Нет такого телефона - [!]\n" )
	infoPhone = json.load( infoPhone )
	print( u"Номер сотового --->", "+" + phone )
	print( u"Страна ---> ", infoPhone["country"]["name"] )
	print( u"Регион ---> ", infoPhone["region"]["name"] )
	print( u"Округ ---> ", infoPhone["region"]["okrug"] )
	print( u"Оператор ---> ", infoPhone["0"]["oper"] )
	print( u"Часть света ---> ", infoPhone["country"]["location"] )
	
	
	number = int(input("\n\n\n \033[33m[\033[31m!\033[33m] \033[36mВыберите номер --->\033[32m "))



#----------------------------------------------------

elif number == 2:
	getIP = input("\n \033[33m[\033[32m+\033[33m]\033[33m Введите IP --> \033[32m")
	url = "https://ipinfo.io/" + getIP + "/json"
	
	try:
	    getInfo = urllib.request.urlopen( url )
	
	except:
	    print( "\n\033[32m[\033[31m!\033[32m]\033[31m - Такого IP не существует! Перезапустите программу и введите правильный. - \033[32m[\033[31m!\033[32m]\n" )
	
	infoList = json.load(getInfo)
	
	def whoisIPinfo(ip):
	
	    try:
	
	        myComand = "whois " + getIP
	        whoisInfo = os.popen( myComand ).read()
	        return whoisInfo
	
	    except:
	
	        return "\n [!] -- Error -- [!] \n"

     
	print( "-" * 60 )
	


	print("\033[32mIP: ", infoList["ip"] )
	print( "Регион: ", infoList["region"] )
	print( "Страна: ", infoList["country"] )
	print( "Название хоста: ", infoList["hostname"] )
	print( "Координаты: ", infoList["loc"])
	
	print( "-" * 60 )
	
	print( "-" * 60)
	

elif number == 0:
	os.system('clear')
	quit()

# Код защищён авторскими правами. Просьба не тыбзить
