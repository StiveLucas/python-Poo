from enum import Enum
import os
                                                                                                                                                                          
os.system("cls || clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

#Aplicação.
print(f"Sexo: {Sexo.FEMININO}")
print(f"Sexo: {Sexo.FEMININO.name}")
print(f"Sexo: {Sexo.FEMININO.value}")

print("\n")

print(f"Sexo: {Sexo.MASCULINO}")
print(f"Sexo: {Sexo.MASCULINO.name}")
print(f"Sexo: {Sexo.MASCULINO.value}")