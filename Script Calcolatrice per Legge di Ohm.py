# Autore: Ludovico Cammarata
# Versione 1.0.1
# Questo script calcola i valori di: Tensione; Corrente; Resistenza; Potenza, usati nella legge di Ohm con una tolleranza di 3 cifre dopo la virgola (errore di ± 0.001).
# Ho utilizzato '\n\r' così da andare a capo e rendere così l'output un pò più carino e meno incasinato
print(" ================================================================")
print("{Digita il numero corrispodente all'operazione che vuoi calcolare}")
print(" ================================================================\n\r")
print("1. Tensione." "          (Formula: R*I, espresso come V)");
print("2. Corrente." "          (Formula: V/R, espresso come I)");
print("3. Resistenza." "        (Formula: V/I, espresso come R)");
print("4. Potenza." "           (Formula: V*I, espresso come P)");
print("5. Esci dal programma.\n\r");
scelta = int(input("Scegli cosa calcolare: "));
if (scelta>=1 and scelta<=4):
    print("Scrivi i 2 valori (uno alla volta): ");
    valore1 = float(input());
    valore2 = float(input());
    if scelta == 1:
    	res = valore1*valore2;
    	print("\n\rIl tuo risultato è = ", "%.3f" " Volt" %res);
    elif scelta == 2:
    	res = valore1/valore2;
    	print("\n\rIl tuo risultato è = ", "%.3f" " Ampere" %res);
    elif scelta == 3:
    	res = valore1/valore2;
    	print("\n\rIl tuo risultato è = ", "%.3f" " Ohm" %res);
    elif scelta == 4:
    	res = valore1*valore2;
    	print("\n\rIl tuo risultato è = ", "%.3f" " Watt" %res);
elif scelta == 5:
    exit();
else:
    print("Input sbagliato..!!");
