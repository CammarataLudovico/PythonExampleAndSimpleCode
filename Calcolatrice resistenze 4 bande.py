# Autore: Ludovico Cammarata
# Calcolatrice per resistenze a 4 bande senza GUI v.1.0.1 

print("==============================================================================")
print("Questo programma è stato creato per calcolare il valore delle resistenze. ")
print("Tieni la resistenza nella tua mano e ora trascrivi in valore del colore partendo da destra e inseriscilo quando richiesto. \n\r")
print("!!!  Attenzione, solo per resistenze a 4 bande !!!")
print("==============================================================================")
# Primo colore
# Qui i valori: Nero = O; Marrone = 1; Rosso = 2; Arancio = 3; Giallo = 4; Verde = 5; Blu = 6; Viola = 7; Grigio = 8; Bianco = 9.
print ("Scegli il primo colore (prima cifra significativa) :")
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
elif prima_banda =="grigio":
    prima_banda = "8"
elif prima_banda =="bianco":
    prima_banda = "9"
else :
    prima_banda = "invalido"
    print ("Colore invalido.")
# Secondo colore
# Qui i valori: Nero = O; Marrone = 1; Rosso = 2; Arancio = 3; Giallo = 4; Verde = 5; Blu = 6; Viola = 7; Grigio = 8; Bianco = 9.
print ("Scegli il secondo colore (seconda cifra significativa) :")
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
# Qui i valori: Nero = *1; Marrone = *10; Rosso = *100; Arancio = *1k; Giallo = *10k; Verde = *100k; Blu = *1M; Viola = *10M.
print ("Scegli il terzo colore (moltiplicatore) :")
terza_banda = input().lower()
if terza_banda == "nero":
    terza_banda = ""
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
# Qui i valori: Nessuno = ±20%; Argento = ±10%; Oro = ±5%; Marrone = ±1%; Rosso = ±2%; Verde = ±0.5%; Blu = ±0.25%; Viola = ±0.1%.
print("Ora scegli il colore della tolleranza. Se la tua resistenza è priva di tolleranza, premi invio.")
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
elif tol == "blu ":
    tolleranza = "con una tolleranza del ± 0.25% "
elif tol == "viola":
    tolleranza = "con una tolleranza del ± 0.1% "
else:
    tolleranza = ""

# Calcolo della resistenza
def result(): 
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
