from tkinter import *
import tkinter.messagebox

def eventos():
    janela_eventos = Tk()
    janela_eventos.title("Eventos Da Família")
    janela_eventos.geometry("400x300")

    frame_eventos = Frame(janela_eventos)
    frame_eventos.pack()

    listbox_eventos = Listbox(frame_eventos, height=8, width=50)
    listbox_eventos.pack(side=LEFT, padx=10, pady=5)

    scrollbar_eventos = Scrollbar(frame_eventos)
    scrollbar_eventos.pack(side=RIGHT, fill=Y)
    listbox_eventos.config(yscrollcommand=scrollbar_eventos.set)
    scrollbar_eventos.config(command=listbox_eventos.yview)

    entrada_eventos = Entry(janela_eventos, width=50)
    entrada_eventos.pack(padx=10, pady=5)

    botao_eventos = Button(janela_eventos, text="Adicionar Evento", width=20, command=lambda: adicionar(entrada_eventos, listbox_eventos))
    botao_eventos.pack(padx=10, pady=5)

    botao_eventos = Button(janela_eventos, text="Deletar Evento", width=20, command=lambda: deletar(listbox_eventos))
    botao_eventos.pack(padx=10, pady=5)

    janela_eventos.mainloop()

def adicionar(entrada, listbox):
    produto = entrada.get()
    if produto != "" and produto != " ":
        listbox.insert(END, produto)
        entrada.delete(0, END)
    else:
        tkinter.messagebox.showwarning(title="Erro!", message="Escreva um evento na barra de entrada")

def deletar(listbox):
    try:
        index_eventos = listbox.curselection()[0]
        listbox.delete(index_eventos)
    except:
        tkinter.messagebox.showwarning(title="Erro!", message="Selecione um evento com seu mouse")

def salvar():
    return

def carregar():
    return