#Autore: Ludovico Cammarata
import random

print('''Password Generator
==================''')
#caratteri_consentiti = caratteri che può utilizzare il programma per creare password
caratteri_consentiti = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@!#$%-/=^\_`{}~+,?0123456789'
#lo script chiede all'utente quante password deve generare
numero_di_password = input('Numero di password da generare: ')
numero_di_password = int(numero_di_password)
#lo script chiede all'utente la lunghezza delle password da generare
lunghezza_password = input('Lunghezza della password: ')
lunghezza_password = int(lunghezza_password)
#il programma da qui in poi "calcolerà" e scriverà a schermo le password che ha generato
print("Ecco qui le tue password: ")
#qui "legge" quante password deve generare, infatti ne genera fino a 'numero_di_caratteri' cioè l'input che abbiamo dato prima al programma
for password in range(numero_di_password):
  password = ""
#qui "legge" il numero di caratteri che le password generate devono avere, che abbiamo prima scritto nella variabile lunghezza
  for caratteri in range(lunghezza_password):
#qui il programma "calcola le password con una scelta random (random.choice) tra i caratteri consentiti che sono scritti nella variabile 'caratteri_consentiti'
     password += random.choice(caratteri_consentiti)
     
#qui il programma "scrive " a schermo le password generate
  print(password)
print("Password generate con successo")
