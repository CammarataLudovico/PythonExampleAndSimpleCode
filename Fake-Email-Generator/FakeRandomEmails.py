import random
import string
import csv
import progressbar


# Chiede all'utente quante email vuole generare, e se non viene inserito un valore intero, lo script riparte.
def getcount():
	numero_email = input("Scrivi quante email vuoi generare : ")
	try:
		rowint = int(numero_email)
		return rowint
	except ValueError:
		print ("Inserisci un valore intero!")
		return getcount()

#Crea una stringa da 1 a 20 caratteri alfanumerici e gli aggiunge un finto dominio e una finta estensione.
def makeEmail():
	estensioni = ['com','net']
	domini = ['gmail','yahoo','hotmail','outlook']

	winext = estensioni[random.randint(0,len(estensioni)-1)]
	windom = domini[random.randint(0,len(domini)-1)]

	acclen = random.randint(1,20)

	winacc = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(acclen))

	finale = winacc + "@" + windom + "." + winext
	return finale

#salva quante email deve generare
howmany = getcount()

#counter per il loop While
counter = 0

#Array vuoto per loop
emailarray = []

#Counter per quante email sta generando

print ("Creazione indirizzi email...")
print ("Progresso: ")

prebar = progressbar.ProgressBar(maxval=int(howmany))

for i in prebar(range(howmany)):
	while counter <= howmany:
		emailarray.append(str(makeEmail()))
		counter = counter+1
		prebar.update(i)
	
print ("Creazione completa.")

#Nomina del file

filename = input("Nomina il tuo file: ")


# Qui lo script "crea" le email, usa WA per aggiugerle ad un file, che se non c'è verrà creato

print ("Progresso: ")

bar = progressbar.ProgressBar(maxval=int(howmany))
	
emailfile = open(str(filename), 'w')
aa = csv.writer(emailfile)

for emailaddr in bar(emailarray):
	aa.writerow([emailaddr])
	bar.update()
emailfile.close()

print ("File '" + filename + "' creato.")

