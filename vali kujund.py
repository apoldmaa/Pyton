# Infot leidsin siit: https://docs.python.org/3/library/turtle.html
#mõne asjaga aitas chatGPT ka
#kujundite värvmiseks kasutasin fantaasiat



import turtle



lubatud_sõnad = ['viisnurk', 'ruut', 'ring', 'suvaline'] #ainult nendest sõnadest vali

while True:
    kujunditüüp = input("Vali kujundi tüüp (viisnurk, ruut, ring, suvaline): ").lower()

# Kontrollib
    if kujunditüüp in lubatud_sõnad:
        break

    print("Vale sisend! Palun sisesta: viisnurk, ruut, ring või suvaline.")

try:
    arv = int(input("Kui palju kujundeid soovid joonistada: "))
    if arv <= 0:
        print("Sisestatud arv ei tohi olla 0 või negatiivne. Seadistan 1-ks.")
        arv = 1
except ValueError:
    print("Vigane sisend, kasutame arvu 1.")
    arv = 1
 
t = turtle.Turtle()

t.fillcolor('red')
t.begin_fill()  
 
import random

for _ in range(arv):
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    size = random.randint(50, 50)
    if kujunditüüp == 'suvaline':
        tüüp = random.choice(['viisnurk', 'ring', 'ruut'])
    else:
        tüüp = kujunditüüp
    
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    if tüüp == 'viisnurk':
        t.begin_fill()
        for _ in range(5):
            t.forward(size)
            t.right(144)
        t.end_fill()
    elif tüüp == 'ring':
        t.fillcolor('red')
        t.begin_fill()
        t.circle(size)
        t.end_fill()
    elif tüüp == 'ruut':
        t.fillcolor('red')
        t.begin_fill()
        for _ in range(4):
            t.forward(size)
            t.right(90)
        t.end_fill()

turtle.done()
