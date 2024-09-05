from enum import Enum
import os

os.system("cls || clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Setor(Enum):
    FINANCEIRO = "Financeiro"
    VENDAS = "Vendas"
    MARKETING = "Marketing"
    RECURSOS_HUMANOS = "Recursos Humanos"

class Funcionarios:
    def __init__(self, id: str, nome: str, salario: float, setor: Setor, sexo: Sexo, idade: int) -> None:

        self.id = id
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.setor = setor
        self.salario = salario

    def __str__(self) -> str:
        return f"Funcionário: \nID: {self.id} \nNome: {self.nome} \nSalário: R$ {self.salario} \nSetor: {self.setor} \nSexo: {self.sexo}"

#Instanciando
funcionario = Funcionarios("7864789-98", "Stive", 750.80, Setor.FINANCEIRO.value, Sexo.MASCULINO.value, 18)

print(funcionario)