from tkinter import *
import customtkinter as ctk
from random import choice

tela = Tk()
tela.geometry('500x300')
tela.resizable(width=False, height=False)
tela.title('Jokempo')

player = 0
lista = ['Pedra', 'Papel', 'Tesoura']
cpu = choice(lista)
print(cpu)

def pedra():
    player = 1

def papel():
    player = 2

def tesoura():
    player = 3

def resultados():
    pedraButton.place(x=5000)
    papelButton.place(x=5000)
    tesouraButton.place(x=5000)
    cpuLabel = Label(tela, text=cpu, font=("Verdana 20"))
    cpuLabel.pack(padx=10, pady=100)
    empateLabel = Label(tela, text="Empate", font=("Verdana 30 bold"))
    vitoriaLabel = Label(tela, text="Vitoria", font=("Verdana 30 bold"))
    derrotaLabel = Label(tela, text="Derrota", font=("Verdana 30 bold"))

    if player == 1 and cpu == 'pedra':
        empateLabel.place(x=170, y=70)
    if player == 1 and cpu == 'papel':
        derrotaLabel.place(x=170, y=70)
    if player == 1 and cpu == 'tesoura':
        vitoriaLabel.place(x=170, y=70)
    if player == 2 and cpu == 'pedra':
        vitoriaLabel.place(x=170, y=70)
    if player == 2 and cpu == 'papel':
        empateLabel.place(x=170, y=70)
        
        def again():
            player = 0
            cpuLabel.place(x=5000)
            empateLabel.place(x=5000)
            derrotaLabel.place(x=5000)
            vitoriaLabel.place(x=5000)
            

        denovoButton = Button(tela, text="Jogar de novo", width=6, height=1, font=("Verdana 15"), command=again)
        denovoButton.place(x= 170, y=150)

jokempoLabel = Label(tela, text="Jokempo", font=("Verdana 20 bold"))
jokempoLabel.place(x=175, y=10)

pedraButton = Button(tela, text="Pedra", width=6, height=1, bd=5, font=("Verdana 20"), command=resultados)
pedraButton.place(x=80, y=70)

papelButton = Button(tela, text="Papel", width=6, height=1, bd=5, font=("Verdana 20"), command=resultados)
papelButton.place(x=200, y=70)

tesouraButton = Button(tela, text="Tesoura", width=6, height=1, bd=5, font=("Verdana 20"), command=resultados)
tesouraButton.place(x=320, y=70)






tela.mainloop()