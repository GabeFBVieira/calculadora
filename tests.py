import unittest

from calculadora import soma,subtracao,divisao,multiplicacao,potenciacao


class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(10,5),15)
        self.assertEqual(soma(5,1),6)

    def test_subtracao(self):
        self.assertEqual(subtracao(5,5),0)
        self.assertEqual(subtracao(1,3),-2)
    
    def test_divisao(self):
        self.assertEqual(divisao(2,2),1)
        self.assertEqual(divisao(4,2),2)
    
    def test_multiplicacao(self):
        self.assertAlmostEqual(multiplicacao(10,10),100)
        self.assertAlmostEqual(multiplicacao(50,2),100)
    
    def test_potenciacao(self):
        self.assertAlmostEqual(potenciacao(2,10),1024)
        self.assertAlmostEqual(potenciacao(2,2),4)

    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divisao(0,0)


if __name__ == '__main__':
    unittest.main()