# تمرین پیاده سازی

import math;
y = math.exp(2)+1
print(y)

#  8.38905609893065 جواب 


# تمرین ماشین حساب

def Calculator():
    number1 = float(input('Please Enter Number 1: '))
    number2 = float(input('Please Enter Number 2: '))
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    result = input("Please Enter an Operation (1/2/3/4): ")

    if result == '1': 
        print("Result:", number1 + number2)
    
    elif result == '2':
        print("Result:", number1 - number2)
    
    elif result == '3':
        print("Result:", number1 * number2)
    
    elif result == '4':
        if number2 != 0:
            print("Result:", number1 / number2)
        else:
            print("Error: Division by zero")
    else: 
        print("Sorry, invalid operation.")

Calculator()


# تمرین مقایسه

"x" < "a"   # False

"a" >= "b"  # False

"a" < "b"  # True


# تمرین کسر 

from fractions import Fraction


a = float(input("Please Enter Number 1 : "))
b = float(input("Please Enter Number 2 : "))


fraction_a = Fraction(a)
fraction_b = Fraction(b)


result = (fraction_a + fraction_b) / 2


print("Result :", result)
