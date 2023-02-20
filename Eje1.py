from tkinter import *
import os
##############################################################################################
carpetaDeTodosLosArchivos = os.path.dirname(__file__)
carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "logo")
##############################################################################################
ventana = Tk()
ventana.geometry("500x300")
ventana.title("Ejercicio N°1")
ventana.iconbitmap(os.path.join(carpetaLogo, "perropepsi.ico"))
tipotexto = "Comic Sans MS", 10, "italic"
##############################################################################################
pesos = IntVar()
dolar = IntVar()

Label(ventana, text="Ingresar Pesos:").place(x=60, y=30)
Entry(ventana, textvariable=pesos).place(x=160, y=30)

Label(ventana, text="Ingresar Dólares:").place(x=52, y=120)
Entry(ventana, textvariable=dolar).place(x=160, y=120)

retorno1 = StringVar()
retorno2 = StringVar()

Entry(ventana, state="readonly", textvariable=retorno1).place(x=160, y=75)
Entry(ventana, state="readonly", textvariable=retorno2).place(x=160, y=155)

def pesoDolar():
    np = pesos.get()
    convertir = np * 400
    return retorno1.set(convertir)

def dolarPeso():
    nd = dolar.get()
    convertir = nd / 385
    return retorno2.set(convertir)

Button(ventana, text="Covertir Dólares", width=16, height=1,
       command=pesoDolar).place(x=20, y=70)
Button(ventana, text="Covertir Pesos", width=16,
       command=dolarPeso).place(x=20, y=150)

Label(ventana, background="Brown1", text="~ VictoriaVMC", font=tipotexto,
      justify=CENTER).pack(side=BOTTOM, fill=BOTH, expand=False)
ventana.mainloop()
