#function to calculate average between two numbers
def average(num1, num2):
    return float(num1 + num2)/2.0

#get user to input numbers to find average
try:
    x = float(input("Enter x value:"))
    y = float(input("Enter y value: "))
    print(average(x,y))
except ValueError:
    print("please enter only digits!")
    
