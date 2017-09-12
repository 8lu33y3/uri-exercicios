

def mult(n1,n2):
    mult = n1*n2
    return mult

def entrada(linha):
    a  = input()
    
    return a

def main():
    
    valores = entrada(input())

    cod, qtd, valor = entrada.split()

    valores2 = entrada1(input())

    cod1,qtd1,valor1 = entrada1.split()

    cod1 = int(cod1)
    qtd1 = int(qtd1)
    valor1 = float(valor1)

    cod = int(cod)
    qtd = int(qtd)
    valor = float(valor)

    pagar = mult(qtd,valor) + mult(qtd1,valor1)
    
    print("VALOR A PAGAR: R$ %0.2f" %pagar)

main()
