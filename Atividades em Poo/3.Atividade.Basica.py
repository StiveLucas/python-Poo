import os

os.system("cls || clear")

class Endereco:
    def __init__(self, logradouro: str, numero: str) -> None:
        self.logradouro = logradouro
        self.numero = numero

    def __str__(self) -> str:
        return f"\nEndereço: \nLogradouro: {self.logradouro} \nNúmero: {self.numero}"
    
    #Construtor
class Aluno:
    def __init__(self, nome: str, idade: int, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def __str__(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade} {self.endereco}"

#Instanciando
enderecos = Endereco("Rua", "333")
alunos = Aluno("Stive", 18, enderecos)
    
print(alunos)