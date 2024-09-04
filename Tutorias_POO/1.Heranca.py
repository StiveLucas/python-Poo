from abc import ABC, abstractmethod
import os

os.system("cls || clear")

class Funcionario(ABC):
    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario

    @abstractmethod #Decorador
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return f"\nNome: {self.nome} \nSalário: R$ {self.salario} \nSalário Final: R$ {self.salario_final()}"

class Motoboy(Funcionario):

    #Acréscimo de 10%
    BONIFICACAO = 1.1

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado

class Engenheiro(Funcionario):
    def __init__(self, nome: str, salario: float, crea: str) -> None:
        super().__init__(nome, salario)
        self.crea = crea

    #Acréscimo de 10%
    BONIFICACAO = 1.2

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado

#Intanciando classes.
motoboy = Motoboy("Stive", 890.75)
engenheiro = Engenheiro("Thiago", 2.00, "75853.90")

print(motoboy, engenheiro)