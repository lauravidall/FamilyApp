from tkinter import *
import tkinter.messagebox

def pessoas():
    janela_pessoas = Tk()
    janela_pessoas.title("Pessoas Da Família")
    janela_pessoas.geometry("400x300")

    frame_pessoas = Frame(janela_pessoas)
    frame_pessoas.pack()

    listbox_pessoas = Listbox(frame_pessoas, height=8, width=50)
    listbox_pessoas.pack(side=LEFT, padx=10, pady=5)

    scrollbar_pessoas = Scrollbar(frame_pessoas)
    scrollbar_pessoas.pack(side=RIGHT, fill=Y)
    listbox_pessoas.config(yscrollcommand=scrollbar_pessoas.set)
    scrollbar_pessoas.config(command=listbox_pessoas.yview)

    entrada_pessoas = Entry(janela_pessoas, width=50)
    entrada_pessoas.pack(padx=10, pady=5)

    botao_pessoas = Button(janela_pessoas, text="Adicionar Membro", width=20, command=lambda: adicionar(entrada_pessoas, listbox_pessoas))
    botao_pessoas.pack(padx=10, pady=5)

    botao_pessoas = Button(janela_pessoas, text="Deletar Membro", width=20, command=lambda: deletar(listbox_pessoas))
    botao_pessoas.pack(padx=10, pady=5)

    janela_pessoas.mainloop()

def adicionar(entrada, listbox):
    pessoa = entrada.get()
    if pessoa != "" and pessoa != " ":
        listbox.insert(END, pessoa)
        entrada.delete(0, END)
    else:
        tkinter.messagebox.showwarning(title="Erro!", message="Escreva um nome na barra de entrada")

def deletar(listbox):
    try:
        index_pessoa = listbox.curselection()[0]
        listbox.delete(index_pessoa)
    except:
        tkinter.messagebox.showwarning(title="Erro!", message="Selecione um nome com seu mouse")

def salvar():
    return

def carregar():
    return