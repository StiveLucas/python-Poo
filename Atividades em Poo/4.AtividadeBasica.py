from abc import ABC, abstractmethod
import os

os.system("cls || clear")

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero} \nComplemento: {self.complemento} \nCEP: {self.cep} \nCidade: {self.cidade}"

class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.salario = salario
        self.endereco = endereco

    def __str__(self) -> str:
        return f"\nNome: {self.nome} \nTelefone: {self.telefone} \nEmail: {self.email} \nSalário: {self.salario} \nEndereço:{self.endereco}"

class Engenheiro:
    def __init__(self, crea: str, funcionario: Funcionario) -> None:
        self.funcionario = funcionario
        self.crea = crea

#Instanciando.
