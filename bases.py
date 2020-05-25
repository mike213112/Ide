#Importamos las librerias necesarias
from tkinter import *
from tkinter import ttk

def obtenervalor():
    value = texarea.get("1.0","end")
    print(value)

def crearconexion():
    labe = Label(ventana, text="Nombre de la conexion:" )
    labe.place(x=10,y=50)

    variable = StringVar()

    nom = Entry(ventana, textvariable=variable)
    nom.place(x=10,y=70)

    jala = nom.get()
    print(jala)

#Nuestra ventana principal
ventana = Tk()
ventana.title("ORACLE DEVELOPER FOR MABE")
ventana.geometry("1100x640+130+45")

listar = ["Abrir", "Nuevo", "Guardar", "Guardar Como", "Cerrar"]

#def ventananueva():
    #ventana2 = Tk()
    #ventana2.geometry("600x600-50-50")
    #ventana2.mainloop()

note = ttk.Notebook(ventana)
note.pack(fill='both',expand='yes')
fra = ttk.Frame(note)
fram = ttk.Frame(note)



def probar():
    
    valor = sting.get()
    print(valor)

sting = StringVar()
n = Entry(ventana,textvariable=sting)
n.place(x=100, y=100)

note.add(fra, text="hola")
note.add(fram, text="Prueba1")

pro = Button(fra, text="Prueba", command=probar)
pro.place(x=150,y=200)

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
var = StringVar()


#bot = Button(ventana,text="Crear", command=crearconexion)
#bot.place(x=10,y=10)

ventana.config(background='gray', menu=op)

ventana.mainloop()