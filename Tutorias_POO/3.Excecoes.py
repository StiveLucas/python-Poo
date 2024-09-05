import os

os.system("cls || clear")

class Conta:
    def __init__(self, numero_conta: int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 0 # Atributo protegido.

    #Semelhante ao getSaldo().
    @property
    def saldo(self):
        return self._saldo
    
    def sacar(self, valor):
        self._saldo -= valor
        return self._saldo
    
    def depositar(self, valor):
        self._saldo += valor

class ContaCorrente(Conta):
    pass


class ContaPoupanca(Conta):
    pass

#Instanciando classe.
conta_corrente = ContaCorrente(222,333)

print(f"Número da Conta: {conta_corrente.numero_conta}")
print(f"Saldo: {conta_corrente._saldo}")