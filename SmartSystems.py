def aantal_dagen(InputFile):
    file=open(InputFile,'r')
    lines=file.readlines()
    file.close()
    dagen= len(lines) - 1
    return dagen

#print(aantal_dagen('InputFile.txt'))



def auto_bereken(InputFile,OutputFile):
    infile = open(InputFile, "r")
    lines = infile.readlines()
    infile.close()
    outfile = open(OutputFile, 'w')
    lines = lines[1:]
    for line in lines:
        gegevens=line.split()
        date= gegevens[0]
        numPeople=int(gegevens[1])
        tempSetpoint=int(gegevens[2])
        tempOutside=int(gegevens[3])
        rainfall=int(gegevens[4])
        temp_difference = tempSetpoint - tempOutside
        if temp_difference >= 20:
            cv_percentage = 100
        elif temp_difference >= 10:
            cv_percentage = 50
        else:
            cv_percentage = 0
        ventilation = numPeople + 1
        if ventilation > 4:
            ventilation = 4
        if rainfall < 3:
            water = True
        else:
            water = False

        outfile.write(str(date) + ";" + str(cv_percentage) + ";" + str(ventilation) + ";" + str(water) + "\n")

    outfile.close()
    print('Alle informatie zijn toegevoegd aan het bestand (OutputFile)')


# auto_bereken(InputFile='Inputfile.txt', OutputFile='OutputFile.txt')


def overwrite_settings(OutputFile):
    file= open(OutputFile, 'r')
    lines=file.readlines()
    file.close()
    date = input('Kies een datum(dd-mm-jj): ')
    gevonden = False
    for data in range(len(lines)):
        line = lines[data]
        gegevens = line.strip().split(";")
        dateInFile=gegevens[0]
        if dateInFile == date:
            gevonden=True

            system = int(input(
                "Choose system:\n"
                "1. CV ketel\n"
                "2. Ventilatie\n"
                "3. Bewatering\n"
            ))

            if system not in [1, 2, 3]:
                return-3

            new_value = input("Verandering: ")

            if system == 1:
                new_value=int(new_value)
                if new_value < 0 or new_value > 100:
                    return -3
                gegevens[1] = str(new_value)

            elif system == 2:
                new_value = int(new_value)
                if new_value < 0 or new_value > 4:
                    return -3
                gegevens[2] = str(new_value)

            elif system == 3:
                if new_value == "0":
                    gegevens[3] = "False"

                elif new_value == "1":
                    gegevens[3] = "True"
                else:
                    return -3

            nieuwe_regel = ";".join(gegevens) + "\n"
            lines[data]=nieuwe_regel
            break

    if gevonden == False:
        return -1

    file = open(OutputFile, "w")
    for line in lines:
        file.write(line)
    file.close()
    return 0


def smart_app_controller():

    input_file = "InputFile.txt"
    output_file = "OutputFile.txt"

    while True:
        print('\nWelkom bij smart app controller!')
        try:
            keuze = int(input(
                "1. Aantal dagen weergeven\n"
                "2. Automatisch berekenen en opslaan\n"
                "3. Waarde overschrijven\n"
                "4. Stoppen\n"
                "Maak uw keuze: "
            ))

        except ValueError:
            print("Kies een optie van het menu.")
            continue

        if keuze == 1:
            print(f"Aantal dagen: {aantal_dagen(input_file)}")

        elif keuze == 2:
            auto_bereken(input_file, output_file)

        elif keuze == 3:
            resultaat = overwrite_settings(output_file)

            if resultaat == 0:
                print("Waarde succesvol aangepast.")

            elif resultaat == -1:
                print("Datum niet gevonden.")

            elif resultaat == -3:
                print("Ongeldige invoer.")

        elif keuze == 4:
            print("Goodbye!\n")
            break

        else:
            print("Ongeldige keuze.")










