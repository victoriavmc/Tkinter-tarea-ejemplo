from tkinter import *
from tkinter.ttk import Combobox
import os
##############################################################################################
carpetaDeTodosLosArchivos = os.path.dirname(__file__)
carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "logo")
##############################################################################################
ventana = Tk()
ventana.geometry("500x300")
ventana.title("Ejercicio N°7")
ventana.iconbitmap(os.path.join(carpetaLogo, "perropepsi.ico"))
tipotexto = "Comic Sans MS", 10, "italic"
##############################################################################################
Label(ventana, background="Brown1", text="~ VictoriaVMC", font=tipotexto,
      justify=CENTER).pack(side=BOTTOM, fill=BOTH, expand=False)
##############################################################################################
listaCandidatos = ["Candidato 1", "Candidato 2", "Candidato 3"]
votos = [56, 8, 8]

Label(ventana, text="Candidatos").place(x=40, y=20)
Label(ventana, text="Candidato con más votos").place(x=40, y=150)
Label(ventana, text="Total de Votos").place(x=100, y=200)
Label(ventana, text="Votos").place(x=310, y=150)

limpiarCombo = StringVar()
combo = Combobox(ventana, width=25, state="readonly",
                 values=listaCandidatos, textvariable=limpiarCombo)
combo.place(x=140, y=20)

verVotos = StringVar()
votos_Totales = StringVar()
candidatoMasVotos = StringVar()
Entry(ventana, state="readonly", textvariable=candidatoMasVotos,
      width=20).place(x=180, y=150)
Entry(ventana, state="readonly", textvariable=votos_Totales,
      width=20).place(x=180, y=200)
Entry(ventana, state="readonly", textvariable=verVotos,
      width=20).place(x=350, y=150)


def seleccionCandidato():
    candidatoMayor = 0
    candidatoMax = ""
    diccionarioCandidatos = zip(listaCandidatos, votos)
    for clave, valor in diccionarioCandidatos:
        if valor > candidatoMayor:
            candidatoMayor = valor
            candidatoMax = clave
        elif valor == candidatoMayor:
            candidatoMax = " "
    return candidatoMax


def votosTotales():
    totalVotos = sum(votos)
    return totalVotos


def votosIndividuales():
    contar = 0
    nuevoVoto = 0
    for numeros in votos:
        if combo.current() == contar:
            nuevoVoto = numeros + 1
            votos[contar] = nuevoVoto
        contar += 1
    cantVotos = votosTotales()
    candidatomasVotado = seleccionCandidato()
    return verVotos.set(nuevoVoto), votos_Totales.set(cantVotos), candidatoMasVotos.set(candidatomasVotado)


def limpiar():
    contar = 0
    for index in votos:
        votos[contar] = 0
        contar += 1
    candidatomasVotado = seleccionCandidato()
    return limpiarCombo.set(""), verVotos.set(0), votos_Totales.set(0), candidatoMasVotos.set(candidatomasVotado)


Button(ventana, text="Votar", width=20,
       command=votosIndividuales).place(x=320, y=20)
Button(ventana, text="Limpiar", width=20, command=limpiar).place(x=320, y=200)

ventana.mainloop()
