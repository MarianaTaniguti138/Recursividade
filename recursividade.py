def menu():
    while True:
        opcao = input("\n1) Soma 0 a N | 2) Menor vetor | 3) X^Y | 4) MDC | Binário | 0) Sair\nOpção: ")
        if opcao == '0': break
        funcs = [soma, menor, potencia, mdc, binario]
        args = [int(input("N: ")), list(map(int, input("Vetor: ").split())),
                (int(input("Base: ")), int(input("Expoente: "))),
                (int(input("A: ")), int(input("B: "))), int(input("Decimal: "))]
        print( funcs[int(opcao) -1](*args[int(opcao) -1]))

def soma(n): return 0 if n == 0 else n + soma(n - 1)
def menor(v): return v[0] if len(v) == 1 else min(v[0], menor(v[1:]))
def potencia(x, y): return 1 if y == 0 else x * potencia(x, y - 1)
def mdc(a, b): return a if b == 0 else mdc(b, a % b)
def binario(n): return "0" if n == 0 else binario(n // 2) + str(n % 2)

menu()