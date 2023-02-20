from tkinter import *
import os
##############################################################################################
carpetaDeTodosLosArchivos = os.path.dirname(__file__)
carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "logo")
##############################################################################################
ventana = Tk()
ventana.geometry("500x300")
ventana.title("Ejercicio N°5")
ventana.iconbitmap(os.path.join(carpetaLogo, "perropepsi.ico"))
tipotexto = "Comic Sans MS", 10, "italic"
##############################################################################################
Label(ventana, background="Brown1", text="~ VictoriaVMC", font=tipotexto,
      justify=CENTER).pack(side=BOTTOM, fill=BOTH, expand=False)
##############################################################################################
Label(ventana, text="Número 1").place(x=170, y=30)
Label(ventana, text="Número 2").place(x=170, y=60)
Label(ventana, text="Resultado").place(x=170, y=90)

n1 = IntVar()
n2 = IntVar()
re = StringVar()
Entry(ventana, textvariable=n1). place(x=250, y=30)
Entry(ventana, textvariable=n2). place(x=250, y=60)
Entry(ventana, state="readonly", textvariable=re).place(x=250, y=90)

def suma():
    num1 = n1.get()
    num2 = n2.get()
    resultado = num1 + num2
    return re.set(resultado)

def resta():
    num1 = n1.get()
    num2 = n2.get()
    resultado = num1 - num2
    return re.set(resultado)

def multi():
    num1 = n1.get()
    num2 = n2.get()
    resultado = num1 * num2
    return re.set(resultado)

def divi():
    num1 = n1.get()
    num2 = n2.get()
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("El Número 2 debe ser difente a 0.")
        resultado = "Infinito"
    return re.set(resultado)

def limpiar():
    return n1.set(0),n2.set(0), re.set(0)

Button(ventana, text="+", width=16, height=1, command=suma).place(x=90, y=150)
Button(ventana, text="-", width=16, height=1,
       command=resta).place(x=250, y=150)
Button(ventana, text="*", width=16, height=1,
       command=multi).place(x=250, y=180)
Button(ventana, text="/", width=16, height=1, command=divi).place(x=90, y=180)
Button(ventana, text="Limpiar", width=16, height=1,
       command=limpiar).place(x=250, y=220)

ventana.mainloop()
