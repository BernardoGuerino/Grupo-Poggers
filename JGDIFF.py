#vitotoso
import csv
import datetime
livros=[]
pessoas=[]

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











#BernardoGuerino
