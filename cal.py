#Module Starts

print("\n What is Your Name?")

name = str(input())

print("\n Welcome To Oxy Py Calculator, " + name)

#code

print("\n Select operation.")

print("\n1.Add")

print("2.Subtract")

print("3.Multiply")

print("4.Divide")

#Add

def add(x, y):

  return x + y

def subtract(x, y): 

  return x - y

#Multiply *

def multiply(x, y):

  return x * y

#Divide

def divide(x, y):

  return x / y

#UserInput

while True:

  print("\n Choose => ")

  choose = input()

  n1 = float(input("Enter First Number: "))

  n2 = float(input("Enter Second Number: "))

  if choose in ('1','2','3','4'):

    

    

    if choose == '1':

      print(n1, "+" , n2, "=", add(n1, n2))

      

    elif choose == '2':

      print(n1, "-", n2, "=", subtract(n1, n2))

    elif choose == '3':

      print(n1, "*", n2, "=", multiply(n1,n2))

      

    elif choose == '4':

      print(n1, "÷", n2, "=", divide(n1, n2))

    else:

      print("Invalid")

      break

   

