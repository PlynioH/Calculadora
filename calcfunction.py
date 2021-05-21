print('Calculadora Iniciada!!!\n')
info = 1; soma = 0; sub = 0; mult = 0; div = 0; poten = 1; num1 = 0; num2 = 0

def calcular_soma(num1: float, num2: float, soma: float):
    num1 = float(input('\n\nDigite um Número: '))
    num2 = float(input('Digite outro Número: '))
    soma = num1 + num2
    print('A soma do número',num1,'com o número',num2,'resulta em',soma,'\n')

def calcular_subtracao(num1: float, num2: float, sub: float):
    num1 = float(input('\n\nDigite um Número: '))
    num2 = float(input('Digite outro Número: '))
    sub = num1 - num2
    print('A subtração do número',num1,'pelo o número',num2,'resulta em',sub,'\n')

def calcular_multiplicacao(num1: float, num2: float, mult: float):
    num1 = float(input('\n\nDigite um Número: '))
    num2 = float(input('Digite outro Número: '))
    mult = num1 * num2
    print('A multiplicação do número',num1,'pelo o número',num2,'resulta em',mult,'\n')

def calcular_divisao(num1: float, num2: float, div: float):
    num1 = float(input('\n\nDigite um Número: '))
    num2 = float(input('Digite outro Número: '))
    div = num1 / num2
    print('A divisão do número',num1,'pelo o número',num2,'resulta em',div,'\n')

def calcular_potencia(num1: float, num2: int, poten: float):
    num1 = float(input('\n\nDigite o Número da base que deseja elevar a uma potência: '))
    num2 = int(input('Digite o valor do expoente: '))
    for _ in range(0, num2):
        poten = poten * num1
    print('A potencia da base número ',num1,'elevada pelo o número',num2,'resulta em',poten,'\n')

while info == 1:
    op = int(input('Digite um número sendo\n1- para soma\n2- para subtração\n3- para multiplicação\n4- para divisão\n5- Para potenciação\n'))

    if op == 1: 
        calcular_soma(num1, num2, soma)

    if op == 2:
        calcular_subtracao(num1, num2, sub)

    if op == 3:
        calcular_multiplicacao(num1, num2, mult)

    if op == 4:
        calcular_divisao(num1, num2, div)

    if op == 5:
        calcular_potencia(num1, num2, poten)

    info = int(input('Deseja fazer outra operação ?\nDigite o número 1 para fazer outra operação ou qualquer outro número para encerrar.\n'))
print('\nCalculadora Encerrada!!!!')
