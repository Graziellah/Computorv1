from __future__ import division

class Solver:
    def __init__(self, equa):
        self.equa = equa
        self.equaDegres = 0
        self.soluce = []
        self.delta = 0
        self.AllNumbersAreSolution = False
    def setEquaDegre(self, nb):
        return  self.equaDegres
        
    def getSolution(self):
        return self.soluce

    def findEquaDegres(self):
        nb = 0
        for key in self.equa.keys():
            if nb < key:
                nb = key
        self.equaDegres = nb

    def calculEqua(self):
        if(self.equaDegres == 0):
            self.soluce = []
        elif(self.equaDegres == 1):
            self.solveFirstDegreEqua()
        elif(self.equaDegres == 2):
            self.solveSecondDegreEqua()
        elif(self.equaDegres == -1):
            self.soluce = []

    def solveFirstDegreEqua(self):
        self.soluce.append((self.equa[0] * (-1)) / self.equa[1])
    
    def solveSecondDegreEqua(self):
        carre = self.equa[1]**2
        ac = 4 * self.equa[0] * self.equa[2]
        self.delta = carre - ac
        if self.delta < 0:
            self.soluce = []
        elif self.delta == 0:
            b = ( -1 * self.equa[1])
            a2= (2 * self.equa[2])
            self.soluce.append(float( b / a2))
        else:
            racineDelta = self.delta**(0.5)
            x1 = (((self.equa[1] * -1) - racineDelta) /( 2 * self.equa[2]))
            x2 = (((self.equa[1] * -1) + racineDelta) /( 2 * self.equa[2]))
            self.soluce.append(x1)
            self.soluce.append(x2)

    def conditionalDisplay(self, valueToDisplay, testedValue):
        newStr = str(testedValue)
        split = newStr.split('.')
        nbToDisplay = 0
        if split[1] == "0":
            nbToDisplay =  int(testedValue)
        else:
            nbToDisplay = float(testedValue)
        if testedValue < 0:
            return " - " + str(nbToDisplay * -1)
        return valueToDisplay + str(nbToDisplay)

    def power(self,nb, powerval):
        if powerval < 0:
            return 0
        if powerval == 0:
            return 1
        return nb * (self.power(nb, powerval - 1))

    def pgcd(self, nb1, nb2):
        if nb2 == 0:
            return nb1
        return self.pgcd(nb2, nb1 % nb2)

    def fraction(self, nb):
        newStr = str(nb)
        split = newStr.split('.')
        if split[1] == "0":
            return int(nb)
        b = len(split[1])
        denominator = int(self.power(10, b))
        numerator = int( nb * denominator)
        gcd = self.pgcd(numerator, denominator)
        fraction = str(int(numerator/ gcd)) +  "/" + str(int(denominator/gcd))
        return fraction

    def displayPower(self, key):
        if key == 0:
            return ""
        elif key == 1:
            return "X"
        else:
            return "X^"+ str(key)

    def displayReducedForm(self):
        reducedForm = 'Reduced form: '
        startLen = len(reducedForm)
        sign = ""
        for key in self.equa.keys():
            if self.equa[key] != 0:
                reducedForm = reducedForm + self.conditionalDisplay(sign , self.equa[key]) + self.displayPower(key) 
                sign = " + "
        if startLen == len(reducedForm):
            self.AllNumbersAreSolution = True
            reducedForm = reducedForm + "0"
        return reducedForm + " = 0\n"

    def displayPolynomialDegres(self):
        return "Polynomial degree: " + str(self.equaDegres) + "\n"

    def displayDiscriminant(self):
        if self.equaDegres < 3 and not self.AllNumbersAreSolution :
            return "<| = b^2 - 4ac = " +  str(round(self.delta, 6)) + "\n"
        return ""
    def displaySolution(self, seeFraction):
        solutions = ""
        for soluce in self.soluce:
            solutions = solutions + "\n"
            if seeFraction :
                solutions = solution +  str(self.fraction(round(self.soluce, 5)))  
            else:
                solutions = solutions + str(round(soluce, 6))
        return solutions

    def displaySolutionIntro(self):
        if self.equaDegres > 2:
            return "The polynomial degree is stricly greater than 2, I can't solve."
        if len(self.soluce ) == 2:
            return'Discriminant is strictly positive, the two solutions are:'
        elif len(self.soluce) == 1:
            return'The solution is:'
        elif self.delta < 0 :
            return "The polynomial equation has no solution in R"
        else:
            return "All numbers in R are solutions"
    
    def display(self, seeFraction):
        finalDisplay = ""
        finalDisplay = finalDisplay + self.displayReducedForm()
        finalDisplay = finalDisplay + self.displayPolynomialDegres()
        finalDisplay = finalDisplay + self.displayDiscriminant()
        finalDisplay = finalDisplay + self.displaySolutionIntro()
        finalDisplay = finalDisplay + self.displaySolution(seeFraction)
        return finalDisplay
