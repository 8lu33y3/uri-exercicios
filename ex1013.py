def main():

    valores = str( input() )
    n1,n2,n3 = valores.split()
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)

    if ( (n1 > n2) and (n1 > n3) ):
        maior = n1
    elif ( (n2 > n1) and (n2 > n3) ):
        maior = n2
    elif ( (n3 >n1) and (n3 >n2) ):
        maior = n3
    print(maior,'eh o maior')

main()
