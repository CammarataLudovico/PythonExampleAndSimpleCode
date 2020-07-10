# Autore: Ludovico Cammarata
# Calcolatrice per resistenze a 4/5 bande senza GUI v.1.0.0


print(" =================================================================")
print("{Digita il numero corrispodente alla resistenza che vuoi calcolare}")
print(" =================================================================\n\r")
print("1. Resistenza 4 Bande.");
print("2. Resistenza 5 Bande.");
print("3. Esci dal programma.");

scelta = int(input("Scegli la resistenza da calcolare: "))
if (scelta>=1 and scelta <=2):

    if scelta == 1:
        print("Scegli il primo colore (prima cifra significativa) :" )
        prima_banda = input().lower()
        if prima_banda == "nero":
            prima_banda = ""
        elif prima_banda == "marrone":
            prima_banda = "1"
        elif prima_banda == "rosso":
            prima_banda = "2"
        elif prima_banda == "arancione":
            prima_banda = "3"
        elif prima_banda == "giallo":
            prima_banda = "4"
        elif prima_banda == "verde":
            prima_banda = "5"
        elif prima_banda == "blu":
            prima_banda = "6"
        elif prima_banda == "viola":
            prima_banda = "7"
        elif prima_banda == "grigio":
            prima_banda = "8"
        elif prima_banda == "bianco":
            prima_banda = "9"
        else :
            print("Colore della banda inesistente")
            prima_banda = "Colore inesistente"

        # Secondo colore
        # Qui i valori: Nero = O; Marrone = 1; Rosso = 2; Arancio = 3; Giallo = 4; Verde = 5; Blu = 6; Viola = 7; Grigio = 8; Bianco = 9.
        print("Scegli il secondo colore (seconda cifra significativa) :")
        seconda_banda = input().lower()
        if seconda_banda == "nero":
            seconda_banda = "0"
        elif seconda_banda == "marrone":
            seconda_banda = "1"
        elif seconda_banda == "rosso":
            seconda_banda = "2"
        elif seconda_banda == "arancione":
            seconda_banda = "3"
        elif seconda_banda == "giallo":
            seconda_banda = "4"
        elif seconda_banda == "verde":
            seconda_banda = "5"
        elif seconda_banda == "blu":
            seconda_banda = "6"
        elif seconda_banda == "viola":
            seconda_banda = "7"
        elif seconda_banda == "grigio":
            seconda_banda = "8"
        elif seconda_banda == "bianco":
            seconda_banda = "9"
        else :
            print("Colore della banda inesistente")
            seconda_banda = "Colore inesistente"

            # terzo colore
            # Qui i valori: Nero = *1; Marrone = *10; Rosso = *100; Arancio = *1k; Giallo = *10k; Verde = *100k; Blu = *1M; Viola = *10M.
        print("Scegli il terzo colore (moltiplicatore) :")
        terza_banda = input().lower()
        if terza_banda == "nero":
            terza_banda = ""
        elif terza_banda == "marrone":
            terza_banda = "0"
        elif terza_banda == "rosso":
            terza_banda = "00"
        elif terza_banda == "arancione":
            terza_banda = "K"
        elif terza_banda == "giallo":
            terza_banda = "0K"
        elif terza_banda == "verde":
            terza_banda = "00K"
        elif terza_banda == "blu":
            terza_banda = "M"
        elif terza_banda == "viola":
            terza_banda = "0M"
        else:
            print("Colore della banda inesistente")
            terza_banda = "Colore inesistente"



        # Calcolo della tolleranza
        # Qui i valori: Nessuno = ±20%; Argento = ±10%; Oro = ±5%; Marrone = ±1%; Rosso = ±2%; Verde = ±0.5%; Blu = ±0.25%; Viola = ±0.1%.
        print("Ora scegli il colore della tolleranza. Se la tua resistenza è priva di questa banda inserire la parola",
              "(nessuno)" " premi il tasto invio")
        tol = input().lower()
        if tol == "oro":
            tolleranza = "con una tolleranza del ± 5% "
        elif tol == "argento":
            tolleranza = "con una tolleranza del ± 10% "
        elif tol == "":
            tolleranza = "con una tolleranza del ± 20% "
        elif tol == "marrone":
            tolleranza = "con una tolleranza del ± 1% "
        elif tol == "rosso":
            tolleranza = "con una tolleranza del ± 2% "
        elif tol == "verde":
            tolleranza = "con una tolleranza del ± 0.5% "
        elif tol == "blu":
            tolleranza = "con una tolleranza del ± 0.25 "
        elif tol == "viola":
            tolleranza = "con una tolleranza del ± 0.1% "
        else:
            tolleranza = ""

        # Calcolo della resistenza
        def result():
            print("La tua resistenza vale " + resistenza + " Ohms " + tolleranza + ".")


        # Risultato mostrato a schermo del calcolo.
        if prima_banda == "invalido":
            print("Colore inesistente.")
        elif seconda_banda == "invalido":
            print("Colore inesistente.")
        elif terza_banda == "00":
            resistenza = prima_banda + "." + seconda_banda + "K"
            result()
        elif terza_banda == "00K":
            resistenza = prima_banda + "." + seconda_banda + "M"
            result()
        elif terza_banda == "invalido.":
            print("Colore inesistente.")
        else:
            resistenza = prima_banda + seconda_banda + terza_banda
            result()



    # Resistenza 5 Bande
    if scelta == 2:
        print("Scegli il primo colore (prima cifra significativa) :" )
        prima_banda = input().lower()
        if prima_banda == "nero":
            prima_banda = ""
        elif prima_banda == "marrone":
            prima_banda = "1"
        elif prima_banda == "rosso":
            prima_banda = "2"
        elif prima_banda == "arancione":
            prima_banda = "3"
        elif prima_banda == "giallo":
            prima_banda = "4"
        elif prima_banda == "verde":
            prima_banda = "5"
        elif prima_banda == "blu":
            prima_banda = "6"
        elif prima_banda == "viola":
            prima_banda = "7"
        elif prima_banda == "grigio":
            prima_banda = "8"
        elif prima_banda == "bianco":
            prima_banda = "9"
        else :
            print("Colore della banda inesistente")
            prima_banda = "Colore inesistente"

        # Secondo colore
        # Qui i valori: Nero = O; Marrone = 1; Rosso = 2; Arancio = 3; Giallo = 4; Verde = 5; Blu = 6; Viola = 7; Grigio = 8; Bianco = 9.
        print("Scegli il secondo colore (seconda cifra significativa) :")
        seconda_banda = input().lower()
        if seconda_banda == "nero":
            seconda_banda = "0"
        elif seconda_banda == "marrone":
            seconda_banda = "1"
        elif seconda_banda == "rosso":
            seconda_banda = "2"
        elif seconda_banda == "arancione":
            seconda_banda = "3"
        elif seconda_banda == "giallo":
            seconda_banda = "4"
        elif seconda_banda == "verde":
            seconda_banda = "5"
        elif seconda_banda == "blu":
            seconda_banda = "6"
        elif seconda_banda == "viola":
            seconda_banda = "7"
        elif seconda_banda == "grigio":
            seconda_banda = "8"
        elif seconda_banda == "bianco":
            seconda_banda = "9"
        else :
            print("Colore della banda inesistente")
            seconda_banda = "Colore inesistente"

        # Terzo colore
        # Qui i valori: Nero = O; Marrone = 1; Rosso = 2; Arancio = 3; Giallo = 4; Verde = 5; Blu = 6; Viola = 7; Grigio = 8; Bianco = 9.
        print("Scegli il terzo colore (terza cifra significativa) :")
        terza_banda = input().lower()
        if terza_banda == "nero":
            terza_banda = "0"
        elif terza_banda == "marrone":
            terza_banda = "1"
        elif terza_banda == "rosso":
            terza_banda = "2"
        elif terza_banda == "arancione":
            terza_banda = "3"
        elif terza_banda == "giallo":
            terza_banda = "4"
        elif terza_banda == "verde":
            terza_banda = "5"
        elif terza_banda == "blu":
            terza_banda = "6"
        elif terza_banda == "viola":
            terza_banda = "7"
        elif terza_banda == "grigio":
            terza_banda = "8"
        elif terza_banda == "bianco":
            terza_banda = "9"
        else :
            print("Colore della banda inesistente")
            terza_banda = "Colore inesistente"

        # Quarto colore
        # Qui i valori: Nero = *1; Marrone = *10; Rosso = *100; Arancio = *1k; Giallo = *10k; Verde = *100k; Blu = *1M; Viola = *10M.
        print("Scegli il quarto colore (moltiplicatore) :")
        quarta_banda = input().lower()
        if quarta_banda == "nero":
            quarta_banda = ""
        elif quarta_banda == "marrone":
            quarta_banda = "0"
        elif quarta_banda == "rosso":
            quarta_banda = "00"
        elif quarta_banda == "arancione":
            quarta_banda = "K"
        elif quarta_banda == "giallo":
            quarta_banda = "0K"
        elif quarta_banda == "verde":
            quarta_banda = "00K"
        elif quarta_banda == "blu":
            quarta_banda = "M"
        elif quarta_banda == "viola":
            quarta_banda = "0M"
        else :
            print("Colore della banda inesistente")
            quarta_banda = "Colore inesistente"

        # Calcolo della tolleranza
        # Qui i valori: Nessuno = ±20%; Argento = ±10%; Oro = ±5%; Marrone = ±1%; Rosso = ±2%; Verde = ±0.5%; Blu = ±0.25%; Viola = ±0.1%.
        print("Ora scegli il colore della tolleranza. Se la tua resistenza è priva di questa banda inserire la parola",
              "(nessuno)" " premi il tasto invio")
        tol = input().lower()
        if tol == "oro":
            tolleranza = "con una tolleranza del ± 5% "
        elif tol == "argento":
            tolleranza = "con una tolleranza del ± 10% "
        elif tol == "":
            tolleranza = "con una tolleranza del ± 20% "
        elif tol == "marrone":
            tolleranza = "con una tolleranza del ± 1% "
        elif tol == "rosso":
            tolleranza = "con una tolleranza del ± 2% "
        elif tol == "verde":
            tolleranza = "con una tolleranza del ± 0.5% "
        elif tol == "blu":
            tolleranza = "con una tolleranza del ± 0.25 "
        elif tol == "viola":
            tolleranza = "con una tolleranza del ± 0.1% "
        else:
            tolleranza = ""

        # Calcolo della resistenza
        def result():
            print("La tua resistenza vale " + resistenza + " Ohms " + tolleranza + ".")


        # Risultato mostrato a schermo del calcolo.
        if prima_banda == "invalido":
            print("Colore inesistente.")
        elif seconda_banda == "invalido":
            print("Colore inesistente.")
        elif terza_banda == "00":
            resistenza = prima_banda + "." + seconda_banda + "K"
            result()
        elif terza_banda == "00K":
            resistenza = prima_banda + "." + seconda_banda + "M"
            result()
        elif terza_banda == "invalido.":
            print("Colore inesistente.")
        else:
            resistenza = prima_banda + seconda_banda + terza_banda + quarta_banda
            result()
    elif scelta == 3:
        exit();







