def fahrenheit(temp_c):
    return 32 + 1.8 * temp_c


def gevoelstemperatuur(temp_c, windsnelheid, luchtvochtigheid):
    return temp_c - luchtvochtigheid / 100 * windsnelheid


def weerrapport(temp_c, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(temp_c, windsnelheid, luchtvochtigheid)

    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif gevoel < 0:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif gevoel < 10:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"


def weerstation():
    temperaturen = []

    for dag in range(1, 8):

        while True:
            temp = input(f"Wat is op dag {dag} de temperatuur [°C]: ")

            if temp == "":
                print("Programma gestopt.")
                return

            try:
                temp = float(temp)
                break
            except ValueError:
                print("Ongeldige invoer, probeer opnieuw.")

        while True:
            wind = input(f"Wat is op dag {dag} de windsnelheid [m/s]: ")

            if wind == "":
                print("Programma gestopt.")
                return

            try:
                wind = float(wind)

                if wind < 0:
                    print("Ongeldige invoer, probeer opnieuw.")
                    continue

                break

            except ValueError:
                print("Ongeldige invoer, probeer opnieuw.")

        while True:
            vocht = input(f"Wat is op dag {dag} de vochtigheid [%]: ")

            if vocht == "":
                print("Programma gestopt.")
                return

            try:
                luchtvochtigheid = int(vocht)

                if 0 <= luchtvochtigheid <= 100:
                    break
                else:
                    print("Voer een geheel getal tussen 0 en 100 in.")

            except ValueError:
                print("Ongeldige invoer, probeer opnieuw.")

        temperaturen.append(temp)

        fahrenheit_temp = fahrenheit(temp)
        rapport = weerrapport(temp, wind, luchtvochtigheid)
        gemiddelde = sum(temperaturen) / len(temperaturen)

        print(f"Het is {temp:.1f}°C ({fahrenheit_temp:.1f}°F)")
        print(rapport)
        print(f"Gemiddelde temperatuur: {gemiddelde:.1f}°C")
        print("=" * 40)


weerstation()