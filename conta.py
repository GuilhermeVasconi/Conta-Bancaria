class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1


    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser postivo!')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo Insuficiente')
        else:
            print('O valor deve ser positivo')

conta1 = Conta('Matheus', 150.00, 2000)

conta1.depositar(1500)

print(conta1.__dict__)

conta1.sacar(1000)

print(conta1.__dict__)

conta1.extrato()
