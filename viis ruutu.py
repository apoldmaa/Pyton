import turtle



r = turtle.Turtle() #r, et ei peaks pikalt välja kirjutama 

def ruut(x, y, kylg): #funktsioon ruutude joonistamiseks
    
    r.penup() #pliiats üles
    r.goto(x - kylg/2, y - kylg/2) # käsk pliiatsi liigutamiseks
    r.pendown() #pliiats alla
    
    for _ in range(4): #tähendab et kordab käsku 4 korda
        r.forward(80) # liigub edasi 
        r.right(90) # 90 kraadi

ruut(0, 0, 150)  #esimene ruut
ruut(150, 0, 100) #teine ruut
ruut(100, 80,80) #kolmas ruut
ruut(100, 180, 90) #neljas ruut
ruut(-100, 50, 80) #viies ruut

turtle.done()
