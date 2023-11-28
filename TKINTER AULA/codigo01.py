from tkinter import *

def mensagem():
    mensagem['text'] = "CADASTRO REALIZADO COM SUCESSO!"

tela = Tk()

tela.title("Tela de Cadastro")

tela_monitor_h = tela.winfo_screenheight()
tela_monitor_w = tela.winfo_screenwidth()

nome = Label(tela,text="NOME: ", font="Georgia").place(x=30, y=50)
email = Label(tela,text="EMAIL: ", font="Georgia").place(x=30, y=90)
telefone = Label(tela, text="TELEFONE: ", font="Georgia").place(x=30, y=130)
campo_nome = Entry(tela,width=50, font="Verdana").place(x=150,y=50)
campo_email = Entry(tela, width=50, font="Verdana").place(x=150, y=90)
campo_telefone = Entry(tela, width=50, font="Verdana").place(x=150, y=130)




botao = Button(tela,text="CADASTRAR", background="#000080", font="Arial 17 bold", fg="#fff", command= mensagem).place(x=150, y=180)

mensagem = Label(tela, text="")
mensagem.grid(column=0, row=2, padx=10, pady=10)


tela.geometry(f"{tela_monitor_w}x{tela_monitor_h}")
tela.mainloop()