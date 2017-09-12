def main():

        valores = str(input())
        codigo, qtd = valores.split()
        codigo = int(codigo)
        qtd = int(qtd)
        
        if codigo == 1:
            total = qtd * 4.00
        if codigo == 2:
            total = qtd * 4.50
        if codigo == 3:
            total = qtd * 5.00
        if codigo == 4:
            total = qtd * 2.00
        if codigo == 5:
            total = qtd * 1.50
        print('Total: R$ %0.2f' %total)
        
main()
