# Autore: Ludovico Cammarata
# Versione: 1.0.1
# Programma in Python per capire se la tua password è ad un buon livello di sicurezza
# Per poter validare la vostra password dovete scriverla dopo l'uguale nella variabile password qui sotto 
import re 
print("")
password = "An_s$op9"
flag = 0
while True:
        #Qui lo script vede se la password inserita è almeno di 8 caratteri, se così non fosse attribuisce alla password valore = -1 e quindi nel conteggio alla fine la password risulta non valida
	if (len(password)<8): 
		flag = -1
		break
	#Qui lo script vede se è stato inserito una lettera da a-z minuscole, se così non fosse attribuisce alla password valore = -1 e quindi nel conteggio alla fine la password risulta non valida
	elif not re.search("[a-z]", password): 
		flag = -1
		break
	#Qui lo script vede se è stato inserito una lettera da A-Z maiuscole, se così non fosse attribuisce alla password valore = -1 e quindi nel conteggio alla fine la password risulta non valida
	elif not re.search("[A-Z]", password): 
		flag = -1
		break
	#Qui los script vede se è stato inserito un numero da 0-9, se così non fosse attribuisce alla password valore = -1 e quindi nel conteggio alla fine la password risulta non valida
	elif not re.search("[0-9]", password): 
		flag = -1
		break
	#Qui lo script vede se è stato inserito un carattere tra questi qui sotto,  se così non fosse attribuisce alla password valore = -1 e quindi nel conteggio alla fine la password risulta non valida
	elif not re.search("[_@$]", password): 
		flag = -1
		break
	elif re.search("\s", password): 
		flag = -1
		break
	else: 
		flag = 0
		print("Password valida") 
		break

if flag ==-1: 
	print("Password non valida")
print("")
