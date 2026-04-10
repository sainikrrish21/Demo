#Take 5 subject marks ,calculate average and print: ≥90% → Grade A ≥75% → Grade B ≥50% → Grade C else Fail

marks1= int(input("Enter marks :"))
average= (marks1)
if average>=90:
    print("Grade A")
elif average>=75:
    print("Grade B")
elif average>=50:
    print("Grade C")
else:
    print("Fail")

#Find the largest of three numbers

num1= int(input("Enter first number:"))
num2= int(input("Enter second number:"))
num3= int(input("Enter third number:"))

if num1>=num2 and num1>=num3:
    print("The largest number is:", num1)
elif num2>=num1 and num2>=num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)

#Check if a year is Leap year or not

year= int(input("Enter a year:"))
if year%4==0:
    print("The year is a leap year")
else:
    print("The year is not a leap year")
    
#Create a simple calculator (+, -, *, / based on user input)

num1= float(input("Enter first number:"))
num2= float(input("Enter second number:"))
operator= input("Enter operator (+, -, *, /):")
if operator=="+":
    result= num1+num2
elif operator=="-":
    result= num1-num2
elif operator=="*":
    result= num1*num2
elif operator=="/":
    result= num1/num2
    
print("Result:", result)

# Check if a number is: divisible by 3 → “Fizz” divisible by 5 → “Buzz” both → “FizzBuzz”

num= int(input("Enter a number:"))
if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
    
# Take a number and check: if even → divide by 2 if odd → multiply by 3 and add 1 (Print result)
 
num= int(input("Enter a number:"))
if num%2==0:
    result= num/2
else:
    result= num*3+1
print("Result:", result)

#Electricity bill calculation: First 100 units → ₹5/unit Next 100 → ₹7/unit Above → ₹10/unit

units= int(input("Enter number of units consumed:"))
if units<=100:
    bill= units*5
elif units<=200:
    bill= 100*5 + (units-100)*7
else:
    bill= 100*5 + 100*7 + (units-200)*10
print("Electricity bill:", bill)

