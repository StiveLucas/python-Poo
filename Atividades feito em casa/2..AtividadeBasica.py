import os
from abc import ABC, abstractmethod

os.system("cls || clear")

class Pessoas(ABC):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__()
        self.nome = nome
        self.idade = idade

class Cliente(Pessoas):
    def __init__(self, nome: str, idade: int, dataDeCompra: str, formaDeCompartamento: str) -> None:
        super().__init__(nome, idade)
        self.dataDeCompra = dataDeCompra
        self.formaDePagamento = formaDeCompartamento

    def __str__(self) -> str:
        return f"Cliente: \nNome: {self.nome} \nIdade: {self.idade} \nData de compra: {self.dataDeCompra} \nForma de Pagamento: {self.formaDePagamento}"
    
class Funcionario(Pessoas):
    def __init__(self, nome: str, idade: int, matricula: str, cargo: str, salario: float) -> None:
        super().__init__(nome, idade)
        self.matricula = matricula
        self.cargo = cargo
        self.salario = salario

    def __str__(self) -> str:
        return f"\n\nFuncionario: \nNome: {self.nome} Idade: {self.idade} \nMatrícula: {self.matricula} \nCargo: {self.cargo} \nSalário: R${self.salario}"


clientes = Cliente("Stive", 18, "02/07/2021", "Débito")
funcionarios = Funcionario("Lucas", 31, "7643.7634 - 98", "Caixa", 750.80)
    
print(clientes, funcionarios)