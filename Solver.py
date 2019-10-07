from __future__ import division

class Solver:
    def __init__(self, degres0 = 0, degres1 = 0, degres2 = 0):
        self.degres0 = degres0
        self.degres1 = degres1
        self.degres2 = degres2
        self.equaDegres = 0
        self.soluce = []
        self.delta = 0
    def getDegres0(self):
        return  self.degres0

    def getDegres1(self):
        return  self.degres1

    def getDegres2(self):
        return  self.degres2

    def getEquaDegre(self):
        return  self.equaDegres

    def setEquaDegre(self, nb):
        return  self.equaDegres
        
    def getSolution(self):
        return self.soluce

    def findEquaDegres(self):
        if((self.degres2 != 0) and (self.equaDegres == 0)):
            self.equaDegres = 2
        elif((self.degres1 != 0) and (self.equaDegres == 0)):
            self.equaDegres = 1
        elif((self.degres0 != 0) and (self.equaDegres == 0)):
            self.equaDegres = 0
        else:
            self.equaDegres = -1

    def calculEqua(self):
        if(self.equaDegres == 2):
            self.solveSecondDegreEqua()
        if(self.equaDegres == 1):
            self.solveFirstDegreEqua()
        if(self.equaDegres == 0):
            self.soluce = []
        if(self.equaDegres == -1):
            self.soluce = [0]

    def solveFirstDegreEqua(self):
        self.soluce.append((self.degres0 * (-1)) / self.degres1)
    
    def solveSecondDegreEqua(self):
        carre = self.degres1**2
        ac = 4 * self.degres0 * self.degres2
        self.delta = carre - ac
        if ( self.delta < 0):
            self.soluce = []
        elif( self.delta == 0):
            b = ( -1 * self.degres1)
            a2= (2 * self.degres2)
            self.soluce.append(float( b / a2))
        else:
            racineDelta = self.delta**(0.5)
            x1 = (((self.degres1 * -1) - racineDelta) /( 2 * self.degres2))
            x2 = (((self.degres1 * -1) + racineDelta) /( 2 * self.degres2))
            self.soluce.append(x1)
            self.soluce.append(x2)

    def conditionalDisplay(self, valueToDisplay, testedValue):
        return valueToDisplay if testedValue != 0 else ''

    def display(self):
        finalEqua= ''
        if(self.degres0 != 0 or self.degres1 != 0 or self.degres2 != 0):
            if(self.degres0 != 0 ):
                finalEqua = finalEqua + str(self.degres0) + self.conditionalDisplay(" + ", self.degres1)
            if(self.degres1 != 0):
                finalEqua = finalEqua +  str(self.degres1) + 'X' +  self.conditionalDisplay(" + ", self.degres2)
            if (self.degres2 != 0): 
                finalEqua = finalEqua + str(self.degres2) + 'X^2'
            finalEqua = finalEqua +  ' = 0 \n '
            finalEqua = finalEqua + 'Polynomial degree: '
            finalEqua = finalEqua + str(self.equaDegres) + '\n '
            finalEqua = finalEqua +  "<| = b^2 - 4ac = " +  str(self.delta) + '\n '
            if(len(self.soluce )== 2):
                finalEqua = finalEqua + 'Discriminant is strictly positive, the two solutions are:\n' 
                finalEqua = finalEqua + str(self.soluce[0])+ '\n' +str(self.soluce[1]) + '\n'
            elif(len(self.soluce) == 1):
                finalEqua = finalEqua +'The solution is:\n' 
                finalEqua = finalEqua + str(self.soluce[0])
            else:
                finalEqua = finalEqua + "The polynomial degree is stricly greater than 2, I can't solve.\n"
        else:
            finalEqua = 'Reduced form: 0 = 0 \nPolynomial degree: 0\n<| = b^2 - 4ac = 0 \nThe solution is: \n0'
        return finalEqua