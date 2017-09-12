
#UFMT - CIENCIA DA COMPUTACAO
#PROGRAMACAO I - CARLOS D. O. SILVA
#SALARIO COM BONUS

def main():
     nome = input() 
     salario = float(input())
     qtdvendas = float(input())
     
     bonus = float(qtdvendas * (15/100))
     
     total =  salario + bonus
     
     print("TOTAL = R$ %0.2f" %total) 
     
main()
