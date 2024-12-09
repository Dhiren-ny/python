# #1 to calculate the rectagle area

# l=int(input("Enetr the length of rectangle  : "))
# b=int(input("Enetr the length of rectangle  : "))
# print(f"The area of rectangle is  {l *b}cm^2")


#2
# nameP=input("What your name sir/madam")
# MonthlyIncome=int(input("Enter the monthly income :  "))
# numberKids=int(input("how many kids yoi have "))
# tax=0.25*((MonthlyIncome*11)-(numberKids*450))

# print(f"{nameP} you needed to pay {tax} amount ")


#3 to take input from the user add 5 and double it and subtract -7

# n=int(input("HEY buddy eneter the number you want :"))
# n=(n+5)*2 -7
# print( f" dam it is your number man {n} ")


# #4 calculate the are and circumference of circle

# Radius=float(input("Radius :"))
# pi=3.14
# print(f"the are of cricle is {pi*(Radius**2)}")
# print(f"circumference of circle is {2*pi*Radius}")





# 5 calculate and print avg of three numbers
# def avg():
 
#   num1,num2,num3 = map(int,input("Enter 3 numbers man :").split())
#   avergae=(num1+num2+num3)/3
#   print(avergae)

# avg()




#lap 2

# #1Using a while loop, asks the user to enter a number, and prints a countdown from the number entered by the user to zero.

# num=int(input("Entwe the number :"))
# while num!=0:
#   print(num)
#   num-=1



# #2 Check if the number enter is a positive number, negative number or zero.
# def check():
#   num = int(input("Enter a number: "))
#   if num > 0:
#     print("The number is positive ")
#   elif num < 0:
#     print("The number is negative")
#   else:
#     print("The number is zero")
# check()



  
# # 3
#   Find the largest numbers between 3 numbers.


# a=2
# i=1
# while i!=10:
#   if a%2==0:
#     print(a**3)
#   else:
#     print(a**2)
#   i+=1
#   a+=1

  
# #4 4. Check year enter is a leap year or not a leap year.

# year=int(input("Enter the year:"))
# if year%4==0 and (year%100!=0 or year%400==0):
#   print("The year is a leap year")
# else:
#   print("it is not the leap a year")



# lap assignment 3

# learn to use print function:
#1 print hello

# print("hello")

#2 write a program to input as a words from a usr and then display by saying welcome

# name=input("hello buddy what sup and what your Name :")
# print(f"welcome , {name} ")


# #input 2 input what ever from the usr and display it


# name=input("hello buddy what sup and what your Name :")
# age=int(input("enter your age  :"))

# print(f"{name}  and {age}")

# # part b test
# num1=int(input("Number 1: "))
# num2=int(input("Number 2: "))
# n=int(input("which operation you want to do perform\n  1. addition\n 2. subtraction\n 3. division\n 4. modulo" ))

# if n==1:
#   print(f"Addition of {num1} + {num2} = {num1+num2}")
# elif n==2:
#    print(f"sub  of {num1} - {num2} = {num1-num2}")
# elif n==3:
#    print(f"division  of {num1} / {num2} = {num1/num2}")
# elif n==4:
#    print(f"module of {num1} % {num2} = {num1%num2}")
# else:
#    print("Enter valid option from the screen ")

  #  5 and 6 is remaining


#LAB 4: CONTROL STRUCTURE IN PYTHON – CONDITIONAL STATEMENT
# 1. Write a program to check if the given number is even or odd.

# def oddEven(n):
#   if (n%2==0):
#     return f" {n} is even"
#   else:
#      return f" {n} is odd"

# print(oddEven(3))

#2 2. Based on the following table, write a program that determines if your score will pass the
#  50> pass
# else 
# fail

# def Mark(n):
#   if n>50:
#     return f"pass"
#   else:
#     return f"fail"
# print(Mark(60))


# . Write a PYTHON program to find largest of three numbers

# def greatestThree():
#   a=int(input("Enter num 1 :"))
#   b=int(input("Enter num 2 :"))
#   c=int(input("Enter num 3 :"))
#   if a>b and a>c:
#     print(f"{a} is greatest")
#   elif b>c:
#    print(f"{b} is greatest")
#   else:
#      print(f"{c} is greatest")

# greatestThree()


# 4. Write a program to display profit or loss in trading of an item.
# Sample input/output:
# Enter selling price: 20
# Enter buying price:19
# You have profit in trading of this item




# def ProfitLoss():
#   sP=int(input("Enter selling price of object :"))
#   cP=int(input("Enter cost price of object :"))
#   if sP>cP:
#     print("you gained profit ")
#   else:
#     print("you have loss ")
    
# ProfitLoss()

# 2. Write a PYTHON program to check entered character is vowel or consonant.

# def CheckLetter():
#   l=input("Enter the letter man:")
#   if l=='a' :
#     print("its vowel")
#   elif l=='e':
#     print("its vowel")
#   elif l=='i':
#      print("its vowel")
#   elif l=='o':
#      print("its vowel")
#   elif l=='u':
#     print("its vowel")
#   else:
#     print("its consonant.")


# CheckLetter()


# # Write a PYTHON program to find smallest of three numbers.

# def smallestThree():
#   num=list(map(int,input("Enter three numbers : ").split()))




# smallestThree()



# LAB 5: CONTROL STRUCTURE IN PYTHON – REPETITI

# i=1
# for i in range(1,50):
#   if i%2==0:
#     print(f"{i} \t" )
    

# Part B: Test yourself!
# 1. Write a Python program to display numbers from 1 to 20. Note: use all types of repetitive structures


# #1 for loop
# i=1
# for i in range(1,20):
#   print(i)


# #2 while looop
# i=1
# while (i!=21):
#   print(i)
#   i+=1

# # 2. Write a Python program to create a multiplication table


# n=7
# i=1
# while (i!=11):
#   print(f"{n} * {i} = {n*i}")
#   i+=1
  




#   4. Write a Python program to construct the following pattern, using a nested for loop. 
  
# * 
# **
# ***
# ****
# ******

# row=5
# for i in range(row):
#    for j in range(i):
#       print("* ",end=" ")
#    print("")

 
  # LAB 6: FUNCTION IN PYTHON
  

  # 2. Write a program to create function calc() that will accept two variables and calculate the two variables. Hint: Use addition and subtraction.

# def calc(num1,num2):
#     return print(f"the sum of {num1+num2}, and the diff is {num1-num2}")


# calc(10,5)
 
# Function with a default argument
# 3. Write a program to create a function named employee() using the following conditions:
# a. Program should accept the employee’s name and salary and display both.
# b. If the salary is missing in the function call, then assign default value 9000 to salary


# def employee(name,salary=9000):
#   print(f"Employee name: {name}, Salary: {salary}")
# employee("dhiren" ,"400")



# Inner function to calculate the addition
# 4. Write a Python program to create the following:
# a. Create an outer function that will accept two parameters, y and z.
# b. Create an inner function inside an outer function that will calculate the addition of y and z.
# c. Lastly, the outer function will add 5 into addition and return it




  

  




   
       

   

  
