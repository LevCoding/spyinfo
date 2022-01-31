import os
import json
from shutil import get_terminal_size
import urllib.request
from rich import print

os.system('clear')


terminal_size = list(get_terminal_size())

print(f"""[blue]

\t▄▀▀ █▀▄ ▀▄░▄▀ ▀ █▄░█ █▀ ▄▀▄ 
\t░▀▄ █░█ ░░█░░ █ █░▀█ █▀ █░█ 
\t▀▀░ █▀░ ░░▀░░ ▀ ▀░░▀ ▀░ ░▀░ 

		 	        [v1.0.2]

[/blue]
[cyan]
[yellow][[cyan]1[/cyan]][/yellow] - Пробив по номеру телефона\n
[yellow][[cyan]2[/cyan]][/yellow] - Пробив по IP\n
[yellow][[cyan]3[/cyan]][/yellow] - Инструкция\n
[yellow][[cyan]4[/cyan]][/yellow] - Что нового?\n
[yellow][[cyan]5[/cyan]][/yellow] - Купить чашечку кофе разработчику\n
[yellow][[cyan]0[/cyan]][/yellow] - Выход
[/cyan]
{"—" * terminal_size[0]}
""")


def phone_data(phone):
	get_info = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone
	try:
	    info_phone = urllib.request.urlopen(get_info)
	except:
	    print("\n[!] - Нет такого телефона - [!]\n" )
	
	phone_info = json.load(info_phone)
	
	print('—' * (terminal_size[0] // 2))
	print(f"""
[white]Номер сотового --->[/white] [green]+{phone}
[white]Страна --->[/white] {phone_info['country']['name']}
[white]Оператор --->[/white] {phone_info['0']['oper']}
[white]Часть света --->[/white] {phone_info['country']['location']} [/green]
""", '—' * (terminal_size[0] // 2), '\n', sep="")

def ip_data(ip):
    url = "https://ipinfo.io/" + ip + "/json"

    try:
        get_info = urllib.request.urlopen(url)

    except:
        print("\n[red]Такого IP не существует! \nПерезапустите программу и введите правильный.[/red]\n" )
  
    infoList = json.load(get_info)
    
    print("\n", "—" * (terminal_size[0] // 2))
    print(f'''
[white]IP:[white] [green]{infoList["ip"]}
[white]Регион:[/white] {infoList["region"]}
[white]Страна:[/white] {infoList["country"]}
[white]Город:[/white] {infoList["city"]}
[white]Координаты:[/white] {infoList["loc"]}[/green]
''')
    print("—" * (terminal_size[0] // 2), '\n')


about = ("""
 Эта утилита разработана компанией Tskhay Global.
 	
		 	КАК ИСПОЛЬЗОВАТЬ?
 	
 Чтобы узнать из какой страны и региона номер, запустиие утилиту. Введите цифру 1 и введите номер телнфона.
 Чтобы узнать местоположение IP, введите 2, введите IP. На данный момент мы разрабатываем функцию, через которую проще будет узнать IP - адрес чужого телефона.
 
 Чаще всего «геолокация» IP-адреса основана на служебном адресе провайдера, которому этот IP-адрес был назначен. Таким образом, местоположение, указанное для вашего IP-адреса, всегда будет отличаться от вашего физического местоположения. Суть в том, что геолокация по IP-адресу не является надежной или точной.
 
 Чтобы узнать какую функцию преобрела утитилита после обновления, напишите 4 в терминал запущенной утилиты.
 Получайте новости в нашем тг канале:\n
 https://t.me/tskhayglobal""")\n



whats_new = (f"""\nЧто нового:\n\n{'—' * (terminal_size[0] // 2)}\n[cyan]
[green][26.01.2022][/green] Создана эта утилита
[green][1.0.1][/green] Добавлена инструкция использования утилиты
[green][1.0.2][/green] Редизайн кода и небольшие дизайнерские изменения
[/cyan]\n{'—' * (terminal_size[0] // 2)}\n""")


donate = ("""[white]
:coffee: Купить чашечку кофе разработчику:[/white]\n
https://oplata.qiwi.com/form?invoiceUid=99565ac6-5e0e-47f2-8ea8-37ff6b62d4aa\n
Внести свою сумму:\n
https://my.qiwi.com/Yoann-TsTRRrbWr5n
""")


def exit():
    os.system('clear')
    quit()



def main():
    while True:
        quest = int(input("Выберите вариант ——> "))
        
        if quest == 1:
            phone = input("Введите полный номер телефона без + ——> ")
            phone_data(phone)
        
        elif quest == 2:
            ip = input('Введите IP для поиска ——> ')
            ip_data(ip)
            
        elif quest == 3:
          	print(about)
          
        elif quest == 4:
          	print(whats_new)
          	
        elif quest == 5:
         	print(donate)
        
        elif quest == 0: exit()

if __name__ == "__main__":
    main()
