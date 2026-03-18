#Control Flow (if, if-else, loops)







#Find the factorial of a number using a loop.

#Count how many even numbers are between 1 and 50.
'''6
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")'''
#2.Find the largest of three numbers.
'''a, b, c = 10, 25, 15
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print(f"The largest number is {largest}")'''
#3.Print the multiplication table of a given number.
'''n = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")'''
'''year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")'''

#4.Check if a year is a leap year.
'''
marks = float(input("Enter marks: "))
if marks > 40:
    print("Passed")
else:
    print("Failed")'''

#5.Write a program to check if a student has passed (marks ≥ 40).

'''correct_password = "Ram"
while True:
    guess = input("Enter password: ")
    if guess == correct_password:
        print("Access Granted")
        break
    else:
        print("Incorrect, try again.")'''
#6.Keep asking the user for a password until they enter the correct one.
'''a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b'''
    
#7.Print the first 10 Fibonacci numbers.

'''for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i, end=" ")'''


#8.Print numbers from 1 to 20, but skip multiples of 3.
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial is {factorial}")
