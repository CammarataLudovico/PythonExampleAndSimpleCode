# Calcolatrice per resistenze a 5 bande senza GUI v.0.2.2 (BETA)
print("Questo programma è stato creato per calcolare il valore delle resistenze. Tieni la resistenza nella tua mano e ora trascrivi in valore del colore partendo da destra e inseriscilo quando richiesto.")
print("Attenzione, solo per resistenze a 5 bande!")
# Primo colore
print ("Scegli il primo colore:")
prima_banda = input().lower()
if prima_banda == "nero":
    prima_banda = ""
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
elif prima_banda =="grigio":
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
    terza_banda = "1"
elif terza_banda =="rosso":
    terza_banda = "2"
elif terza_banda =="arancione":
    terza_banda = "3"
elif terza_banda =="giallo":
    terza_banda = "4"
elif terza_banda   =="verde":
    terza_banda = "5"
elif terza_banda =="blu":
    terza_banda = "6"
elif terza_banda =="viola":
    terza_banda = "7"
elif terza_banda =="grigio":
    terza_banda = "8"
elif terza_banda =="bianco":
    terza_banda = "9"
else :
    terza_banda = "invalido"
    print ("Colore invalido.")

# Quarto colore
print ("Scegli il quarto colore:")
quarta_banda = input().lower()
if quarta_banda == "nero":
    quarta_banda = ""
elif quarta_banda =="marrone":
    quarta_banda = "0"
elif quarta_banda =="rosso":
    quarta_banda = "00"
elif quarta_banda =="arancione":
  quarta_banda = "K"
elif quarta_banda =="giallo":
    quarta_banda = "0K"
elif quarta_banda =="verde":
    quarta_banda = "00K"
elif quarta_banda =="blu":
    quarta_banda = "M"
elif quarta_banda =="viola":
    quarta_banda = "0M"
else :
    print ("Colore della banda inesistente.")
    quarta_banda = "Colore inesistente"

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
    resistenza = prima_banda + seconda_banda + terza_banda + quarta_banda
    result()

