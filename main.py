#function to add two numbers
def sum (num1,num2):
  return num1+num2

#function to subtract two numbers
def sub(num1, num2):
    totminus = num1 - num2
    return totminus

print("1. Summation of 2 numbers")
print("2. Subtraction of 2 numbers")

while True:
  # input from user 
  choice = input("Please enter your choice:")

#check the users choice
  if choice in ('1', '2'):
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    if choice == '1':
      print("The sum of 2 numbers is: ", sum(num1,num2))
    elif choice == "2":
      print(num1, "-", num2, sub(num1,num2))
    break
  else:
    print("Invalid input")
  
