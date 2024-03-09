class Calculate:
    def __init__(self, firstNum = 0, secondNum = 0, operator = None):
        self.firstNum = firstNum
        self.secondNum = secondNum
        self.operator = operator
    
    def calculate(self,):
        if self.operator == "+":
            return self.firstNum + self.secondNum
        elif self.operator == "-":
            return self.firstNum - self.secondNum
        elif self.operator == "*":
            return self.firstNum * self.secondNum
        elif self.operator == "/":
            canDivide = self.checkdivide()
            if canDivide:
                return self.firstNum / self.secondNum
            else:
                return "Cannot divide by zero"
        else:
            return "Invalid operator"

    def checkdivide(self):
        if self.secondNum == 0:
            return False
        else:
            return True
        
    def playAgain(self):
        playAgain = input("Play again? (y/n): ")
        if playAgain == "y":
            return True
        else:
            return False