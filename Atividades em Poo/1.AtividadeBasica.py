import os

#Comando para limpar tela
os.system("cls || clear")

#Construtor
class Aluno:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

#Instanciando clase
aluno = Aluno("Batman", 47)

print("Nome: ", aluno.nome)
print("Idade: ", aluno.idade)
