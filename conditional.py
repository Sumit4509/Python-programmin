# conditional statements

# check if person can vote or not -----------------
'''
n= int(input("enter your age"))
if(n<18):
    print("you can't vote")
else :
    print("you can vote")

'''

# Write a program to check if the year is a leap year or not (include the concept of century year also).
'''
n= int(input("enter the year"))
if(n%400==0) and (n%100==0):
    print("{0} is a leap year".format(n))
elif(n%4==0 ) and (n%100!=0):
    print("{0} is a leap year".format(n))
else:
    print("{0} is not a leap year".format(n))

'''

# Write a program to print the triangle as either equilateral or isosceles or scalene, given the sides
'''
s1=int(input("enter side1"))
s2=int(input("enter side2"))
s3=int(input("enter side3"))

if(s1==s2==s3):
    print("The given triangle is an equilateral triangle")
elif(s1==s2)or(s1==s3):
    print("The given triangle is an isosceles triangle")
else:
    print("The given triangle is an scalene triangle")

'''
# Write a program to find largest number from four given numbers
'''
n1=int(input("enter 1st no"))
n2=int(input("enter 2nd no"))
n3=int(input("enter 3rd no"))
n4=int(input("enter 4th no"))

if(n1>n2)and(n1>n3)and(n1>n4):
    print("{0} is greatest among them".format(n1))
elif(n2>n1)and(n2>n3)and(n2>n4):
    print("{0} is greatest among them".format(n2))
elif(n3>n1)and(n3>n2)and(n3>n4):
    print("{0} is greatest among them".format(n3))
else:
    print("{0} is greatest among them".format(n4))
'''

# Write a program to check vowel or consonant.
'''
str1= str(input("enter the character "))
if(str1=='a'or str1=='e'or str1=='i' or str1=='o' or str1=='u'):
    print("{0} is vowel".format(str1))
else:
    print("{0} is consonat".format(str1))
'''

# Write a program to check whether a character is an alphabet, a digit or any other special symbol.
'''
str1=(input("enter the char "))
if(str1>='a' and str1<='z')or(str1>='A' and str1<='Z'):
    print("{0} is a alphabet".format(str1))
elif(str1>=0 and str1<=9):
    print("{0} is a digit".format(str1))
else:
    print("{0} is a digit".format(str1))
'''

# Write a program to check the given number is less than or equal to 20 or 40 or 60 or greater than 60.
'''
n =int (input("enter the number"))
if(n<20):
    print("{0} is less than 20".format(n))
elif(n<40):
    print("{0} is less than 40 ".format(n))
elif(n<60):
    print("{0} is less than 60".format(n))
else :
    print("{0} is greater than 60".format(n))
'''

# Write a program to input basic salary of an employee and calculate its Gross salary and according to following condition:

# Basic Salary <= 10000: HRA = 20%, DA = 80%

# Basic Salary <= 20000: HRA = 25%, DA = 90%

# Basic Salary > 20000 : HRA = 30%, DA = 95%

# Deduction PPF 10%
'''
def salary_data(basic_salary):
    
    if(basic_salary<=10000):
        DA = basic_salary*0.8
        HRA = basic_salary*0.2
    elif(basic_salary<=20000):
        DA = basic_salary*0.9
        HRA = basic_salary*0.25
    else:
        DA = basic_salary*0.95
        HRA = basic_salary*0.3
    Net_salary = basic_salary +DA +HRA
    PPF = Net_salary*0.2
    Gross_salary  = Net_salary-PPF

    print("BASIC SALARY   :    {0}".format(basic_salary))
    print("DA             :    {0}".format(DA))
    print("HRA            :    {0}".format(HRA))
    print("----------------------------")
    print("Net Salary     :    {0}".format(Net_salary))
    print("PPF            :   -{0}".format(PPF))
    print("----------------------------")
    print("Gross Salary   :    {0}".format(Gross_salary))

Basic_salary = int (input("Enter your Basic Salary "))
salary_data(Basic_salary)
'''

# Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:

# For first 50 units Rs. 0.50/unit

# For next 100 units Rs. 0.75/unit

# For next 100 units Rs. 1.20/unit

# For unit above 250 Rs. 1.50/unit

# An additional surcharge of 20% is added to the bill
    
'''
def Total_bill(Unit):
    if(Unit<=50):
        bill = unit*0.5
    elif(Unit<=150):
        bill= 50*0.5+(Unit-50)*0.75
    elif(Unit<=250):
        bill= 50*0.5+100*0.75+(Unit-150)*1.20
    else:
        bill= 50*0.5+100*0.75+100*1.20+(Unit-250)*1.50
    SurCharge = bill*0.2
    Final_bill = SurCharge+bill
    print("Total bill = {0}". format(Final_bill))

Unit = int (input("Enter the unit of electricity consumed"))
Total_bill(Unit)
'''



