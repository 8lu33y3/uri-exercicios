def main():

    valores = str(input())
    a,b,c = valores.split()
    a = float(a)
    b = float(b)
    c = float(c)
    if ( (a < b+c) and (a > abs(b-c) ) ) :  # abs() eh o comando usado para retorno de valor absoluto
        if ( (b < a+c) and (b > abs(a-c) ) ) :
            if ( (c < b+a) and (c > abs(b-a)) ):
                 perimetro = a + b + c
                 print('Perimetro = %0.1f' %perimetro)
            else:
                 area = ( (a+b) * c) / 2
        else:
                 area = ( (a+b) * c) / 2
    else:
                 area = ( (a+b) * c) / 2
                 print('Area = %0.1f' %area)
        
             
main()
