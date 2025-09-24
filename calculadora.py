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

def escolher_operacao(num1, num2, escolha):
   
    try:
        num1_float = float(num1)
        num2_float = float(num2)
    except ValueError:
        return "Um ou ambos os números digitados são inválidos"

    operadores_permitidos = '12345'
    if escolha not in operadores_permitidos:
        return "Operador inválido, tente novamente"

    if escolha == '1':
        return soma(num1_float, num2_float)
    elif escolha == '2':
        return subtracao(num1_float, num2_float)
    elif escolha == '3':
        return multiplicacao(num1_float, num2_float)
    elif escolha == '4':
        return divisao(num1_float, num2_float)
    elif escolha == '5':
        return potenciacao(num1_float, num2_float)


if __name__ == "__main__":  
    while True: 
                
            print('-----------------------')
            print('      Calculadora       ')
            print(' 1.Soma\n 2.Subtração\n 3.Multiplicação\n 4.Divisão\n 5.Potenciação\n 6.Sair')
            print('----------------------')
            
            num1 = int(input('Digite um Número: '))
            num2 = int(input('Digite um Número: '))
            escolha = input('Qual operação deseja executar? Escolha um número de 1 a 5  ')

            resultado = escolher_operacao(num1, num2, escolha)
            print('Resultado:', resultado)

            sair= (input('Deseja sair? [s]im ou [n]ão ').lower().startswith('s'))
                
            if sair is True:
                print('Saindo...')
                break
            else:
                
                continue


        

