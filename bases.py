#Importamos las librerias necesarias
from tkinter import *

#Nuestra ventana principal
ventana = Tk()
ventana.title("MABE")
ventana.geometry("1100x640+130+45")

listar = ["Abrir", "Nuevo", "Guardar", "Guardar Como", "Cerrar"]

#def ventananueva():
    #ventana2 = Tk()
    #ventana2.geometry("600x600-50-50")
    #ventana2.mainloop()

barramenu = Menu(ventana)

op = Menu(barramenu)
op.add_command(label="File")
op.add_command(label="Edit")
op.add_command(label="View")
op.add_command(label="Navigate")
op.add_command(label="Run")
op.add_command(label="Source")
op.add_command(label="Team")
op.add_command(label="Tools")
op.add_command(label="Windows")
op.add_command(label="Help")

sroll = Scrollbar(ventana)
#.place(x=1006,y=50)

texarea = Text(ventana, width=100, height=35, yscrollcommand=sroll.set)

texarea.place(x=200,y=0)
sroll.config(command=texarea.yview)
#sroll.place(x=100,y=0,filter=(Y))
sroll.pack(side=RIGHT,fill=Y)

#op.add_command(label="Nuevo")

ventana.config(background='gray', menu=op)



ventana.mainloop()