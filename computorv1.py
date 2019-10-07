import sys
import Equation

if(len(sys.argv) == 1):
    print('il manque un argument')
elif(len(sys.argv) != 2):
    print('usage: computorv1 [equation]')
else:
    equa = sys.argv[1]
    result = Equation.Equation(equa)
    try:
        result.split()
    except:
        print('syntax error')
        sys.exit(1)
    try:
        result.calculateDegreValue()
    except:
        print("The polynomial degree is stricly greater than 2, I can't solve")
        sys.exit(1)
    result.solve()
    print (result.displaySoluce())

