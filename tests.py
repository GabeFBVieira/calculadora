import unittest

from calculadora import soma,subtracao,divisao,multiplicacao,potenciacao, escolher_operacao


class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(10,5),15)
        self.assertEqual(soma(5,1),6)
        self.assertEqual(soma(0,0),0)
        self.assertEqual(soma(5,0),5)

    def test_subtracao(self):
        self.assertEqual(subtracao(5,5),0)
        self.assertEqual(subtracao(1,3),-2)
        self.assertEqual(subtracao(-1,0),-1)
        self.assertEqual(subtracao(-10,4),-14)
    
    def test_divisao(self):
        self.assertEqual(divisao(2,2),1)
        self.assertEqual(divisao(4,2),2)
        self.assertEqual(divisao(8,-1),-8)
        
    
    def test_multiplicacao(self):
        self.assertAlmostEqual(multiplicacao(10,10),100)
        self.assertAlmostEqual(multiplicacao(50,2),100)
        self.assertAlmostEqual(multiplicacao(-10,50),-500)
        self.assertEqual(multiplicacao(10,0),0)
    
    def test_potenciacao(self):
        self.assertAlmostEqual(potenciacao(2,10),1024)
        self.assertAlmostEqual(potenciacao(2,2),4)

    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divisao(5,0)
    
    def test_escolha(self):
        self.assertEqual(escolher_operacao('7','8','9'),'Operador inválido, tente novamente')
    
    def test_numero(self):
        self.assertEqual(escolher_operacao('a','b','c'),'Um ou ambos os números digitados são inválidos')

if __name__ == '__main__':
    unittest.main()