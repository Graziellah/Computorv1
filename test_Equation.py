import Equation
from StringIO import StringIO

def test_initEquation():
    equa = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
    test = Equation.Equation(equa)
    assert test.getEquation() == equa
def test_setLeft():
    equa = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
    test = Equation.Equation(equa)
    test.split()
    left = test.getLeftPart()
    assert left == ['5*X^0', '+4*X^1','-9.3*X^2']
def test_setRight():
    equa = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
    test = Equation.Equation(equa)
    test.split()
    left = test.getRightPart()
    assert left == ['1*X^0']
def test_thereIsX_True():
    test = Equation.Equation()
    returnValue = test.thereIsX('1*X^0')
    assert returnValue == True
def test_thereIsX_False():
    test = Equation.Equation()
    returnValue = test.thereIsX('1')
    assert returnValue == False
def test_getDegresValue_0():
    test = Equation.Equation()
    returnValue = test.thereIsX('1')
    assert returnValue == False
def test_getDegresValue_coeff_minus1():
    test = Equation.Equation()
    returnValue = test.getDegresValue('-9.3*X^2', 'X^2', -1)
    assert returnValue == 9.3
def test_getDegresValue_coeff_1():
    test = Equation.Equation()
    returnValue = test.getDegresValue('-9.3*X^2', 'X^2', 1)
    assert returnValue == -9.3
def test_getDegresValue_coeff_1():
    test = Equation.Equation()
    returnValue = test.getDegresValue('-9.3', 'X^2', 1)
    assert returnValue == 0
def test_getDegresValue_0():
    test = Equation.Equation()
    returnValue = test.getDegresValue('-9.3', 'X^2', 1)
    assert returnValue == 0
def test_sortAllValue_withX():
    test = Equation.Equation()
    test.sortAllValue(['5*X^0', '+4*X^1','-9.3*X^2'],1)
    assert  test.getDegres0() == 5
    assert  test.getDegres1() == 4
    assert  test.getDegres2() == -9.3
def test_sortAllValue_withoutX():
    test = Equation.Equation()
    test.sortAllValue(['5', '+4*X^1','-9.3*X^2'],1)
    assert  test.getDegres0() == 5
    assert  test.getDegres1() == 4
    assert  test.getDegres2() == -9.3
def test_calculateDegreValue():
    equa = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
    test = Equation.Equation(equa)
    test.split()
    test.calculateDegreValue()
    assert  test.getDegres0() == 4
    assert  test.getDegres1() == 4
    assert  test.getDegres2() == -9.3
def test_displaySoluce():
    equa = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
    test.split()
    test.calculateDegreValue()
    test.displaySoluce()
    out = StringIO()
    output = out.getvalue().strip()
    
# def test_solveEquation():
#     equa = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
#     test = Equation.Equation(equa)
#     test.split()
#     test.calculateDegreValue()
#     degres0 = test.getDegres0()
#     degres1 = test.getDegres1()
#     degres2 = test.getDegres1()
#     test.solve()

  




      