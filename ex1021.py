def main():
    import math
    
    valor = float(input())
    aux = valor
    print('NOTAS:')
    notas = int(valor / 100)
    print('%s nota(s) de R$ 100.00' %notas)
    valor = valor % 100
    notas = int(valor / 50)
    print('%s nota(s) de R$ 50.00' %notas)
    valor = valor%50
    notas = int(valor/20)
    print('%s nota(s) de R$ 20.00' %notas)
    valor = valor%20
    notas = int(valor/10)
    print('%s nota(s) de R$ 10.00' %notas)
    valor = valor%10
    notas = int(valor/5)
    print('%s nota(s) de R$ 5.00' %notas)
    valor = valor%5
    notas = int(valor/2)
    print('%s nota(s) de R$ 2.00' %notas)
    valor = valor%2
    notas = int(valor)
    print('MOEDAS:')
    
    print('%s moeda(s) de R$ 1.00' %notas)
    valor = valor*100
    moeda = int(valor%100/50)

    print('%s moeda(s) de R$ 0.50' %moeda)
    moeda = int(valor%100%50/25)
                
    print('%s moeda(s) de R$ 0.25' %moeda)
    moeda = int(valor%100%50%25/10)

    print('%s moeda(s) de R$ 0.10' %moeda)
    moeda = int(valor%100%50%25%10/5)

    print('%s moeda(s) de R$ 0.05' %moeda)
    
    moeda = int(valor%100%50%25%10%5)

    print('%s moeda(s) de R$ 0.01' %moeda)

main()
