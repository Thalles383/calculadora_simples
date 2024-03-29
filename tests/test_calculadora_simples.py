import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self) -> None:
        self.calc_simples = Calculadora()
    
    #Deve retornar a soma correta de dois números.
    def test_somar_dois_numeros_corretamente(self):
        self.assertEqual(self.calc_simples.adicao(10, 10), 20)
    
    #Deve retornar a subtração correta de dois números.
    def test_subtrair_dois_numeros_corretamente(self):
        self.assertEqual(self.calc_simples.subtracao(20, 10), 10)
    
    #Deve retornar o produto correto de dois números.
    def test_retornar_produto_corretamente(self):
        self.assertEqual(self.calc_simples.multiplicacao(5, 10), 50)
    
    #Deve retornar o resultado correto da divisão de dois números.
    def test_retornar_resultado_divisao_corretamente(self):
        self.assertAlmostEqual(self.calc_simples.divisao(15, 3.25), 4.615, places=2)
    
    #Deve retornar a mensagem de erro adequada ao tentar dividir por zero.
    def test_retornar_erro_ao_dividir_por_zero(self):
        resultado = self.calc_simples.divisao(20, 0)
        self.assertEqual(resultado, "ERRO: Não é possível dividir por zero.")

    #Deve retornar o resultado correto para operadores válidos.
    def test_retornar_resultado_corretamente_para_operadores_validos(self):
        self.assertEqual(self.calc_simples.calcular("+", 10, 10), 20)
        self.assertEqual(self.calc_simples.calcular("-", 20, 10), 10)
        self.assertEqual(self.calc_simples.calcular("*", 3, 10), 30)
        self.assertEqual(self.calc_simples.calcular("/", 20, 2), 10)
    
    #Deve retornar a mensagem de erro apropriada para operador inválido.
    def test_retornar_mensagem_erro_apropriada_para_operadores_invalidos(self):
        resultado = self.calc_simples.calcular("abc", 123, 456)
        self.assertEqual(resultado, "ERRO: Operação inválida. Por favor, escolha +, -, * ou /.")

    #Deve retornar a mensagem de erro apropriada para entradas inválidas.
    def test_retornar_mensagem_erro_apropriada_para_entrada_invalidas(self):
        resultado = self.calc_simples.calcular("+", "abc", "def")
        self.assertEqual(resultado, "ERRO: Entrada inválida. Certifique-se de digitar números válidos.")

if __name__ == "__main__":
    unittest.main()
