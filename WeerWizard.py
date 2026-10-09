from SmartSystems import smart_app_controller
from WeerStation import weerstation
from Utrechtweer import huidige_temperatuur

print("\033[0;37m \033[0;94m▓██\033[0;37m   \033[0;94m█▄\033[0;37m                    \033[0;94m▓██\033[0;37m   \033[0;94m█▄\033[0;37m                         \033[0;97m██\033[0m")
print("\033[0;94m▄███\033[0;37m \033[0;94m▄\033[0;37m \033[0;94m██\033[0;37m \033[0;97m▄█▀█▄\033[0;37m \033[0;97m▄█▀█▄\033[0;37m \033[0;97m▄█▀\033[0;97;47m▀\033[0;97m▄\033[0;37m \033[0;94m▄███\033[0;37m \033[0;94m▄\033[0;37m \033[0;94m██\033[0;37m \033[0;97m▀▀\033[0;37m \033[0;97m▀▀▀█▄\033[0;37m \033[0;97m▄█▀█▄\033[0;37m \033[0;97m▄█▀\033[0;97;47m▀\033[0;97m▄\033[0;37m \033[0;97m▄█▀██\033[0m")
print("\033[0;37m \033[0;94m███\033[0;37m \033[0;94m█\033[0;37m \033[0;94m██\033[0;37m \033[0;97m██▀▀\033[0;37m  \033[0;97m██▀▀\033[0;37m  \033[0;97m██\033[0;37m     \033[0;94m███\033[0;37m \033[0;94m█\033[0;37m \033[0;94m██\033[0;37m \033[0;97m█\033[0;97;47m▄\033[0;37m \033[0;97m▄█▀▀\033[0;37m  \033[0;97m██▀██\033[0;37m \033[0;97m██\033[0;37m    \033[0;97m██\033[0;37m \033[0;97m██\033[0m")
print("\033[0;37m \033[0;34m▀\033[0;94m▀▀▀\033[0;37m \033[0;94m▀▀\033[0;37m   \033[0;97m▀▀\033[0;37m▀   \033[0;97m▀▀\033[0;37m▀  \033[0;97m▀\033[0;37m▀     \033[0;34m▀\033[0;94m▀▀▀\033[0;37m \033[0;94m▀▀\033[0;37m  \033[0;97m▀▀\033[0;37m  ▀\033[0;97m▀▀▀\033[0;37m \033[0;97m▀▀\033[0;37m \033[0;97m▀\033[0;37m▀ \033[0;97m▀\033[0;37m▀     \033[0;97m▀▀▀\033[0;37m▀\033[0m")
print("")

BLUE = '\033[34m'

while True:
    try:
        keuze = int(input(
            BLUE+"1: Weer station\n"
            "2: Smart app controller\n"
            "3: Huidige temperatuur in Utrecht\n"
            "4: Stoppen\n"
            "Maak uw keuze: "
        ))

        if keuze == 1:
            weerstation()
        elif keuze == 2:
            smart_app_controller()
        elif keuze == 3:
            print(f'De huidige temperatuur in Utrecht is {huidige_temperatuur()} C°')
        elif keuze == 4:
            print('Goodbye!')
            break
        else:
            print("Kies een optie van de menu \n")

    except FileNotFoundError:
        print('Het bestand is niet gevonden \n')

    except ValueError:
        print('Kies een optie van de menu (nummer)')


