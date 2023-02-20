from tkinter import *
import os
##############################################################################################
carpetaDeTodosLosArchivos = os.path.dirname(__file__)
carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "logo")
##############################################################################################
ventana = Tk()
ventana.geometry("500x300")
ventana.title("Ejercicio N°6")
ventana.iconbitmap(os.path.join(carpetaLogo, "perropepsi.ico"))
tipotexto = "Comic Sans MS", 10, "italic"
##############################################################################################
Label(ventana, background="Brown1", text="~ VictoriaVMC", font=tipotexto,
      justify=CENTER).pack(side=BOTTOM, fill=BOTH, expand=False)
##############################################################################################
listadePelis = ["El Gato Con Botas: El Último Deseo", "Red", "M3GAN", "Garra"]

Label(ventana, text="Película").place(x=40, y=30)
nombrePeli = StringVar()
Entry(ventana, textvariable=nombrePeli, width=40).place(x=90, y=30)

def enlistar(plista):
    Label(ventana, bg="White", borderwidth=2, relief="groove",
          height=13, width=60).place(x=60, y=60)
    mostrar = ""
    for indice in plista:
        mostrar += "# "+indice+"\n"
    Label(ventana, text=mostrar, bg="White", justify=LEFT).place(x=65, y=65)

enlistar(listadePelis)

def agregarPelicula():
    nombre = nombrePeli.get()
    listadePelis.append(nombre)
    enlistar(listadePelis)

Button(ventana, text="Agregar", width=16,
       command=agregarPelicula).place(x=350, y=27)

ventana.mainloop()