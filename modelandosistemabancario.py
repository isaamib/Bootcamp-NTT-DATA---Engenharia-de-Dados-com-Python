class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class ContaBancaria:
    def __init__(self, cliente):
        self.cliente = cliente
        self.saldo = 0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para saque.")
        elif valor <= 0:
            print("Valor de saque deve ser positivo.")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def mostrar_extrato(self):
        print("\n=== Extrato Bancário ===")
        if not self.extrato:
            print("Nenhuma movimentação registrada.")
        else:
            for movimento in self.extrato:
                print(movimento)
        print(f"Saldo Atual: R$ {self.saldo:.2f}")
        print("=========================")

def main():
    nome_cliente = input("Digite o nome do cliente: ")
    cpf_cliente = input("Digite o CPF do cliente: ")
    cliente = Cliente(nome_cliente, cpf_cliente)
    conta = ContaBancaria(cliente)

    while True:
        print("\n=== Menu ===")
        print("1. Depósito")
        print("2. Saque")
        print("3. Extrato")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor do depósito: R$ "))
            conta.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor do saque: R$ "))
            conta.sacar(valor)
        elif opcao == '3':
            conta.mostrar_extrato()
        elif opcao == '4':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
