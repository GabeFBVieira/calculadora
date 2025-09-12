def soma(num1,num2):
    return num1 + num2

def subtracao(num1,num2):
    return num1 - num2

def multiplicacao(num1,num2):
    return num1 * num2

def divisao(num1,num2):
    return num1 / num2

def potenciacao(num1,num2):
        
    return num1 ** num2

if __name__ == '__main__':
  
    while True: 
            
        print('-----------------------')
        print('      Calculadora       ')
        print('1. Soma')
        print('2. Subtração')
        print('3. Multiplicação')
        print('4. Divisão')
        print('5. Potenciação')
        print('6. Sair')
        print('----------------------')
        
        num1 = int(input('Digite um Numero: '))
        num2 = int(input('Digite um Numero: '))
        escolha = input('Qual operação deseja executar? Escolha um numero de 1 a 5  ')
        
        numeros_validos = None
        
        try:
            num1_float = float(num1)
            num2_float = float(num2)
            numeros_validos = True
        except:
            numeros_validos = None
        
        if numeros_validos is None:
            print('Um ou ambos os numeros digitados são invalidos')
            continue
        
        operadores_permitidos = '12345'
        
        if escolha not in operadores_permitidos:
            print('operador inválido, tente novamente')
            continue
        
        if escolha == '1':
            print(soma(num1_float,num2_float))
        elif escolha == '2':
            print(subtracao(num1_float,num2_float))
        elif escolha == '3':
            print(multiplicacao(num1_float,num2_float))
        elif escolha == '4':
            print(divisao(num1_float,num2_float))
        elif escolha == '5':
            print(potenciacao(num1_float,num2_float)) 
        
        
        sair= (input('Deseja sair? [s]im ou [n]ão ').lower().startswith('s'))
            
        if sair is True:
            print('Saindo...')
            break
        else:
            
            continue