def main():

    valores = str(input())
    a,b = valores.split()
    a = int(a)
    b = int(b)

    if ( ((a % b) == 0) or (b%a) == 0 ):
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

main()
