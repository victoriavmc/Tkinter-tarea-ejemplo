from tkinter import *
import os
from googletrans import Translator
##############################################################################################
carpetaDeTodosLosArchivos = os.path.dirname(__file__)
carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "logo")
##############################################################################################
ventana = Tk()
ventana.geometry("500x300")
ventana.title("Ejercicio N°4")
ventana.iconbitmap(os.path.join(carpetaLogo, "perropepsi.ico"))
tipotexto = "Comic Sans MS", 10, "italic"
##############################################################################################
Label(ventana, background="Brown1", text="~ VictoriaVMC", font=tipotexto,
      justify=CENTER).pack(side=BOTTOM, fill=BOTH, expand=False)
##############################################################################################
Label(ventana, text="Palabra").place(x=80, y=30)
palabra = StringVar()
Entry(ventana, textvariable=palabra).place(x=140, y=30)

resuelto=StringVar()
Entry(ventana, state="readonly", textvariable=resuelto).place(x=140, y=60)

traductor = Translator()

def traducctor():
    text = (palabra.get())
    traducido = (traductor.translate(text, dest='es', src="en").text)
    return resuelto.set(traducido)

Button(ventana, text="Traducción", command=traducctor).place(x=60, y=60)

ventana.mainloop()
