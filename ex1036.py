def main():
        import math
        coef = str(input())
        a,b,c = coef.split()
        a = float(a)
        b = float(b)
        c = float(c)
        try: 
            delta = (b**2) - 4 * (a*c)
            d = math.sqrt(delta)
        
            if  ( (a <= 0) or (d < 0) ):
                print('Impossivel calcular')
            else:
                
                r1 = (-b + d ) / (2*a)
                r2 = (-b - d ) / (2*a)
                
                print('R1 = %0.5f' %r1)
                print('R2 = %0.5f' %r2)
        except ValueError:
            print('Impossivel calcular')
                      
main()
