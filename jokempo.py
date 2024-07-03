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

def again():
    global cpu
    cpu = choice(['Pedra', 'Papel', 'Tesoura'])
    print(cpu)
    cpuLabel.place(x=5000)
    empateLabel.place(x=5000)
    derrotaLabel.place(x=5000)
    vitoriaLabel.place(x=5000)
    denovoButton.place(x=5000)
    pedraButton.place(x=80, y=70)
    papelButton.place(x=200, y=70)
    tesouraButton.place(x=320, y=70)

empateLabel = Label(tela, text="Empate", font=("Verdana 30 bold"))
vitoriaLabel = Label(tela, text="Vitoria", font=("Verdana 30 bold"))
derrotaLabel = Label(tela, text="Derrota", font=("Verdana 30 bold"))
cpuLabel = Label(tela, text=cpu, font=("Verdana 20"))
denovoButton = Button(tela, text="Jogar de novo", width=12, height=1, font=("Verdana 15"), command=again)



def pedra():
    global player
    player = 1
    pedraButton.place(x=5000)
    papelButton.place(x=5000)
    tesouraButton.place(x=5000)
    cpuLabel.pack(padx=10, pady=10)

    if cpu == 'Pedra':
        empateLabel.place(x=170, y=100)
    if cpu == 'Papel':
        derrotaLabel.place(x=170, y=100)
    if cpu == 'Tesoura':
        vitoriaLabel.place(x=170, y=100)

    denovoButton.place(x= 170, y=150)

def papel():
    global player
    player = 2
    pedraButton.place(x=5000)
    papelButton.place(x=5000)
    tesouraButton.place(x=5000)
    cpuLabel.pack(padx=10, pady=10)

    if cpu == 'Pedra':
        vitoriaLabel.place(x=170, y=100)
    if cpu == 'Papel':
        empateLabel.place(x=170, y=100)
    if cpu == 'Tesoura':
        derrotaLabel.place(x=170, y=100)

    denovoButton.place(x= 170, y=150)

def tesoura():
    global player
    player = 3
    pedraButton.place(x=5000)
    papelButton.place(x=5000)
    tesouraButton.place(x=5000)
    cpuLabel.pack(padx=10, pady=10)

    if cpu == 'Pedra':
        derrotaLabel.place(x=170, y=100)
    if cpu == 'Papel':
        vitoriaLabel.place(x=170, y=100)
    if cpu == 'Tesoura':
        empateLabel.place(x=170, y=100)

    denovoButton.place(x= 170, y=150)


jokempoLabel = Label(tela, text="Jokempo", font=("Verdana 20 bold"))
jokempoLabel.place(x=175, y=10)

pedraButton = Button(tela, text="Pedra", width=6, height=1, bd=5, font=("Verdana 20"), command=pedra)
pedraButton.place(x=80, y=70)

papelButton = Button(tela, text="Papel", width=6, height=1, bd=5, font=("Verdana 20"), command=papel)
papelButton.place(x=200, y=70)

tesouraButton = Button(tela, text="Tesoura", width=6, height=1, bd=5, font=("Verdana 20"), command=tesoura)
tesouraButton.place(x=320, y=70)

tela.mainloop()
