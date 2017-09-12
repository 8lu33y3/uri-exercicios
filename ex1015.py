#UFMT - CIENCIA DA COMPUTACAO
#PROGRAMACAO 1 - CARLOS D.O. SILVA

def main():
	
	import math
	
	ab = str(input())
	x1,y1 = ab.split()
	
	ordenada =str(input())
	x2,y2 = ordenada.split()
	
	x1 = float(x1)
	x2 = float(x2)
	y1 = float(y1)
	y2 = float(y2)
	
	x = (x2-x1)**2
	y = (y2-y1)**2
	d = math.sqrt(x+y)
	
	print("%0.4f " %d)
	
main()
