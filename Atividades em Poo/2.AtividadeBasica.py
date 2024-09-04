import os

#Comando para limpar tela
os.system("cls || clear")

class Pet:
    def __init__(self, nome: str, idade: int, raca: str, alimentacao: str) -> None:
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.alimentacao = alimentacao

    def exibir_dados(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade} \nRaça: {self.raca}  \nAlimento: {self.alimentacao}"

pets = Pet("Davi", 18, "Inferior", "Swadon")

print(pets.exibir_dados())
