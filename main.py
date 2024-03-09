import calculator
def floatInput(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter an integer")
            continue
            
def main():
    while True:
        firstNum = floatInput("Enter first number: ")
        secondNum = floatInput("Enter second number: ")
        operator = input("Enter operator: ")
        calculate = calculator.Calculate(firstNum=firstNum, secondNum=secondNum, operator=operator)
        print(calculate.calculate())

        if calculate.playAgain():
            continue
        else: 
            print("Thank you For Playing! ")
            break


if __name__ == "__main__":
    main()
