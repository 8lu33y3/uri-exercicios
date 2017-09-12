# -*- coding: utf-8 -*-

#UFMT - CIENCIA DA COMPUTACAO
#PROGRAMACAO I - CARLOS D. O. SILVA
#CONVERSAO DE TEMPO EM DIAS PARA (ANO,MES,DIA)

def main():
    idade = int(input())
    
    ano = int(idade / 365)
    
    meses = int(idade %365)
    mes = int(meses / 30 )
    dia = int(idade % 365)
    dia = int(dia % 30)

          
    print(str(ano) + " ano(s)")
    print(str(mes) + " mes(es)")
    print(str(dia) + " dia(s)")
   

main()
