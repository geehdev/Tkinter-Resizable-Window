from os.path import exists
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview


def inserir():
    # adiciona dados no treeview
    tree.insert('', END, values=(entry_nome.get(), entry_idade.get(), entry_fone.get()))
    
    entry_nome.delete(0, END)
    entry_idade.delete(0, END)
    entry_fone.delete(0, END)
    entry_nome.focus()

def deletar():
    v = tree.selection()[0]
    tree.delete(v)


def obter():
    v = tree.selection()[0]
    print(tree.item(v, 'values'))



if exists('dados_usuarios.txt') == False:
    """Reponsável por criar o arquivo txd"""
    open('dados_usuarios.txt', 'w').close()
else:
    pass



# programa principal
root = Tk()
root.title('Janela Redimensionável')
root.geometry('650x332+50+100')

labelFrame_cadastro = LabelFrame(root, text='Preencha', fg='#9a09b0' , bg='#9c8e9b', width=288, height=180, borderwidth=2, font=('Gabriola', 15, 'italic'))
labelFrame_cadastrados = LabelFrame(root, text='Dados Cadastrados', fg='#9a09b0' , bg='#9c8e9b', width=288, height=180, borderwidth=2, font=('Gabriola', 15, 'italic'))

var_nome = Label(labelFrame_cadastro, background='#9c8e9b', text='Nome', font=('Times', 10, 'bold',  'italic') )
var_idade = Label(labelFrame_cadastro, background='#9c8e9b', text='Idade', font=('Times', 10, 'bold',  'italic') )
var_fone = Label(labelFrame_cadastro, background='#9c8e9b', text='Telefone', font=('Times', 10, 'bold',  'italic') )

entry_nome = Entry(labelFrame_cadastro)
entry_idade = Entry(labelFrame_cadastro, justify=CENTER)
entry_fone = Entry(labelFrame_cadastro)

Button(labelFrame_cadastro, text='Inserir', bg='#255385', relief='raised', border=1, command=inserir).place(relx=0.02 ,rely=0.7, relwidth=0.96, relheight=0.15)
Button(root, text='Deletar', bg='#255385', relief='raised', border=1, command=deletar).place(relx=0.62 ,rely=0.9, relwidth=0.1, relheight=0.1)
Button(root, text='Obter', bg='#255385', relief='raised', border=1, command=obter).place(relx=0.8 ,rely=0.9, relwidth=0.1, relheight=0.1)

# Treeview
tree = Treeview(labelFrame_cadastrados, columns=('name_column', 'age_column', 'phone_column'),show='headings')

# configurando as colunas
tree.column('name_column', width=160, )
tree.column('age_column', width=40)
tree.column('phone_column', width=100)
#definindo os nomes das colunas
tree.heading('name_column', text='Nome', anchor=CENTER )
tree.heading('age_column', text='Idade', anchor=CENTER )
tree.heading('phone_column', text='Telefone', anchor=CENTER)


# posicionando os widgets
labelFrame_cadastro.place(relx=0.009, rely=0.04, relheight=0.85, relwidth=0.48 )
labelFrame_cadastrados.place(relx=0.489, rely=0.04, relheight=0.85, relwidth=0.5)

var_nome.place(relx=0.01, rely=0, relheight=0.19, relwidth=0.2)
var_idade.place(relx=0.01, rely=0.21, relheight=0.19, relwidth=0.2)
var_fone.place(relx=0.01, rely=0.42, relheight=0.19, relwidth=0.2)

entry_nome.place(relx=0.22, rely=0, relheight=0.12, relwidth=0.77 )
entry_idade.place(relx=0.22, rely=0.21, relheight=0.12, relwidth=0.1)
entry_fone.place(relx=0.22, rely=0.42, relheight=0.12, relwidth=0.30)

tree.place(relx=0.02 ,rely=0, relwidth=0.96, relheight=0.98)

root.config(background='#4f0c4b')
root.mainloop()