import os
os.system('cls')

from tkinter import *
from Pessoas import *
from ListaDeCompras import *
from ListaDeTarefas import *
from Eventos import *

janela = Tk() 
janela.title("FamilyApp")
janela.geometry("500x400")


textodeorientacao = Label(janela, text="Welcome to the FamilyApp", font="Arial 16")
textodeorientacao.pack(anchor=CENTER, pady=60, padx=10) #usar pack com anchor=center para centralizar a mensagem

botao_pessoas = Button(janela, text="Pessoas da Família", width=20, command=pessoas)
botao_pessoas.pack(padx=10, pady=5)

botao_lista_compras = Button(janela, text="Lista de Compras", width=20, command=listaCompras)
botao_lista_compras.pack(padx=10, pady=5)

botao_eventos = Button(janela, text="Eventos", width=20, command=eventos)
botao_eventos.pack(padx=10, pady=5)

botao_lista_tarefas = Button(janela, text="Lista de Tarefas", width=20, command=listaTarefas)
botao_lista_tarefas.pack(padx=10, pady=5)


janela.mainloop()