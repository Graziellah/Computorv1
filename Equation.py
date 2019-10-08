import re
from string import *
import Solver
from locale import atof

class Equation:
    def __init__(self, equation = 0):
        self.equation = equation
        self.rightPart = ''
        self.leftPart = ''
        self.solver = None
        self.equaDetail = {}
    
    def getEquation(self):
        return self.equation
 
    def checkValidityFormat(self):
        p = re.search('[^0-9X=\^\+\-\s*.]', self.equation)
        if( p != None):
            raise  SyntaxError( 'Syntax Error ' + self.equation)       

    def split(self):
        try:
            self.checkValidityFormat()
        except SyntaxError as err :
            raise err
        splittedEqu = self.equation.split('=')
        self.leftPart = self.lexerParseur(splittedEqu[0])
        self.rightPart = self.lexerParseur(splittedEqu[1])

    def sortAllValue(self,equa, coeff):
        for equa in equa:
            powerValue = int(self.getPowerValue(equa))
            oldValue = self.equaDetail[powerValue] if powerValue in self.equaDetail.keys() else 0
            self.equaDetail[powerValue] = self.getValue(equa, coeff) + oldValue
    
    def getValue(self, equa, coeff):
        nb = 0
        if(equa.find("*") > -1):
            nb = equa.split('*')
        else:
            nb = equa
        if(len(nb) == 1):
            if(nb[0][0] == "-"):
                return -1 * coeff
            else:
                return coeff
        else:
            return atof(nb[0]) * coeff

    def getPowerValue(self, equa):
        if(self.thereIsXPower(equa)):
            value = equa.index("X^")
            if(equa[value + 2]):
                return equa[value + 2]
        elif(self.thereIsX(equa)):
            return 1
        else:
            return 0

    def calculateDegreValue(self):
        self.sortAllValue(self.leftPart, 1)
        self.sortAllValue(self.rightPart, -1)
        self.instanciateSolver()

    def instanciateSolver(self):
        self.solver = Solver.Solver(self.equaDetail)

    def solve(self):
        self.solver.findEquaDegres()
        self.solver.calculEqua()

    def getDegresValue(self,equa, pattern, coeff):
        if(equa.find(pattern) > -1 ):
            nb = equa.split('*')
            if(len(nb) == 1):
                if(nb[0][0] == "-"):
                    return -1 * coeff
                else:
                    return coeff
            else:
                return atof(nb[0]) * coeff
        else:
            return 0

    def thereIsXPower(self,equa):
        a = equa.find('X^') 
        if( a != -1):
                return True
        return False

    def thereIsX(self,equa):
        a = equa.find('X') 
        if( a != -1):
                return True
        return False

    def displaySoluce(self, seeFraction = False):
        return self.solver.display(seeFraction)

    def lexerParseur(self, equa):
        result = []
        lexeme = ''
        plus = '+'
        moins = '-'
        for i,char in enumerate(equa):
            if char != plus or char != moins:
                lexeme += char 
            if (i+1 < len(equa)): 
                if equa[i+1] == plus or equa[i+1] == moins: 
                    if lexeme != '' or lexeme != ' ':
                        result.append(lexeme.replace(" ", ""))
                    lexeme = '' 
        result.append(lexeme.replace(" ", ""))
        return result
