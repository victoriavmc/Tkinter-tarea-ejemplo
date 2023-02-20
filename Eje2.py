from tkinter import *
import os
##############################################################################################
carpetaDeTodosLosArchivos = os.path.dirname(__file__)
carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "logo")
##############################################################################################
ventana = Tk()
ventana.geometry("500x300")
ventana.title("Ejercicio N°2")
ventana.iconbitmap(os.path.join(carpetaLogo, "perropepsi.ico"))
tipotexto = "Comic Sans MS", 10, "italic"
##############################################################################################
Label(ventana, background="Brown1", text="~ VictoriaVMC", font=tipotexto,
      justify=CENTER).pack(side=BOTTOM, fill=BOTH, expand=False)
##############################################################################################
Label(ventana, text="TP1").place(x=105, y=30)
Label(ventana, text="TP2").place(x=105, y=60)
Label(ventana, text="Parcial").place(x=88, y=90)
Label(ventana, text="Integrador").place(x=70, y=120)

n1 = IntVar()
n2 = IntVar()
n3 = IntVar()
n4 = IntVar()

Entry(ventana, textvariable=n1).place(x=150, y=30)
Entry(ventana, textvariable=n2).place(x=150, y=60)
Entry(ventana, textvariable=n3).place(x=150, y=90)
Entry(ventana, textvariable=n4).place(x=150, y=120)

resultado=StringVar()
Entry(ventana, state="readonly", width=38, textvariable=resultado).place(x=150, y=180)

def promedio():
    num1 = n1.get()
    num2 = n2.get()
    num3 = n3.get()
    num4 = n4.get()
    if (num1 >= 0) and (num2 >= 0) and (num3 >= 0) and (num4 >= 0):
        promediar = (num1+num2+num3+num4)/4
    else:
        promediar = "Las Notas ingresadas deben ser mayor a 0."
    return resultado.set(promediar)

Button(ventana, text="Promedio", command=promedio, width=16).place(x=20, y=180)
ventana.mainloop()
