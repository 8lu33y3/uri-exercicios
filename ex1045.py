def main():

    valores = str(input())
    a,b,c= valores.split()
    
    a = float(a)
    b = float(b)
    c = float(c)

    if (a >= (b+c)):
        print('NAO FORMA TRIANGULO')

    else:
        aux = b**2 + c**2
        
        if ( (a**2) == aux ):
            print('TRIANGULO RETANGULO')

        if ( (a**2) > aux ):
            print('TRIANGULO OBTUSANGULO')

        if ( (a**2) < aux ):
            print('TRIANGULO ACUTANGULO')

        if ( ((a == b) and (a== c) and (b == c)) ) :
            print('TRIANGULO EQUILATERO')

        if (a == b) != c :
            if(b==c) != a:
                if (a == c) != b:
                    print('TRIANGULO ISOSCELES')
    

    
main()
