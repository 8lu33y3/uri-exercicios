# -*- coding: utf-8 -*-
#UFMT - CIENCIA DA COMPUTACAO
#PROGRAMACAO I - CARLOS D. O. SILVA
#MEDIA COMBUSTIVEL GASTO

def main():
    valor = int(input())
    print(valor)
    aux = int(valor / 100)   
    print("%s nota(s) de R$ 100,00" %aux)
    valor %= 100
    aux = int(valor / 50)
    print("%s nota(s) de R$ 50,00" %aux)
    valor %= 50
    aux = int(valor / 20)
    print("%s nota(s) de R$ 20,00" %aux)
    valor %= 20
    aux = int(valor / 10)
    print("%s nota(s) de R$ 10,00" %aux)
    valor %= 10
    aux = int(valor / 5)
    print("%s nota(s) de R$ 5,00" %aux)
    valor %= 5
    aux = int(valor / 2)
    print("%s nota(s) de R$ 2,00" %aux)
    valor %= 2
    print("%s nota(s) de R$ 1,00" %valor)
     
main()
