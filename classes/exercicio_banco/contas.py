import abc


class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(F'(DEPOSITO {valor})')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f'o seu saldo é {self.saldo:.2f}{msg}')
        print('--')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'

        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(F'(SAQUE {valor})')
            return self.saldo

        print('Não foi possivel sacar o valor desejado')
        self.detalhes(F'(SAQUE NEGADO: valor do saque negado {valor})')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0, \
                 limite: float = 0) -> None:
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(F'(SAQUE {valor})')
            return self.saldo

        print('Não foi possivel sacar o valor desejado')
        print(f'seu limite de saque especial é {-self.limite:.2f}')
        self.detalhes(F'(SAQUE NEGADO: valor do saque negado {valor})')
        return self.saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"({self.agencia!r}, {self.conta!r}, {self.saldo!r}, "\
            f"{self.limite!r})"
        return f'{class_name}{attrs}'


if __name__ == '__main__':  # para não importar para o main
    print('POupança')
    cp1 = ContaPoupanca(111, 222, 100)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    print('Conta corrente')
    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(99)
    cc1.sacar(1)
    print('##')
    print(cc1.limite)