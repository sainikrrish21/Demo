#WAP to print series of numbers from 3 to 39.

for i in range(3, 40):
    print(i) 
 
#WAP to print series of numbers from 15 to 5.

i=15
while i>=5:
    print(i)
    i-=1
    
#WAP to print numbers divisible by 7 in range 1 to 21

for i in range(1, 22):
    if i%7==0:
        print(i)
        
#WAP to print the numbers which are divisible by both 3 and 5 from 5 to 25

for i in range(5, 26):
    if i%3==0 and i%5==0:
        print(i)
        
#WAP to print divisor of 24 from 3 to 12.

for i in range(3, 13):
    if 24%i==0:
        print(i)
        
#WAP to count total no .of divisor of the given number.

num= int(input("Enter a number:"))
count=0
for i in range(1, num+1):
    if num%i==0:
        count+=1
print("Total number of divisors:", count)

#WAP to check that count of the divisor of a given number is equal to 2 . If it is equal print prime number else print not a prime number.

num= int(input("Enter a number:"))
count=0
for i in range(1, num+1):
    if num%i==0:
        count+=1
if count==2:
    print("Prime number")
else:
    print("Not a prime number")
    
#WAP to print sum of the numbers present from 3 to 9.

total=0
for i in range(3, 10):
    total+=i
print("Sum of numbers from 3 to 9:", total)

#WAP to print sum of the digits present in a number

num= int(input("Enter a number:"))
total=0
while num>0:
    digit=num%10
    total+=digit
    num//=10
print("Sum of digits:", total)

#WAP to print sum of the odd digit present in a number

num= int(input("Enter a number:"))
total=0
while num>0:
    digit=num%10
    if digit%2!=0:
        total+=digit
    num//=10
print("Sum of odd digits:", total)
