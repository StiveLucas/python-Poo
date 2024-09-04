import os

os.system("cls || clear")

class Endereco:
    def __init__(self, logradouro: str, numero: str) -> None:
        self.logradouro = logradouro
        self.numero = numero

    def __str__(self) -> str:
        return f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero}"
    

class ContaBancaria:
    def __init__(self, banco: str, agencia: str, numeroDaConta: str, tipoDeConta: str, saldoAtual: float, limiteDisponivel: float) -> None:
        self.banco = banco
        self.agencia = agencia
        self.numeroDaConta = numeroDaConta
        self.tipoDaConta = tipoDeConta
        self.saldoAtual = saldoAtual
        self.limiteDisponivel = limiteDisponivel

    def __str__(self) -> str:
        return (f"Banco: {self.banco} \nAgência: {self.agencia} \nNumero da Conta: {self.numeroDaConta}" 
                 f"\nTipo de Conta: {self.tipoDaConta} \nSaldo Atual: R$ {self.saldoAtual} \nLimite Disponivel: R$ {self.limiteDisponivel}")
        

class Funcionarios:
    def __init__(self, codigoDoFuncionario: str, nome: str, endereco: Endereco, telefone: str, email: str, contaBanco: ContaBancaria) -> None:
        self.codigoDoFuncionario = codigoDoFuncionario
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.contaBancaria = contaBanco

    def __str__(self) -> str:
        return (f"Código do Funcionário: {self.codigoDoFuncionario} \nNome: {self.nome} \n\nEndereço: {self.endereco}"
                f"\n\nTelefone: {self.telefone} \nEmail: {self.email} \n\nConta Bancária: \n{self.contaBancaria}")
    
#intanciar
enderecos = Endereco("Rua", "333")
contaBancarias = ContaBancaria("Salvador Brasil", "PSP", "874.891", "Livre", 450.90, 9000)
funcionarios = Funcionarios("4534.8990", "Stive", enderecos, "71-6634.899", "luce@gmail.com", contaBancarias)

print(funcionarios)
        