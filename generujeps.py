class Eps:

    epsfile = None

    def openfile(self, filename, x, y):
        self.epsfile = open(filename, 'w')
        self.epsfile.write(r'%!PD-Adobe-3.0 EPSF-3.0'+'\n'+r'%%BoundingBox: 0 0 '+str(x)+' '+str(y)+' \n')

    def closefile(self):
        self.epsfile.close()
            
    def drawline(self, x, y, x2, y2):
        self.epsfile.write(str(x)+' '+str(y)+' moveto \n')
        self.epsfile.write(str(x2)+' '+str(y2)+' lineto \n')

    def continueline(self, x, y):
        self.epsfile.write(str(x)+' '+str(y)+' lineto \n')

    def linewidth(self, x):
        self.epsfile.write(str(x)+ ' setlinewidth \n')

    def newpath(self):
        self.epsfile.write('newpath \n')

    def closepath(self):
        self.epsfile.write('closepath \n')

    def stroke(self):
        self.epsfile.write('stroke \n')

    def showpage(self):
        self.epsfile.write('showpage \n')

    def fill(self):
        self.epsfile.write('fill \n')
            
    def arc(self, x, y, r, begin, end):
        self.epsfile.write(str(x)+' '+str(y)+' '+str(r)+' '+str(begin)+' '+str(end)+' arc \n')

    def setfont(self, font, size):
        self.epsfile.write('/'+font+' findfont \n'+str(size)+' scalefont \n setfont \n')

    def setcolor(self, r, g, b):
        self.epsfile.write(str(r)+' '+str(g)+' '+str(b)+' setrgbcolor \n')
            
    def setgray(self, g):
        self.epsfile.write(str(g)+' setgray')

    def fontsize(self, size):
        self.epsfile.write(str(size)+' scalefont \n')
        
    def clip(self):
        self.epsfile.write('clip \n')

    def write(self, string):
        self.epsfile.write('('+string+') show \n')
    
    def moveto(self, x, y):
        self.epsfile.write(str(x)+' '+str(y)+" moveto \n")

    def drawdot(self, x, y):
        self.arc(self, x, y, 1, 0, 360)







