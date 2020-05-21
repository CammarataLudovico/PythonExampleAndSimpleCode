# Versione Python 3.7.6
# Autore: Ludovico Cammarata
# Semplice script per il controllo di un "parcheggio"
class Queue:
    def __init__(self):
        self._qList = list()
    def isEmpty(self):
        return len(self._qList)==0
    def __len__(self):
        return len(self._qList)
    def enqueue(self,item):
        self._qList.append(item)


# "Definizione" della macchine con le varie targhe
class Car:
    def __init__(self,pltNum):
        self.pltNum = pltNum
        self.counter = 0
        self.next = None

# Lista macchine con targhe
class LinkedList:

    def __init__(self):
        self.head = None
        self.numCar = 0
        
    def insertLast(self,pltNum):
        newCar = Car(pltNum)
        newCar.next = None
        

# Corpo centrale del programma
park = Queue()
parkIn = list()
waitingList = LinkedList()
maxSize = 16


# Funzione arrivo
def arriving(plateNum,counter):
    
    # when park has a free space
    if checkSpaces():
        newCar = Car(plateNum)
        newCar.counter = counter
        park.enqueue(newCar)
        parkIn.append(plateNum)
        if newCar.counter==0:
            print("A. C'è un posto libero, la macchina", "con targa",newCar.pltNum, " può parcheggiare.")
 #A = posti liberi, B = posti occupati,  (solo per mappa mentale)
    else:
        print("B. I posti sono tutti occupati,la macchina", "con targa", "%s deve aspettare." % plateNum)
        waitingList.insertLast(plateNum)
# Controlla i posti disponibilli
def checkSpaces():
    if (park.__len__() < maxSize):
        return True
    else:
        return False


#   Per poter funzionare bisogna inserire lo script in una cartella, con un file chiamato inputs.txt, con all'interno i "dati" delle macchine
#   Non ci devono essere spazi bianchi o righe bianche alla fine del file .txt
#   Le macchine devono avere la targa formata da 4 caratteri (sia numeri che lettere)


# Prendi gli "input" cioè le macchine dal file e controlla che soddisfino i requisiti delle targhe
# r: è usato per far leggere i dati allo script
file = open("inputs.txt","r")
while True:
    line = file.readline()
    if(""==line):
        print("                 |======================|")
        print("                 | Programma Completato |")
        print("                 |======================|")
        break
    k = line.split(" ")
    aORd = k[0]
    plateNum = k[1][:4]
    if aORd=='a':
        arriving(plateNum,0)
# Ho voluto fare un piccolo disegno del parcheggio
print("\n")
print("                =========Parcheggio===========")
print('''                ******************************
                *  °||°	  °||°	 °||°	°||° *
                *  °||°	  °||°	 °||°	°||° *
                *  PK29	  JN26	 CI38  	AY56 *
                *			     *
                *  °||°	  °||°	 °||°	°||° *
                *  °||°	  °||°	 °||°	°||° *
                *  BG27	  KD06	 TT72	OQ63 *******************************
                *			                         
                *  °||°	  °||°	 °||°	°||° ******************************* 
                *  °||°	  °||°	 °||°	°||° *
                *  TZ42	  BP74	 CG50	DO01 *
                *                            *
                *  °||°	  °||°	 °||°	°||° *
                *  °||°	  °||°	 °||°	°||° *
                *  WV92   JS82   BZ29   QW42 *
                ******************************''')

print("\n")
print("                ====In attesa====")
print('''                *****************
                *  °||°	  °||°	*
                *  °||°	  °||°	*
                *  UR16	  JM46	*
                *		*
                *  °||°	  °||°	*
                *  °||°	  °||°	*
                *  RI17	  HT87	*********************
                *		                    *
                *  °||°	  °||°	*****************   *
                *  °||°	  °||°	*               *   *
                *  ZR58	  CB19	*               *   *
                *               *               *   *
                *  °||°	  °||°	*               *   ***************
                *  °||°	  °||°	*               *   
                *  AN36   OR32  *               *******************  
                *****************''')



