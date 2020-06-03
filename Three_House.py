import turtle
import math

print(" ==========================================================")
print("{Digita il numero corrispodente alla casa che vuoi generare}")
print(" ==========================================================\n\r")
#Se viene effettuta questa scelta viene generate la prima casa
print("1. Casa_1." "  ");
#Se viene effettuta questa scelta viene generate la seconda casa
print("2. Casa_2." "  ");
#Se viene effettuta questa scelta viene generate la terza casa
print("3. Casa_3." "  ");
#Se viene effettuta questa scelta verrà richiesto di premere ok per chiudere il programma
print("4. Esci dal programma.\n\r");
#Qui viene richiesto di scegliere un numero da 1 a 4.
scelta = int(input("Scegli la versione della casa desiderata: "));
if (scelta>=1 and scelta<=4):
  #Se la scelta ricade sul numero 1 allora lo script genererà la casa con questi parametri
  if scelta == 1:
    #Creazione della finestra
    screen = turtle.Screen()
    #Colore di sfondo
    screen.bgcolor("White")

    #Creazione puntatore 
    t = turtle.Turtle()
    #Colore puntatore
    t.color("black")
    t.shape("turtle")
    #Velocità puntatore
    t.speed(5)

    # Riempimento e creazione Rettangoli
    # Dimensione e colore
    def drawRectangle(t, width, height, color):
      t.fillcolor(color)
      t.begin_fill()
      t.forward(width)
      t.left(90)
      t.forward(height)
      t.left(90)
      t.forward(width)
      t.left(90)
      t.forward(height)
      t.left(90)
      t.end_fill()
  
    # Riempimento e creazione Triangoli
    def drawTriangle(t, length, color):
      t.fillcolor(color)
      t.begin_fill()
      t.forward(length)
      t.left(135)
      t.forward(length / math.sqrt(2))
      t.left(90)
      t.forward(length / math.sqrt(2))
      t.left(135)
      t.end_fill()
  
    # Riempimento e creazione Parallelogrammi
    def drawParallelogram(t, width, height, color):
      t.fillcolor(color)
      t.begin_fill()
      t.left(30)
      t.forward(width)
      t.left(60)
      t.forward(height)
      t.left(120)
      t.forward(width)
      t.left(60)
      t.forward(height)
      t.left(90)
      t.end_fill()


    # Fronte casa
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    # Coordinate per la creazione del fronte casa 
    t.goto(-150, -120)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore 
    drawRectangle(t, 100, 110, "blue")

    # Porta
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    # Coordinate per la creazione della porta
    t.goto(-120, -120)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore
    drawRectangle(t, 40, 60, "lightgreen")

    # Tetto Frontale Casa
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    # Coordinate per la creazione del Tetto Frontale
    t.goto(-150, -10)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore
    drawTriangle(t, 100, "magenta")

    # Parte laterale Casa
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    # Coordinate per la creazione della parte laterale della Casa
    t.goto(-50, -120)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore
    drawParallelogram(t, 60, 110, "yellow")

    # Fascia laterale
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    # Coordinate per la creazione della Fascia laterale della Casa
    t.goto(-150, -35)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore
    drawRectangle(t, 100, 25, "Green")

    # Finestra
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    # Coordinate per la creazione della finestra
    t.goto(-30, -60)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore
    drawParallelogram(t, 20, 30, "brown")
    
    # Fascia laterale
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    # Coordinate per la creazione della fascia laterale
    t.goto(-50, -35)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore
    drawParallelogram(t, 60, 25, "Green")

    # Tetto Laterale Casa
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    t.goto(-50, -10)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore
    t.fillcolor("orange")
    t.begin_fill()
    t.left(30)
    t.forward(60)
    t.left(105)
    t.forward(100 / math.sqrt(2))
    t.left(75)
    t.forward(60)
    t.left(105)
    t.forward(100 / math.sqrt(2))
    t.left(45)
    t.end_fill()
    # Cancella il puntatore
    t.hideturtle()
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()

  # Se la scelta ricade sul numero 2 allora lo script genererà la casa con questi parametri
  if scelta == 2:
    # Creazione della finestra
    screen = turtle.Screen()
    # Colore di sfondo
    screen.bgcolor("skyblue")

    # Creazione puntatore 
    t = turtle.Turtle()
    # Colore puntatore
    t.color("black")
    t.shape("turtle")
    # Velocità puntatore
    t.speed(8)

    # Riempimento e creazione Rettangoli
    # Dimensione e colore
    def drawRectangle(t, width, height, color):
      t.fillcolor(color)
      t.begin_fill()
      t.forward(width)
      t.left(90)
      t.forward(height)
      t.left(90)
      t.forward(width)
      t.left(90)
      t.forward(height)
      t.left(90)
      t.end_fill()
  
    # Riempimento e creazione Triangoli
    def drawTriangle(t, length, color):
      t.fillcolor(color)
      t.begin_fill()
      t.forward(length)
      t.left(135)
      t.forward(length / math.sqrt(2))
      t.left(90)
      t.forward(length / math.sqrt(2))
      t.left(135)
      t.end_fill()
  
    # Riempimento e creazione Parallelogrammi
    def drawParallelogram(t, width, height, color):
      t.fillcolor(color)
      t.begin_fill()
      t.left(30)
      t.forward(width)
      t.left(60)
      t.forward(height)
      t.left(120)
      t.forward(width)
      t.left(60)
      t.forward(height)
      t.left(90)
      t.end_fill()


    # Fronte casa
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    # Coordinate per la creazione del fronte casa 
    t.goto(-150, -120)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore 
    drawRectangle(t, 100, 110, "Yellow")


    # Fascia laterale
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    # Coordinate per la creazione della Fascia laterale della Casa
    t.goto(-150, -35)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore
    drawRectangle(t, 100, 25, "Purple")

    

    # Porta
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    # Coordinate per la creazione della porta
    t.goto(-140, -120)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore
    drawRectangle(t, 60, 85, "Orange")

    # Tetto Frontale Casa
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    # Coordinate per la creazione del Tetto Frontale
    t.goto(-150, -10)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore
    drawTriangle(t, 100, "red")

    # Parte laterale Casa
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    # Coordinate per la creazione della parte laterale della Casa
    t.goto(-50, -120)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore
    drawParallelogram(t, 40, 110, "Green")

    # Finestra
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    # Coordinate per la creazione della finestra
    t.goto(-40, -70)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore
    drawParallelogram(t, 20, 30, "magenta")

    # Fascia laterale
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    # Coordinate per la creazione della fascia laterale
    t.goto(-50, -35)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore
    drawParallelogram(t, 40, 25, "purple")
    

    # Tetto Laterale Casa
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    t.goto(-50, -10)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore
    t.fillcolor("lightgreen")
    t.begin_fill()
    t.left(30)
    t.forward(40)
    t.left(105)
    t.forward(100 / math.sqrt(2))
    t.left(75)
    t.forward(40)
    t.left(105)
    t.forward(40 / math.sqrt(2))
    t.left(45)
    t.end_fill()
    # Cancella il puntatore
    t.hideturtle()
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()

