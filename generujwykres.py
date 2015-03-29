from generujeps import Eps

functionfile = open("funk.py", "w")
functionfile.write("def funkcja(x):")
f = raw_input("Podaj funkcje: f(x) = ")
#Z jakiegos powodu x**3 nie dziala. Nie wiem dlaczego ;_;, za to dzialaja wykladnicze, kwadratowe i liniowe.
functionfile.write("    return "+str(f))
functionfile.close()
from funk import funkcja


plik = Eps()
plik.openfile('wykres.eps', 1000, 1000)
plik.newpath()
plik.setcolor(0,0,1)
plik.setfont("Arial", 30)
plik.moveto(10, 970)
plik.write(str(f))
plik.closepath()
plik.stroke()


plik.newpath()
plik.setgray(0)
plik.linewidth(1)
for i in range(100):
    plik.drawline(1, 10*i, 1000, 10*i)
    plik.drawline(10*i, 1, 10*i, 1000)
plik.closepath()
plik.stroke()

plik.newpath()
plik.linewidth(3)
plik.drawline(1,500, 1000, 500)
plik.drawline(500, 1, 500, 1000)
plik.drawline(1000, 500, 990, 510)
plik.drawline(1000, 500, 990, 490)
plik.drawline( 500, 1000, 510, 990)
plik.drawline( 500, 1000, 490, 990)
plik.closepath()
plik.stroke()


plik.newpath()
plik.setcolor( 0, 1, 0)
plik.moveto(975, 460)
plik.write("X")
plik.closepath()
plik.stroke()

plik.newpath()
plik.moveto(460, 970)
plik.write("Y")
plik.closepath()
plik.stroke()



plik.newpath()
plik.moveto(-1, funkcja(-50.1)*10+500)

plik.linewidth(3)
plik.setcolor( 1, 0, 1)

for i in range(1000):
    plik.continueline(i, funkcja((i-500)/10.0)*10.0+500)
plik.closepath()
plik.stroke()

plik.closefile()
