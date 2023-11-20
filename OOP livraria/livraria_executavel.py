from Livraria import Livraria as l

def main():
    livros = l.livros
    clientes = l.clientes

    pessoa = l()
    livro_nome = l.login(pessoa,clientes)
    clientes[0].update({'nome do livro' : livro_nome})
    print(clientes)

if __name__ == '__main__':
    main()