#Se la scelta ricade sul numero 1 allora lo script genererà la casa con questi parametri
  if scelta == 3:
    #Creazione della finestra
    screen = turtle.Screen()
    #Colore di sfondo
    screen.bgcolor("skyblue")

    #Creazione puntatore
    t = turtle.Turtle()
    #Colore puntatore
    t.color("black")
    t.shape("turtle")
    #Velocità puntatore
    t.speed(10)

    # Riempimento e creazione Rettangoli
    # Dimensione e colore
    def drawRectangle(t, width, height, color):
      t.fillcolor(color)
      t.begin_fill()
      t.forward(width)
      t.left(90)
      t.forward(height)
      t.left(90)
      t.forward(width)
      t.left(90)
      t.forward(height)
      t.left(90)
      t.end_fill()
  
    # Riempimento e creazione Triangoli
    def drawTriangle(t, length, color):
      t.fillcolor(color)
      t.begin_fill()
      t.forward(length)
      t.left(135)
      t.forward(length / math.sqrt(2))
      t.left(90)
      t.forward(length / math.sqrt(2))
      t.left(135)
      t.end_fill()
  
    # Riempimento e creazione Parallelogrammi
    def drawParallelogram(t, width, height, color):
      t.fillcolor(color)
      t.begin_fill()
      t.left(30)
      t.forward(width)
      t.left(60)
      t.forward(height)
      t.left(120)
      t.forward(width)
      t.left(60)
      t.forward(height)
      t.left(90)
      t.end_fill()


    # Fronte casa
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    # Coordinate per la creazione del fronte casa 
    t.goto(-150, -120)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore 
    drawRectangle(t, 120, 130, "Red")

    # Tetto Frontale Casa
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    # Coordinate per la creazione del Tetto Frontale
    t.goto(-150, -20)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore
    drawRectangle(t, 120, 30, "black")

    

    # Porta
    # Il puntatore si muove sullo schermo ma non disegnaa
    t.penup()
    # Coordinate per la creazione della porta
    t.goto(-140, -120)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore
    drawRectangle(t, 80, 100, "Orange")

    # Tetto Frontale Casa
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    # Coordinate per la creazione del Tetto Frontale
    t.goto(-150, 10)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore
    drawTriangle(t, 120, "Yellow")

    # Parte laterale Casa
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    # Coordinate per la creazione della parte laterale della Casa
    t.goto(-30, -120)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore
    drawParallelogram(t, 42, 130, "Green")

    # Tetto Laterale Casa
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    t.goto(-30, 10)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore
    t.fillcolor("lightgreen")
    t.begin_fill()
    t.left(30)
    t.forward(40)
    t.left(105)
    t.forward(120 / math.sqrt(2))
    t.left(75)
    t.forward(40)
    t.left(105)
    t.forward(10 / math.sqrt(2))
    t.left(45)
    t.end_fill()
    # Cancella il puntatore
    t.hideturtle()
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()

    # Finestra
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    # Coordinate per la creazione della finestra
    t.goto(-20, -70)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore
    drawParallelogram(t, 25, 30, "Blue")

    # Fascia laterale
    # Il puntatore si muove sullo schermo ma non disegna
    t.penup()
    # Coordinate per la creazione della fascia laterale
    t.goto(-30, -20)
    # Il puntatore muovendosi sullo schermo disegna
    t.pendown()
    # Riempimento con colore
    drawParallelogram(t, 42, 30, "black")
# Se la scelta ricade sul numero 4 allora lo script chiederà la conferma per la chiusura del programma
  elif scelta == 4:
    exit();
