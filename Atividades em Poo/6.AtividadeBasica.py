import os

os.system("cls || clear")

class MenorIdadeError(Exception):
    pass

class Usuario:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.idadePermitida = 18

    def idadeDoUsuario(self) -> str:
        idadeUsuario = int(input("Digite sua idade: "))

        try:
            self._verificar_idade(idadeUsuario)

        except MenorIdadeError as erro:
            return f"Prezado Cliente: {erro}"
        
        return f"Idade acima de 18, Acesso Permitido!"
            
    def _verificar_idade(self) -> None:

        if self.idadeDoUsuario < self.idadePermitida:
            raise MenorIdadeError("Idade Minima permitida: 18 \nAcesso negado.")
        
class UsuarioFechada(Usuario):
    pass

#Instanciando classe.
usuario_fechado = UsuarioFechada("Lucas")

print(f"Nome: {usuario_fechado.nome}")
print(f"Idade: {usuario_fechado.idadeDoUsuario()}")