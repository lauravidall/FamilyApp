from tkinter import *
import tkinter.messagebox

def listaTarefas():
    
    janela_lista_Tarefas = Tk()
    janela_lista_Tarefas.title("Lista De Tarefas")
    janela_lista_Tarefas.geometry("400x300")

    frame_lista_Tarefas = Frame(janela_lista_Tarefas)
    frame_lista_Tarefas.pack()

    listbox_lista_Tarefas = Listbox(frame_lista_Tarefas, height=8, width=50)
    listbox_lista_Tarefas.pack(side=LEFT, padx=10, pady=5)

    scrollbar_lista_Tarefas = Scrollbar(frame_lista_Tarefas)
    scrollbar_lista_Tarefas.pack(side=RIGHT, fill=Y)
    listbox_lista_Tarefas.config(yscrollcommand=scrollbar_lista_Tarefas.set)
    scrollbar_lista_Tarefas.config(command=listbox_lista_Tarefas.yview)

    lista_Tarefas = Entry(janela_lista_Tarefas, width=50)
    lista_Tarefas.pack(padx=10, pady=5)

    nome = Entry(janela_lista_Tarefas, width=50)
    nome.pack(padx=10, pady=5)

    botao_lista_Tarefas = Button(janela_lista_Tarefas, text="Adicionar Tarefa", width=20, command=lambda: adicionar(lista_Tarefas, nome, listbox_lista_Tarefas))
    botao_lista_Tarefas.pack(padx=10, pady=5)

    botao_lista_Tarefas = Button(janela_lista_Tarefas, text="Deletar Tarefa", width=20, command=lambda: deletar(listbox_lista_Tarefas))
    botao_lista_Tarefas.pack(padx=10, pady=5)

    janela_lista_Tarefas.mainloop()

def adicionar(tarefa, nome, listbox):
    tarefa = tarefa.get()
    nome = nome.get()
    if tarefa and nome:
        item = f"{tarefa} - {nome}"
        listbox.insert(END, item)
        tarefa.delete(0, END)
        nome.delete(0, END)
    else:
        tkinter.messagebox.showwarning(title="Erro!", message="Por favor, preencha tanto o nome da tarefa quanto o nome da pessoa.")

def deletar(listbox):
    try:
        index_Tarefas = listbox.curselection()[0]
        listbox.delete(index_Tarefas)
    except:
        tkinter.messagebox.showwarning(title="Erro!", message="Selecione um tarefa com seu cursor")

def salvar():
    return

def carregar():
    return