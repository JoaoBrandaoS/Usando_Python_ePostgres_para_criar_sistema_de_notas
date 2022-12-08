import psycopg2
from  BancoDeDados import DataBase

Banco = psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "postgres",
    database = "postgres"
)

MeuCursor = Banco.cursor()
Funcoes = DataBase()

sala = Funcoes.SelecionarTabela()

while True:
    opcao = int(input("Escolha a função desejada:\n[1]Adicionar ALuno\n[2]Mostrar Tabela"
                      "\n[3]Mudar Tabela\n[4]Sair\n"))
    if opcao == 4:
        break
    elif opcao == 3:
        sala = Funcoes.SelecionarTabela()

    elif opcao == 2:
        Tabela = Funcoes.MostrarDados(MeuCursor)
        for x in Tabela:
            print(x)

    elif opcao == 1:
        aluno = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do primeiro bimestre: "))
        nota2 = float(input("Digite a nota do segundo bimestre: "))
        nota3 = float(input("Digite a nota do terceiro bimestre: "))
        Funcoes.CopularTabela(MeuCursor,Banco,aluno,nota,nota2,nota3)
        while True:
            sair = int(input("Voce deseja adicionar outro aluno?\n[1]Sim\n[2]Não"))
            if sair == 2:
                break
            else:
                aluno = input("Digite  nome do proximo aluno: ")
                nota = float(input("Digite a nota do primeiro bimestre: "))
                nota2 = float(input("Digite a nota do segundo bimestre: "))
                nota3 = float(input("Digite a nota do terceiro bimestre: "))
                Funcoes.CopularTabela(MeuCursor, Banco, aluno, nota, nota2, nota3)

MeuCursor.close()




