def ixibir_menu():
        print("bem vindo ao menu de cadastro")
        print("1 - cadastrar")
        print("2 - ver cadastro")
        print("3 - sair")
        print("-----------------------------")

def cadastrar_pessoa (cadastros):
        nome = input("Nome")
        idade = input("Idade")
        turma = input("Turma")
        curso = input("Curso")
        cadastros.append({"nome": nome, "idade" : idade, "turma" : turma, "curso" : curso})
        print("Cadastro realizado com sucesso!!!")