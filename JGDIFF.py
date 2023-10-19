#vitotoso
import csv
import datetime

def cadastrar_livro(livros):
    livro=input("Digite o nome do livro:  ")
    editora=input("Digite o nome da editora:  ")
    autor=input("Digite o nome do autor:  ")

    livro={
        'Titulo':livro,
        'Editora':editora,
        'Autor':autor  
    }
    livros.append(livro)
    cirar_livro_csv()
    print("LIVRO CADASTRADO COM SUCESSO!!")
    print("====================================")
    
def cadastrar_pessoa(pessoas):
    nome=input("Digite o nome da Pessoa:  ")
    telefone=input("Digite o telefone da pessoa:  ")
    email=input("Digite o email da pessoa:  ")
    
    pessoa={
        'Nome':nome,
        'Telefone':telefone,
        'Email':email
    }
    pessoas.append(pessoa)
    criar_pessoa_csv()
    print("PESSOA CADASTRADA COM SUCESSO!!!")
    print("=====================================")
emprestimos=[]
def Cadastrar_emprestimos(emprestimos):
    
    procurar_livro=input("Qual o nome do livro que vc deseja fazer o emprestimo:  ")
    procurar_pessoa=input("Qual o email da pessoa que vai pegar o livro:  ")
    dia=int(input("Dia do mes de vencimento:  "))
    mes=int(input("Mes de vencimento:  "))
    ano=int(input("Ano de vencimento:  "))
    
    for livro in livros:
        if procurar_livro == livro['Titulo']:
            
            procurar_livro=livro['Nomelvr']
        else:
            print("Esse Livro nao existe.")
            
    for pessoa in pessoas:
        if procurar_pessoa == pessoa['Email']:
            
            procurar_pessoa=pessoa['Email']
        
        else:
            
            print("Essa pessoa nao existe.")
            
    emprestimo={
        
        'Pessoa':procurar_pessoa,
        'Livro':procurar_livro,
        'Entrega':datetime(ano,mes,dia) 
    }
    emprestimos.append(emprestimo)
    criar_emprestimo_csv()
    print("Emprestimo cadastrado com sucesso.")
    
#DaNasser














#Githug-o
def editar_livros():
    leitor = csv.DictReader(open('arquivo_livros.csv', mode="r"))
    editlivro = input("Digite o nome do livro que deseja editar: ")

    for livro in leitor:
        if livro['Titulo'] == editlivro:
            livro['Titulo'] = input("Título: ")
            livro['Editora'] = input("Editora: ")
            livro['Autor'] = input("Autor: ")
        else:
            print("Livro não encontrado.")
    livros = leitor
    criar_livro_csv()

def editar_contatos():
    leitor = csv.DictReader(open('arquivo_livros.csv', mode="r"))
    editcontato = input("Digite o email do contato que deseja editar: ")

    for contato in leitor:
        if contato['Email'] == editcontato:
            contato['Nome'] = input("Nome: ")
            contato['Telefone'] = input("Telefone: ")
            contato['Email'] = input("Email: ")
        else:
            print("Livro não encontrado.")
    contatos = leitor
    criar_contato_csv()

def editar_emprestimos():
    leitor = csv.DictReader(open('arquivo_livros.csv', mode="r"))
    editemprestimo = input("Digite o nome do livro emprestado que deseja alterar: ")
    opc1 = int(input("Qual informação deseja alterar?\n1 - Pessoa;\n2 - Livro;\n3 - Entrega;\n4 - Todas.\n")) 

    for emprestimo in leitor:
        if emprestimo['Livro'] == editemprestimo:
            if opc1 == 1:
                emprestimo['Nome'] = input("Nome: ")
            elif opc1 == 2:
                emprestimo['Livro'] = input("Livro: ") 
            elif opc1 == 3: 
                dia = int(input("Digite o dia a previsão de devolução (dd): "))
                mes = int(input("Digite o mês a previsão de devolução (mm): "))
                ano = int(input("Digite o ano a previsão de devolução (aaaa): "))

                emprestimo['Entrega'] = datetime(ano,mes,dia)
            elif opc1 == 4:             
                emprestimo['Nome'] = input("Nome: ")
                emprestimo['Telefone'] = input("Telefone: ")
                emprestimo['Email'] = datetime(ano,mes,dia)
            else:
                print("Opção inválida!")
        else:
            print("Livro não encontrado.")
    emprestimos = leitor
    criar_emprestimo_csv()
#BernardoGuerino
from datetime import datetime

livros = []
pessoas = []
emprestimos = []
contatos = []



def imprimir_livros(livro):
    pesquisa= input("Digite o nome do livro !")
    for livro in livros :
        if livro['livro'] == pesquisa #????
        print(f"   Título  |   Editora   |      Autor(a)  ")    
        print(f"   {livros['Titulo']}  |   {livros['Editora']}   |   {livros['Autora']}")
        

def imprimir_pessoas(pessoa):
    pesquisa= input("Digite o seu email !")
    for pessoa in pessoas :
        if livro['livro'] == pesquisa #????
    print(f"   |   Nome  |   Telefone   |   E-mail ")       
    print(f"  |   {contatos['Nome']}  |   {contatos['Telefone']}   |   {contatos['Email']}")
        

def imprimir_emprestimos(emprestimo):
    pesquisa= input("Digite o nome do livro !")
    pesquisa= input("Digite email da pessoa em posso do livro !")
    for emprestimo in emprestimos 
    print(f"Email  |   Status  |   Livro  |   Detentor   |   Data emprestimo | Data devolução")
        if emprestimos['Devolucao'] < datetime.now():
            status = "Atrasado"
        else:
            status = "No prazo"

            print(f"{['Email']}  |    {status}  |   {emprestimos['Livro']}  |   {emprestimos['Pessoa']}   |   {emprestimos['Data']}")


