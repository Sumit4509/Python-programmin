# two types of loops for and while 
# Indentation is important no need of curly brackets 

'''
# Write a program that prompts the user to input an integer and then outputs the number with the digits reversed. For example, if the input is 12345, the output should be 54321.

num = int(input("Enter an integer: "))
reversed_num = 0
while num > 0:
    remainder = num % 10
    reversed_num = reversed_num * 10 + remainder
    num = num // 10
print("Reversed number:", reversed_num)
'''

'''
# Write a program that prompts the user to input a positive integer. It should then output a message indicating whether the number is a prime number.
num= int(input("enter the num"))
a=0
for i in range(2:n//2:1):
    if(num%i==0):
        a=1
        break
if a==0:
    print("num is prime no")
else:
    print("num is not a prime no")
'''

'''
# Write a program to enter the numbers till the user wants and at the end it should display the count of positive, negative and zeros entered.
num= int (input("enter the number of integer you want to given "))
positive =0
negative =0
zero_entered=0

while(num>0):
    n=float (input("enter the number value "))
    if n==0:
        zero_entered+=1
    elif n>0:
        positive+=1
    else:
        negative+=1

    num-=1
print("positve values {0}".format(positive))
print("negetive values {0}".format(negative))
print("zero_entered values {0}".format(zero_entered))

'''

'''
# Write a program to print out all Armstrong numbers between 1 and 500. If sum of cubes of each digit of the number is equal to the number itself, then the number is called an Armstrong number.
# For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 )

def is_armstrong(number):
    # Convert number to string to iterate through digits
    str_num = str(number)
    num_digits = len(str_num)
    # Calculate sum of cubes of each digit
    armstrong_sum = sum(int(digit) ** num_digits for digit in str_num)
    # Check if the sum equals the number itself
    return armstrong_sum == number

def print_armstrong_numbers():
    print("Armstrong numbers between 1 and 500:")
    for num in range(1, 501):
        if is_armstrong(num):
            print(num)

print_armstrong_numbers()
'''
'''
# . Write a program to print Fibonacci series of n terms where n is input by user :
# 0 1 1 2 3 5 8 13 24 .....

n = int (input("enter n"))
a=[]
start =0
end = 1
a.append(start)
a.append(end)

for i in range(2,n,1):
    next = start+end 
    start =end
    end =next 
    a.append(next)
print(a)

'''

'''
# Write a program to enter the numbers till the user wants and at the end the program should display the largest and smallest numbers entered.
num = int(input("Enter the number of integers you want to input: "))

if num == 0:
    print("No values entered.")
else:
    smallest = float('inf')  # Initialize smallest to positive infinity
    largest = float('-inf')  # Initialize largest to negative infinity
    
    for i in range(num):
        value = float(input("Enter value {}: ".format(i + 1)))
        smallest = min(smallest, value)
        largest = max(largest, value)

    print("Smallest:", smallest)
    print("Largest:", largest)

'''

'''
# Write a program to convert a binary number into a decimal number without using array, function and while loop

binary = input("Enter a binary number: ")

decimal = 0
power = len(binary) - 1  # Initialize the power of 2

for digit in binary:
    if digit == '1':
        decimal += 2 ** power  # Add 2 raised to the power of its position
    power -= 1  # Decrement the power for the next digit

print("Decimal equivalent:", decimal)

'''

'''
# print the pattern
# **********
# **********
# **********
# **********
n=4
m=10 
for i in range(1,n+1):
    for j in range(1,m+1):
        print("*",end="")
    print()
'''

'''
# *
# **
# ***
# ****
# *****
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()

'''
'''
    *
   ***
  *****
 *******
*********
# n=5
# for i in range(1, n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print("*",end="")
        
#     print()
'''

     