import sys
import Equation

if(len(sys.argv) == 1):
    print('il manque un argument')
elif(len(sys.argv) > 3):
    print('usage: computorv1 [equation] [-f]')
else:
    seeFraction = False
    if(len(sys.argv) == 3 and sys.argv[2] != "-f"):
        print("computorv1: illegal option " + sys.argv[2])
        print('usage: computorv1 [equation] [-f]')
        print('-f : see solution with fractional format')
        sys.exit(1)
    if "-f" in sys.argv:
        seeFraction = True
    equa = sys.argv[1]
    result = Equation.Equation(equa)
    try:
        result.split()
    except SyntaxError as err:
        print( err)
        sys.exit(1)
    result.calculateDegreValue()
    result.solve()
    print (result.displaySoluce(seeFraction))

