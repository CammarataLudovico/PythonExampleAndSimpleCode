# Autore: Ludovico Cammarata
# Versione: 1.0.3
# Programma in Python per capire se la tua password è ad un buon livello di sicurezza
# Per poter validare la vostra password dovete scriverla dopo l'uguale nella variabile password qui sotto 
import re 
print("")
password = "Anassop9"
# Con flag = 0 lo script assegna un valore iniziale di 0
flag = 0
while True:
        #Qui lo script vede se la password inserita è almeno di 10 caratteri, se così non fosse attribuisce alla password valore = -1 e quindi nel conteggio alla fine la password risulta non valida
	if (len(password)<10): 
		flag = -1
		break
	#Qui lo script vede se è stato inserito una lettera da a-z minuscole, se così non fosse attribuisce alla password valore = -2 e quindi nel conteggio alla fine la password risulta non valida
	elif not re.search("[a-z]", password): 
		flag = -2
		break
	#Qui lo script vede se è stato inserito una lettera da A-Z maiuscole, se così non fosse attribuisce alla password valore = -3 e quindi nel conteggio alla fine la password risulta non valida
	elif not re.search("[A-Z]", password): 
		flag = -3
		break
	#Qui lo script vede se è stato inserito un numero da 0-9, se così non fosse attribuisce alla password valore = -4 e quindi nel conteggio alla fine la password risulta non valida
	elif not re.search("[0-9]", password): 
		flag = -4
		break
	#Qui lo script vede se è stato inserito un carattere tra questi qui sotto,  se così non fosse attribuisce alla password valore = -5 e quindi nel conteggio alla fine la password risulta non valida
	elif not re.search("[_@$]", password): 
		flag = -5
		break
	elif re.search("\s", password): 
		flag = -6
		break
	#Qui lo script vede se il valore finale del flag è uguale a 0, se è così allora stamperà a schermo: Password valida
	else: 
		flag = 0
		print("Password valida") 
		break
# Valore finale della variabile flag = -1
if flag ==-1: 
	print("Password non valida: non è lunga almeno 10 caratteri!")
# Valore finale della variabile flag = -2
elif flag == -2:       
        print("Password non valida: non contiene almeno un carattere minuscolo!")
# Valore finale della variabile flag = -3
elif flag == -3:
        print ("Password non valida: non contiene almeno un carattere maiuscolo!")
# Valore finale della variabile flag = -4
elif flag == -4:
        print ("Password non valida: non contiene almeno un numero!")
# Valore finale della variabile flag = -5
elif flag == -5:
        print ("Password non valida: non contiene un carattere speciale elencato sopra!")       
print("")
