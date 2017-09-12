# -*- coding: utf-8 -*-
#UFMT - CIENCIA DA COMPUTACAO
#PROGRAMACAO I - CARLOS D. O. SILVA
#CONVERSAO DE TEMPO - SEGUNDOS/HORA

def main():
    tempo = int(input())
    minutos = int(tempo / 60) 
    minuto = int(minutos % 60)
    segundos = (tempo % 60)
    hora = int(minutos / 60)
          
    print("%s:%s:%s" %(hora,minuto,segundos))
    
main()
