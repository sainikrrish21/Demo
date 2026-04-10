#Check if a number is Even or Odd.

num= int(input("Enter a number:"))
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")
    
#Check if a number is Positive or Negative or Equal to Zero

num= int(input("Enter a number:"))
if num>0:    
    print("The number is positive")
elif num<0:
    print("The number is negative")
else:
    print("The number is zero")
    
#Check if a person is Minor or Adult (age 18)

age= int(input("Enter your age:"))
if age>=18:
    print("You are an adult")
else:
    print("You are not an adult")
    
#Find the greater of two numbers

num1= int(input("Enter first number:"))
num2= int(input("Enter second number:"))
if num1>num2:
    print("The greater number is:", num1)
elif num2>num1:
    print("The greater number is:", num2)

#Check if a number is divisible by 10 or not

num= int(input("Enter a number:"))
if num%10==0:
    print("The number is divisible by 10")
else:
    print("The number is not divisible by 10")
    
