import matplotlib.pyplot as plt
from collections import Counter
import os
# Realizando os imports necessarios para o uso da aplicação.

# Criando a Classe Livro.
class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

#array vazio onde será inserido os livros.
livros = []

# função para cadastrar um novo livro.
def cadastrar_livro(titulo, autor, genero, quantidade):
    livro = Livro(titulo, autor, genero, quantidade)
    livros.append(livro)

# função para listar os livros do sistema.
def listar_livros():
    for livro in livros:
        print(f'Título: {livro.titulo}, Autor: {livro.autor}, Gênero: {livro.genero}, Quantidade: {livro.quantidade}')

# função para buscar um livro pelo titulo.
def buscar_livro(titulo):
    for livro in livros:
        if livro.titulo.lower() == titulo.lower():
            return livro
    return None

# função para gerar um gráfico utilizando o Matplotlib
def gerar_grafico_por_genero():
    generos = [livro.genero for livro in livros]
    contagem = Counter(generos)
    plt.bar(contagem.keys(), contagem.values())
    plt.xlabel('Gênero')
    plt.ylabel('Quantidade')
    plt.title('Quantidade de Livros por Gênero')
    plt.show()

# função para encerrar a aplicação e limpar o terminal após o encerramento.
def finalizar_app():
    # para limpar o terminal assim que a opção for escolhida
    os.system('cls')
    print("Saindo do sistema...")

# Cadastrando alguns livros...
cadastrar_livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 'ficção', 5)
cadastrar_livro('Duna', 'Frank Herbert', 'ficção', 2)
cadastrar_livro('A culpa é das Estrelas', 'John Green', 'romance', 3)
cadastrar_livro('A Coisa', 'Stephen King', 'terror', 4)
cadastrar_livro('Carrie', 'Stephen King', 'terror', 1)
cadastrar_livro('O vilarejo', 'Raphael Montes', 'terror', 3)

# função onde será feito os testes da aplicação.
def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Buscar livro")
        print("4. Gerar gráfico de gêneros")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            genero = input("Gênero: ")
            quantidade = int(input("Quantidade: "))
            cadastrar_livro(titulo, autor, genero, quantidade)
            print("Livro cadastrado com sucesso!")

        elif opcao == '2':
            print("Livros disponíveis:")
            listar_livros()

        elif opcao == '3':
            titulo_busca = input("Digite o título do livro: ")
            livro_encontrado = buscar_livro(titulo_busca)
            if livro_encontrado:
                print(f'Livro encontrado: {livro_encontrado.titulo} por {livro_encontrado.autor}')
            else:
                print('Livro não encontrado.')

        elif opcao == '4':
            gerar_grafico_por_genero()

        elif opcao == '5':
            finalizar_app()
            break

        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o sistema.
menu()



