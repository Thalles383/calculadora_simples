from decimal import Decimal
from os import system, name
from calculadora import Calculadora


def limpar_tela():
    # Verifica o sistema operacional e executa o comando apropriado para limpar a tela
    if name == "nt":  # Windows
        system("cls")
    else:  # Mac e Linux
        system("clear")


def main():
    # Inicializa a calculadora
    calculadora = Calculadora()

    limpar_tela()

    # Apresenta o cabeçalho da calculadora
    print("=" * 40)
    print(f"{'Calculadora Simples':^40}")
    print("=" * 40, end="\n\n")

    # Solicita a operação e os dois números ao usuário
    operador = input("Escolha a operação (+, -, *, /): ")
    x = input("Digite o primeiro número: ")
    y = input("Digite o segundo número: ")

    # Calcula o resultado usando a função calcular
    resultado = calculadora.calcular(operador, x, y)

    # Verifica se o resultado é um número decimal, indicando sucesso no cálculo
    if type(resultado) is Decimal:
        # Converte o resultado em string e formata para o padrão brasileiro.
        resultado = f"O resultado da operação é: {str(resultado).replace('.', ',')}"

    # Exibe o resultado com uma linha de separação
    print("-" * len(resultado))
    print(resultado)
    print("-" * len(resultado))


if __name__ == "__main__":
    # Chama a função principal quando o script é executado
    main()
