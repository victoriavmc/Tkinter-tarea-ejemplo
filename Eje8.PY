from tkinter.ttk import *
from tkinter import *
import json
import os
##############################################################################################
carpetaDeTodosLosArchivos = os.path.dirname(__file__)
carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "logo")
##############################################################################################
ventana = Tk()
ventana.geometry("575x500")
ventana.title("Ejercicio N°8")
ventana.iconbitmap(os.path.join(carpetaLogo, "perropepsi.ico"))
##############################################################################################
tipotexto = "Comic Sans MS", 12, "italic"
tipotitulo = "Comic Sans MS", 12, "italic", "underline"
##############################################################################################
Label(ventana, background="Brown1", text="~ VictoriaVMC", font=tipotexto,
      justify=CENTER).pack(side=BOTTOM, fill=BOTH, expand=False)
##############################################################################################
with open('servidores.json') as f:
    diccionarioInformatica = json.load(f)
##############################################################################################


def menu():
    Label(ventana, text="Departamento de Informática",
          font=tipotitulo).place(x=125, y=20)
    Label(ventana, text="Mostrar información sobre:",
          font=tipotexto).place(x=40, y=50)
    Radiobutton(ventana, text="1 - Estado de un servidor determinado.", value=1,
                variable=seleccion, command=MostrarDatos, font=tipotexto).place(x=60, y=80)
    Radiobutton(ventana, text="2 - Cantidad de servidores según un estado determinado.",
                value=2, variable=seleccion, command=MostrarDatos, font=tipotexto).place(x=60, y=110)
    Radiobutton(ventana, text="3 - Cantidad de servidores.",
                value=3, variable=seleccion, command=MostrarDatos, font=tipotexto).place(x=60, y=140)
    Radiobutton(ventana, text="4 - Ver todos los servidores.",
                value=4, variable=seleccion, command=MostrarDatos, font=tipotexto).place(x=60, y=170)
    Radiobutton(ventana, text="5 - Ingresar un nuevo servidor.",
                value=5, variable=seleccion, command=MostrarDatos, font=tipotexto).place(x=60, y=200)


def listaSegun(pseleccion):
    listaMostrarCombo = []
    Label(ventana, text="Seleccionar:", font=tipotexto).place(x=80, y=268)
    for listas in diccionarioInformatica:
        for clave, valor in listas.items():
            if clave == pseleccion:
                if valor not in listaMostrarCombo:
                    listaMostrarCombo.append(valor)
    valorSeleccionado = IntVar()
    combo = Combobox(ventana, width="10", values=listaMostrarCombo,
                     state="readonly", textvariable=valorSeleccionado)
    combo.place(x=200, y=270)

    def comboboxFun():
        contador = 0
        for listas in diccionarioInformatica:
            for valor in listas.values():
                if (combo.get()) == valor:
                    if valor == "Activo" or valor == "Inactivo":
                        contador += 1
                    else:
                        contador = str('#')
                    estado = listas['Estado']
        mostrarEstadoContador = f"{contador} {estado}"
        Label(ventana, text=mostrarEstadoContador, width="10",
              font=tipotexto).place(x=200, y=370)
    Button(ventana, font=tipotexto, text="Enviar",
           command=comboboxFun).place(x=300, y=270)


def cantidadServidores(pContar):
    contar = 0
    for listas in diccionarioInformatica:
        for clave in listas:
            if clave == pContar:
                contar += 1
    return contar


def mostrarListas():
    Label(ventana, font=tipotitulo, text="Id").place(x=40, y=260)
    Label(ventana, font=tipotitulo, text="Servidor").place(x=110, y=260)
    Label(ventana, font=tipotitulo, text="IP").place(x=275, y=260)
    Label(ventana, font=tipotitulo, text="Estado").place(x=350, y=260)
    contador = 20
    for lista in diccionarioInformatica:
        for clave, valor in lista.items():
            if clave == 'Id':
                Label(ventana, text=valor, font=tipotexto,
                      justify=CENTER, width=3).place(x=65, y=260+contador)
            if clave == 'Servidor':
                Label(ventana, text=valor, font=tipotexto).place(
                    x=190, y=260+contador)
            if clave == 'IP':
                Label(ventana, text=valor, font=tipotexto).place(
                    x=300, y=260+contador)
            if clave == 'Estado':
                Label(ventana, text=valor, font=tipotexto).place(
                    x=410, y=260+contador)
                contador += 30


def MostrarDatos():
    separador = "☆…☆…☆…☆…☆…☆…☆…☆…☆…☆…☆…☆…☆…☆…☆…☆…☆…☆…☆"
    Label(ventana, width=100, height=15).place(x=10, y=230)
    Label(ventana, text=separador, font=tipotexto).place(x=40, y=230)
    Label(ventana, text=separador, font=tipotexto).place(x=40, y=440)

    opcion = seleccion.get()

    buscarSegun = "Servidor"
    if opcion == 1:
        listaSegun(buscarSegun)
    elif opcion == 2:
        buscarSegun = "Estado"
        listaSegun(buscarSegun)
    elif opcion == 3:
        Label(ventana, text=f"La cantidad de servidores es: \n {cantidadServidores(buscarSegun)}", font=tipotexto).place(
            x=120, y=280)
    elif opcion == 4:
        mostrarListas()
    else:
        cargarNuevo = cantidadServidores(buscarSegun)
        listadeJson = cargarNuevosServidores(
            diccionarioInformatica, cargarNuevo)
        with open("servidores.json", "w") as jsonfile:
            json.dump(listadeJson, jsonfile)


def cargarNuevosServidores(plistadeJson, NumeroNuevo):
    diccionarioP = dict()
    ident = NumeroNuevo + 1
    diccionarioP["Id"] = ident
    concatenaServidor = (f"Servidor{ident}")
    diccionarioP["Servidor"] = concatenaServidor
    concatenaIP = (f"{ident}.{ident}.{ident}.{ident}")
    diccionarioP["IP"] = concatenaIP
    Label(ventana, text="En que estado se encuentra? \n 1. Activo \n 2. Inactivo",
          font=tipotexto, justify=CENTER).place(x=100, y=270)
    r1 = IntVar()
    Entry(ventana, font=tipotexto, textvariable=r1, width=15).place(x=280, y=300)

    def tipoEstado():
        carga = True
        estado = r1.get()
        if estado == 1 or estado == 2:
            mensaje = "Carga realizada con exito!"
            if estado == 1:
                estad = "Activo"
            else:
                estad = "Inactivo"
                diccionarioP["Estado"] = estad
            plistadeJson.append(diccionarioP)
        else:
            carga = False
            mensaje = " ERROR DEBE INGRESAR: \n 1-ACTIVO O 2-INACTIVO"
        Label(ventana, text=mensaje, font=tipotexto,
              width=25, height=2).place(x=150, y=390)
        if carga:
            return (plistadeJson)

    Button(ventana, font=tipotexto, text="Cargar",
           command=tipoEstado).place(x=250, y=350)


#############################################################################################
seleccion = IntVar()
menu()
ventana.mainloop()
