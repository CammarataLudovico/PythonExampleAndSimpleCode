import turtle
import math

print(" ==========================================================")
print("{Digita il numero corrispodente alla casa che vuoi generare}")
print(" ==========================================================\n\r")
print("1. Casa_1." "  ");
print("2. Casa_2." "  ");
print("3. Casa_3." "  ");
print("4. Esci dal programma.\n\r");

scelta = int(input("Scegli la versione della casa desiderata: "));
if (scelta>=1 and scelta<=4):
  if scelta == 1:
    screen = turtle.Screen()
    screen.bgcolor("White")

# creazione della tartaruga 
    t = turtle.Turtle()
    t.color("black")
    t.shape("turtle")
    t.speed(5)

# funzione per il riempimento dei rettangoli
# dimensione e colore
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
  
# definizioen di una funzipone per la crazione e il rimepimento dei triangoli
# i triangoli assumono le colorazioni scelte
# possiamo usarlo per la creazioen del tetto.
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
  
# definire una funzioen per la creazioen di un parallelogrammo
# per disegnare il lato della casa
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


# disegna il fronte della casa
    t.penup() 
    t.goto(-150, -120)
    t.pendown()
    drawRectangle(t, 100, 110, "blue")

# disegna il fronte della porta
    t.penup()
    t.goto(-120, -120)
    t.pendown()
    drawRectangle(t, 40, 60, "lightgreen")

# tetto frontale
    t.penup()
    t.goto(-150, -10)
    t.pendown()
    drawTriangle(t, 100, "magenta")

# lato della casa
    t.penup()
    t.goto(-50, -120)
    t.pendown()
    drawParallelogram(t, 60, 110, "yellow")
    t.penup() 
    t.goto(-150, -35)
    t.pendown()
    drawRectangle(t, 100, 25, "Green")

# finestra
    t.penup()
    t.goto(-30, -60)
    t.pendown()
    drawParallelogram(t, 20, 30, "brown")
# lato della casa
    t.penup()
    t.goto(-50, -35)
    t.pendown()
    drawParallelogram(t, 60, 25, "Green")

# tetto laterale
    t.penup()
    t.goto(-50, -10)
    t.pendown()
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
    t.hideturtle()
    t.penup()

  if scelta == 2:
    screen = turtle.Screen()
    screen.bgcolor("skyblue")

# creazione della tartaruga 
    t = turtle.Turtle()
    t.color("black")
    t.shape("turtle")
    t.speed(8)

# funzione per il riempimento dei rettangoli
# dimensione e colore
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
  
# definizioen di una funzipone per la crazione e il rimepimento dei triangoli
# i triangoli assumono le colorazioni scelte
# possiamo usarlo per la creazioen del tetto.
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
  
# definire una funzioen per la creazioen di un parallelogrammo
# per disegnare il lato della casa
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


# disegna il fronte della casa
    t.penup() 
    t.goto(-150, -120)
    t.pendown()
    drawRectangle(t, 100, 110, "Yellow")

    t.penup() 
    t.goto(-150, -35)
    t.pendown()
    drawRectangle(t, 100, 25, "Purple")

    

# disegna il fronte della porta
    t.penup()
    t.goto(-140, -120)
    t.pendown()
    drawRectangle(t, 60, 85, "Orange")

# tetto frontale
    t.penup()
    t.goto(-150, -10)
    t.pendown()
    drawTriangle(t, 100, "red")

# lato della casa
    t.penup()
    t.goto(-50, -120)
    t.pendown()
    drawParallelogram(t, 40, 110, "Green")

# finestra
    t.penup()
    t.goto(-40, -70)
    t.pendown()
    drawParallelogram(t, 20, 30, "magenta")
# lato della casa
    t.penup()
    t.goto(-50, -35)
    t.pendown()
    drawParallelogram(t, 40, 25, "purple")
    

# tetto laterale
    t.penup()
    t.goto(-50, -10)
    t.pendown()
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
    t.hideturtle()
    t.penup()


if scelta == 3:
    screen = turtle.Screen()
    screen.bgcolor("skyblue")

# creazione della tartaruga 
    t = turtle.Turtle()
    t.color("black")
    t.shape("turtle")
    t.speed(10)

# funzione per il riempimento dei rettangoli
# dimensione e colore
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
  
# definizioen di una funzipone per la crazione e il rimepimento dei triangoli
# i triangoli assumono le colorazioni scelte
# possiamo usarlo per la creazioen del tetto.
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
  
# definire una funzioen per la creazioen di un parallelogrammo
# per disegnare il lato della casa
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


# disegna il fronte della casa
    t.penup() 
    t.goto(-150, -120)
    t.pendown()
    drawRectangle(t, 120, 130, "Red")

    t.penup() 
    t.goto(-150, -20)
    t.pendown()
    drawRectangle(t, 120, 30, "black")

    

# disegna il fronte della porta
    t.penup()
    t.goto(-140, -120)
    t.pendown()
    drawRectangle(t, 80, 100, "Orange")

# tetto frontale
    t.penup()
    t.goto(-150, 10)
    t.pendown()
    drawTriangle(t, 120, "Yellow")

# lato della casa
    t.penup()
    t.goto(-30, -120)
    t.pendown()
    drawParallelogram(t, 42, 130, "Green")

# tetto laterale
    t.penup()
    t.goto(-30, 10)
    t.pendown()
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
    t.hideturtle()
    t.penup()

# finestra
    t.penup()
    t.goto(-20, -70)
    t.pendown()
    drawParallelogram(t, 25, 30, "Blue")
# lato della casa
    t.penup()
    t.goto(-30, -20)
    t.pendown()
    drawParallelogram(t, 42, 30, "black")

elif scelta == 4:
    exit();
