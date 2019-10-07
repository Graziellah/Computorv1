import re
from string import *
import Solver
from locale import atof

class Equation:
    def __init__(self, equation = 0):
        self.equation = equation
        self.rightPart = ''
        self.leftPart = ''
        self.degres0= 0
        self.degres1= 0
        self.degres2= 0
        self.solver = None

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

    def getRightPart(self):
        return self.rightPart

    def getLeftPart(self):
        return self.leftPart

    def sortAllValue(self,equa, coeff):
        for equa in equa:
            if(self.thereIsXPower(equa)):
                self.degres0 += self.getDegresValue(equa, 'X^0', coeff)
                self.degres1 += self.getDegresValue(equa, 'X^1', coeff)
                self.degres2 += self.getDegresValue(equa, 'X^2', coeff)
            elif(self.thereIsX(equa)):
                self.degres1 += self.getDegresValue(equa, 'X', coeff)
            else:
                self.degres0 += atof(equa)

    def calculateDegreValue(self):
        self.sortAllValue(self.leftPart, 1)
        self.sortAllValue(self.rightPart, -1)
        self.instanciateSolver()

    def instanciateSolver(self):
        self.solver = Solver.Solver(self.degres0, self.degres1, self.degres2)

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

    def displaySoluce(self):
        return self.solver.display()

    def getDegres0(self):
        return  self.degres0

    def getDegres1(self):
        return  self.degres1

    def getDegres2(self):
        return  self.degres2

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
    
    
    
