from tkinter import *
import os
##############################################################################################
carpetaDeTodosLosArchivos = os.path.dirname(__file__)
carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "logo")
##############################################################################################
ventana = Tk()
ventana.geometry("500x300")
ventana.title("Ejercicio N°3")
ventana.iconbitmap(os.path.join(carpetaLogo, "perropepsi.ico"))
tipotexto = "Comic Sans MS", 10, "italic"
##############################################################################################
Label(ventana, background="Brown1", text="~ VictoriaVMC", font=tipotexto,
      justify=CENTER).pack(side=BOTTOM, fill=BOTH, expand=False)
##############################################################################################
Label(ventana, text="Altura (metros)").place(x=105, y=30)
Label(ventana, text="Peso (kg)").place(x=135, y=60)

n1 = DoubleVar()
n2 = DoubleVar()

Entry(ventana, textvariable=n1).place(x=200, y=30)
Entry(ventana, textvariable=n2).place(x=200, y=60)

resultado = StringVar()

Entry(ventana, state="readonly", width=38,
      textvariable=resultado).place(x=200, y=160)


def imc():
    num1 = n1.get()
    num2 = n2.get()
    if (num1 > 0) and (num2 > 0):
        calculador = (num2/(num1*num1))
        if calculador < 18.5:
            texto = "Bajo peso."
        elif calculador < 24.9:
            texto = "Normal."
        elif calculador < 29.9:
            texto = "Sobrepeso."
        elif calculador < 34.8:
            texto = "Obesidad."
        elif calculador < 34.9:
            texto = "Obesidad I"
        elif calculador < 39.9:
            texto = "Obesidad II"
        else:
            texto = "Obesidad III"
        Label(ventana, text=f"Presenta {texto}").place(x=200, y=135)
        mostrar = round(calculador, 2)
    else:
        mostrar = "Los datos ingresados deben ser mayor a 0."
    return resultado.set(mostrar)


Button(ventana, text="Calcular IMC", command=imc, width=16).place(x=60, y=160)
ventana.mainloop()
