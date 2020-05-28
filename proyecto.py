#importar librerias necesarias
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle
import mysql.connector

#Ver si existe la base de datos

#Declaracion de funciones
def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

def crearconexion():
    # Uso de variables
    host = 'localhost'
    nombre = StringVar()
    usuario = StringVar()
    password = StringVar()
    plugin = 'mysql_native_password'

    def destruirventana():
        ventanaparaconexion.destroy()

    def nuevaconexion():
        nombre = campo.get()
        usuario = campo1.get()
        password = campo2.get()
        #messagebox.showinfo(message="Conexion creada con exito", title="Satisfactorio")
        if nombre == "":
            messagebox.showerror(title="Error Campo vacio",message="El campo nombre esta vacio")
        elif campo1.get() == "":
            messagebox.showerror(title="Error Campo vacio", message="El campo Usuario esta vacio")
        elif campo2.get() == "":
            messagebox.showerror(title="Error Campo vacio", message="El campo contraseña esta vacio")
            #messagebox.askokcancel(message="Desea continuar",title="otra vez")
        else:
            if nombre != "" and usuario != "" and password != "":
                # Crear nueva conexion
                nueva = mysql.connector.connect(
                    host=host,
                    user=usuario,
                    passwd=password,
                    auth_plugin=plugin
                )
                cursor = nueva.cursor()
                cursor.execute("CREATE DATABASE " + nombre)
                messagebox._show(title="BataBase Create", message="La Base de datos fue creado con exito")
                print(cursor)

                destruirventana()
                # Crear pestanas
                note = ttk.Notebook(ventanaprincipal)
                note.pack(fill='both', expand='yes')
                pestana1 = ttk.Frame(note)
                note.add(pestana1, text=nombre)

                # Creamos el scroll
                sroll = Scrollbar(note)

                # Creamos nuestro campo
                texarea = Text(pestana1, width=100, height=35, yscrollcommand=sroll.set)
                texarea.place(x=0, y=0)
                texarea.focus()
                sroll.config(command=texarea.yview)
                sroll.pack(side=RIGHT, fill=Y)

                def mensaje():
                    obtener = texarea.get("1.0", "end")
                    list = []
                    list.append(obtener)
                    texarea1 = Text(pestana1, width=34, height=20, wrap=WORD)
                    texarea1.place(x=807, y=0)
                    texarea1.configure(background='light grey')
                    for recorre in list:
                        if 'select' in recorre:
                            select = mysql.connector.connect(
                                host=host,
                                user=usuario,
                                passwd=password,
                                auth_plugin=plugin,
                                database=nombre
                            )
                            selecccionar = select.cursor()  
                            selecccionar.execute(recorre)
                            for fila in selecccionar:
                                texarea1.insert(1.0, fila)
                        elif 'insert' in recorre:
                            inser = mysql.connector.connect(
                                host=host,
                                user=usuario,
                                passwd=password,
                                auth_plugin=plugin,
                                database=nombre
                            )
                            ingresar = inser.cursor()
                            ingresar.execute(recorre)
                            inser.commit()
                            texarea1.insert(1.0, 'Se ha ingresado datos a la tabla')
                        elif 'update' in recorre:
                            upda = mysql.connector.connect(
                                host=host,
                                user=usuario,
                                passwd=password,
                                auth_plugin=plugin,
                                database=nombre
                            )
                            update = upda.cursor()
                            update.execute(recorre)
                            upda.commit()
                            texarea1.insert(1.0, 'se ha actualizado ', update.rowcount )
                        elif 'delete' in recorre:
                            dele = mysql.connector.connect(
                                host=host,
                                user=usuario,
                                passwd=password,
                                auth_plugin=plugin,
                                database=nombre
                            )
                            delete = dele.cursor()
                            delete.execute(recorre)
                            dele.commit()
                            texarea1.insert(1.0, "se ha eliminado ", delete.rowcount)
                        elif 'create table' in recorre:
                            crear = mysql.connector.connect(
                                host=host,
                                user=usuario,
                                passwd=password,
                                auth_plugin=plugin,
                                database=nombre
                            )
                            createtable = crear.cursor()
                            createtable.execute(recorre)
                            texarea1.insert(1.0, 'Tabla creada correctamente')
                        elif 'drop table' in recorre:
                            dro = mysql.connector.connect(
                                host=host,
                                user=usuario,
                                passwd=password,
                                auth_plugin=plugin,
                                database=nombre
                            )

                            drop = dro.cursor()
                            drop.execute(recorre)
                            texarea1.insert(1.0, 'se ha eliminado la tabla')
                        elif 'create user' in recorre:
                            creuser = mysql.connector.connect(
                                host=host,
                                user=usuario,
                                passwd=password,
                                auth_plugin=plugin,
                                database=nombre
                            )
                            crearuser = creuser.cursor()
                            crearuser.execute(recorre)
                            texarea1.insert(1.0, 'se ha creado el usuario')
                        elif 'alter user' in recorre:
                            alte = mysql.connector.connect(
                                host=host,
                                user=usuario,
                                passwd=password,
                                auth_plugin=plugin,
                                database=nombre
                            )
                            alteruser = alte.cursor()
                            alteruser.execute(recorre)
                            texarea1.insert(1.0, 'se ha alterado el usuario correctamente')
                        elif 'drop user' in recorre:
                            dropus = mysql.connector.connect(
                                host=host,
                                user=usuario,
                                passwd=password,
                                auth_plugin=plugin,
                                database=nombre
                            )
                            eliminaruser = dropus.cursor()
                            eliminaruser.execute(recorre)
                            dropus.commit()
                            texarea1.insert(1.0, 'Se ha eliminado correctamente el usuario')
                        elif 'create schema' in recorre:
                            crearsch = mysql.connector.connect(
                                host=host,
                                user=usuario,
                                passwd=password,
                                auth_plugin=plugin,
                                database=nombre
                            )
                            crearschema = crearsch.cursor()
                            crearschema.execute(recorre)
                            texarea1.insert(1.0, 'Schema creado')


                boton2 = Button(pestana1, text="Run", command=mensaje)
                boton2.place(x=900, y=500)

    ventanaparaconexion = Tk()
    ventanaparaconexion.title("Crear Nueva Conexion")
    ventanaparaconexion.geometry('500x200')
    center(ventanaparaconexion)

    label = Label(ventanaparaconexion, text="Nombre:")
    label.place(x=10, y=45)
    label1 = Label(ventanaparaconexion, text="Usuario:")
    label1.place(x=10, y=80)
    label2 = Label(ventanaparaconexion, text="Contraseña:")
    label2.place(x=10, y=110)

    campo = Entry(ventanaparaconexion, textvariable=nombre)
    campo.place(x=100, y=45)
    campo.focus()
    campo1 = Entry(ventanaparaconexion, textvariable=usuario)
    campo1.place(x=100, y=80)
    campo2 = Entry(ventanaparaconexion, textvariable=password, show="*")
    campo2.place(x=100, y=110)

    nombre = campo.get()

    boton = Button(ventanaparaconexion, text="Crear", bg='green', fg='white',  command=nuevaconexion)
    boton.place(x=350, y=160)
    boton1 = Button(ventanaparaconexion, bg='red', fg='white', text="Cerrar", command=destruirventana)
    boton1.place(x=420, y=160)

    ventanaparaconexion.mainloop()

#Crear nuestra ventana principal
ventanaprincipal = Tk()
#Le asignamos un titulo a nuesta ventana
ventanaprincipal.title('ORACLE DEVELOPER FOR MABE')
#Le damos las dimensiones que tendra la ventana
ventanaprincipal.geometry("1100x630")

#Crear el menu
barramenu = Menu(ventanaprincipal)
barra = Menu(barramenu)
barra.add_command(label="File")
barra.add_command(label="Edit")
barra.add_command(label="View")
barra.add_command(label="Navigate")
barra.add_command(label="Run")
barra.add_command(label="Source")
barra.add_command(label="Team")
barra.add_command(label="Tools")
barra.add_command(label="Windows")
barra.add_command(label="Help")
ventanaprincipal.config(background='gray', menu=barra)

#Boton
boton = Button(ventanaprincipal, text="Nueva Conexion", bg='green', fg='white', command=crearconexion)
boton.place(x=10, y=10)

#para mantener abierta nuesta ventana
center(ventanaprincipal)
ventanaprincipal.mainloop()