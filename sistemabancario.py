class SistemaBancario:
  def __init__(self):
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
  sistema = SistemaBancario()

  while True:
      print("\n=== Menu ===")
      print("1. Depósito")
      print("2. Saque")
      print("3. Extrato")
      print("4. Sair")

      opcao = input("Escolha uma opção: ")

      if opcao == '1':
          valor = float(input("Digite o valor do depósito: R$ "))
          sistema.depositar(valor)
      elif opcao == '2':
          valor = float(input("Digite o valor do saque: R$ "))
          sistema.sacar(valor)
      elif opcao == '3':
          sistema.mostrar_extrato()
      elif opcao == '4':
          print("Saindo do sistema.")
          break
      else:
          print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
  main()
