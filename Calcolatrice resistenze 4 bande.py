# Calcolatrice per resistenze a 4 bande senza GUI v.0.1.2 (BETA)
print("Questo programma è stato creato per calcolare il valore delle resistenze. Tieni la resistenza nella tua mano e ora trascrivi in valore del colore partendo da destra e inseriscilo quando richiesto.")
print("Attenzione, solo per resistenze a 4 bande!")
# Primo colore
print ("Scegli il primo colore:")
prima_banda = input().lower()
if prima_banda == "nero":
    prima_banda = "0"
elif prima_banda =="marrone":
    prima_banda = "1"
elif prima_banda =="rosso":
    prima_banda = "2"
elif prima_banda =="arancione":
    prima_banda = "3"
elif prima_banda =="giallo":
    prima_banda = "4"
elif prima_banda =="verde":
    prima_banda = "5"
elif prima_banda =="blu":
    prima_banda = "6"
elif prima_banda =="viola":
    prima_banda = "7"
elif prima_banda =="grgio":
    prima_banda = "8"
elif prima_banda =="bianco":
    prima_banda = "9"
else :
    prima_banda = "invalido"
    print ("Colore invalido.")
# Secondo colore
print ("Scegli il secondo colore:")
seconda_banda = input().lower()
if seconda_banda == "nero":
    seconda_banda = "0"
elif seconda_banda =="marrone":
    seconda_banda = "1"
elif seconda_banda =="rosso":
    seconda_banda = "2"
elif seconda_banda =="arancione":
    seconda_banda = "3"
elif seconda_banda =="giallo":
    seconda_banda = "4"
elif seconda_banda   =="verde":
    seconda_banda = "5"
elif seconda_banda =="blu":
    seconda_banda = "6"
elif seconda_banda =="viola":
    seconda_banda = "7"
elif seconda_banda =="grigio":
    seconda_banda = "8"
elif seconda_banda =="bianco":
    seconda_banda = "9"
else :
    seconda_banda = "invalido"
    print ("Colore invalido.")
# Terzo colore
print ("Scegli il terzo colore:")
terza_banda = input().lower()
if terza_banda == "nero":
    terza_banda = "0"
elif terza_banda =="marrone":
    terza_banda = "0"
elif terza_banda =="rosso":
    terza_banda = "00"
elif terza_banda =="arancione":
  terza_banda = "K"
elif terza_banda =="giallo":
    terza_banda = "0K"
elif terza_banda =="verde":
    terza_banda = "00K"
elif terza_banda =="blu":
    terza_banda = "M"
elif terza_banda =="viola":
    terza_banda = "0M"
else :
    print ("Colore della banda inesistente.")
    terza_banda = "Colore inesistente"
# Calcolo della tolleranza
print("Ora scegli il colore della tolleranza. Se la tua resistenza è priva di questa banda inserire la parola", "(nessuno)" " premi il tasto invio")
tol = input().lower()
if tol == "oro":
    tolleranza = "con una tolleranza del ±5% "
elif tol == "argento":
    tolleranza = "con una tolleranza del ±10% "
elif tol == "nessuno":
    tolleranza = "con una tolleranza del ±20% "
else:
    tolleranza = ""


def result(): # Calcolo della resistenza
    print ("La tua resistenza vale "+ resistenza  +" Ohms " + tolleranza + ".")


# Risultato mostrato a schermo del calcolo.
if prima_banda == "invalido":
    print ("Colore invalido.")
elif seconda_banda == "invalido":
    print ("Colore invalido.")
elif terza_banda == "00":
    resistenza = prima_banda + "." + seconda_banda + "K"
    result()
elif terza_banda == "00K":
    resistenza = prima_banda + "." + seconda_banda + "M"
    result ()
elif terza_banda == "invalido.":
    print ("Colore invalido.")
else :
    resistenza = prima_banda + seconda_banda + terza_banda
    result()
