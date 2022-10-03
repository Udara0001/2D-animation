from tkinter import *
import time
WIDTH=500
HEIGHT=500
xvelocity=4
yvelocity=5


window=Tk()

canvas=Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()



photo=PhotoImage(file="ball.png")
myphoto=canvas.create_image(0,0,image=photo,anchor=NW)

imagewidth=photo.width()
imageheight=photo.height()
while True:
    coordinates=canvas.coords(myphoto)
    print(coordinates)
    if(coordinates[0]>=(WIDTH-imagewidth) or coordinates[0]<0):
        xvelocity=-xvelocity
    if (coordinates[1] >= (HEIGHT - imageheight) or coordinates[1] < 0):
        yvelocity = -yvelocity
    canvas.move(myphoto,xvelocity,yvelocity)
    window.update()
    time.sleep(0.01)



window.mainloop()





