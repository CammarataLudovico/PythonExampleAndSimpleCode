# Questo script calcola i valori di: Tensione;Corrente;Resistenza;Potenza,con 3 cifre dopo la virgola (errore di ± 0.001).

print("1. Tensione" " (V)");
print("2. Corrente" " (I)");
print("3. Resistenza" " (R)");
print("4. Potenza" " (P)");
print("5. Esci dal programma");
scelta = int(input("Scegli cosa calcolare: "));
if (scelta>=1 and scelta<=4):
    print("Scrivi 2 valori: ");
    valore1 = float(input());
    valore2 = float(input());
    if scelta == 1:
    	res = valore1*valore2;
    	print("Il tuo risultato è = ", "%.3f" " Volt" %res);
    elif scelta == 2:
    	res = valore1/valore2;
    	print("Il tuo risultato è = ", "%.3f" " Ampere" %res);
    elif scelta == 3:
    	res = valore1/valore2;
    	print("Il tuo risultato è = ", "%.3f" " Ohm" %res);
    elif scelta == 4:
    	res = valore1*valore2;
    	print("Il tuo risultato è = ", "%.3f" " Watt" %res);
elif scelta == 5:
    exit();
else:
    print("Input sbagliato..!!");
