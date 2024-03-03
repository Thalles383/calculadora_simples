from decimal import Decimal


class Calculadora:

    def adicao(self, x, y):
        # Função para realizar a adição de dois números
        return x + y

    def subtracao(self, x, y):
        # Função para realizar a subtração de dois números
        return x - y

    def multiplicacao(self, x, y):
        # Função para realizar a multiplicação de dois números
        return x * y

    def divisao(self, x, y):
        try:
            # Tenta realizar a divisão, tratando a exceção de divisão por zero
            return x / y
        except ZeroDivisionError:
            # Caso o denominador seja zero, retorna uma mensagem de erro.
            return "ERRO: Não é possível dividir por zero."

    def calcular(self, operador, x, y):
        # Verifica se o operador é válido
        if operador not in ["+", "-", "*", "/"]:
            return "ERRO: Operação inválida. Por favor, escolha +, -, * ou /."

        # Remove espaços e substitui vírgulas por pontos, se existirem.
        x, y = (str(x).strip().replace(",", "."), str(y).strip().replace(",", "."))

        # Tenta converter os valores de entrada em Decimal. Se não der certo, retorna mensagem de erro.
        try:
            x, y = (Decimal(x), Decimal(y))
        except:
            return "ERRO: Entrada inválida. Certifique-se de digitar números válidos."

        # Chama a função adequada de acordo com o operador e retorna o resultado.
        if operador == "+":
            return self.adicao(x, y)
        elif operador == "-":
            return self.subtracao(x, y)
        elif operador == "*":
            return self.multiplicacao(x, y)
        elif operador == "/":
            return self.divisao(x, y)
