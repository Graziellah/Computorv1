import Solver

def test_instantiation():
    test = Solver.Solver()
    assert test.getDegres0() == 0
    assert test.getDegres1() == 0
    assert test.getDegres2() == 0
    assert test.getEquaDegre() == 0
    assert test.getSolution() == []

def  test_findEquaDegres():
    test = Solver.Solver(2, 3, 9)
    test.findEquaDegres()
    assert test.getEquaDegre() == 2

def  test_findEquaDegres():
    test = Solver.Solver(3, 9, 0)
    test.findEquaDegres()
    assert test.getEquaDegre() == 1

def  test_findEquaDegres():
    test = Solver.Solver(0, 0, 9)
    test.findEquaDegres()
    assert test.getEquaDegre() == 0

def  test_findEquaDegres():
    test = Solver.Solver(0, 0, 0)
    test.findEquaDegres()
    assert test.getEquaDegre() == -1

def test_calculEqua_degres2_deltaPos():
    test = Solver.Solver(-6, -1, 2)
    test.findEquaDegres()
    test.calculEqua()
    assert test.getSolution() == [ -1.5, 2]

def test_calculEqua_degres2_delta0():
    test = Solver.Solver(1.125, -3, 2)
    test.findEquaDegres()
    test.calculEqua()
    assert test.getSolution() == [0.75]

def test_calculEqua_degres1():
    test = Solver.Solver(-15, 3, 0)
    test.findEquaDegres()
    test.calculEqua()
    value = test.getSolution() 
    assert value == [5]

# def test_calculEqua_degres0():
#     test = Solver.Solver(0, 0, 9)
#     test.findEquaDegres()
#     test.calculEqua()
#     assert test.getSolution() == 0

# def test_calculEqua_noSoluce():
#     test = Solver.Solver(0, 0, 0)
#     test.findEquaDegres()
#     test.calculEqua()
#     assert test.getSolution() == 0