# -*- coding: utf-8 -*-
#UFMT - CIENCIA DA COMPUTACAO
#PROGRAMACAO 1 - CARLOS D.O. SILVA
#area

def main():
	
        import math
        n = str(input())
        a,b,c = n.split()
        
        a = float(a)
        b = float(b)
        c = float(c)
        
        
        aT = (a*c)/2
        
        aC = 3.14159 * (c**2)
        aQ = b**2
        aQQ = ( (a + b)*c) / 2
        aR = a*b
	
        print("TRIANGULO: %0.3f" %aT) 
        print("CIRCULO: %0.3f" %aC)
        print("TRAPEZIO: %0.3f" %aQQ) 
        print("QUADRADO: %0.3f" %aQ) 
        print("RETANGULO: %0.3f" %aR)
	
main()

