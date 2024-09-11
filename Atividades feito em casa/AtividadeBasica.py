import os

os.system("clear || cls")

class MinhaClasse:

                # Self são obrigatorios.
    def meu_metodo(self):
        print("Estou no metodo!")

    def meu_metodo2(self, num, mult):
        return num * mult
    
class ClasseCompleta(MinhaClasse):
    pass

#Instanciando
classe_completa = ClasseCompleta()

print(classe_completa.meu_metodo())
print(classe_completa.meu_metodo2(4, 7))
