#function to sum() the value from user input

def sum (num1,num2):
  return num1+num2

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c= sum (a,b)
print("Sum of a", a, "and b", b, "is", c)