# i=1
# while i<=10:
#   print(f"Index {i} : yep that it ")
#   i+=1



#   #pirnt 1 to 20 natural num
# i=1
# while i<=20:
#     print(i)
#     i+=1


# 3 print first 30 odd numbers


# 30 narutal number 

#4 20 first even numbers

# i=1
# d=1
# while i<30:
#   print(f"index:{i}  {d}") # to use different variable than loops

#   i+=1
#   d+=2

#  fist 40 natural number sum:

# i=1
# sum=0
# while i<=40:
#   i+=1
#   sum=sum+i
# print(f"the sum first 40 Natural numbers : {sum}") 

# i=1
# e=1
# while i<=20:
 
#   i+=1
#   i%2==0
#   print(e)
# i=1
# a=1
# sum=0
# # for i in range (1,20):
# while i<20:
#  a+=1
#  i+=1
# if a%2==0:
#  sum=sum+a
#  i

# print(sum)




# calculating sum of 20 numbers

# i=1
# sum1=0
# even=0
# while i<=20:

#   even+=1
#   if even%2==0:
#     sum1=sum1+even
#     # print(f"index:{i} {even}")
#     i+=1
# #     sum=sum+even
# print(f"the sum of first 20 even number is {sum1}")
  
     
  


# def cunter(n):
#   while n>0:
#     print(f"rocket launch start in  {n} ")
#     n-=1
#   print("lift upppppppppppppppppppppp")
    
# cunter(4)


# user will specify how much number he want to print of even numbers


# def even(n):
#   sum1=1
#   add=0
#   while sum1<=n:
   
#     if sum1%2==0:
#       add=add+sum1
#     sum1+=1
#   return add
# n=int(input("enter num"))

# print(even(n))



# Vending machine simulation
# def vending_machine():
#     items = {"Soda": 1.50, "Chips": 1.00, "Candy": 0.75}
    
#     print("Items available:")
#     for item, price in items.items():
#         print(f"{item}: ${price:.2f}")
    
#     total_money = float(input("Insert money (e.g., 5.00): "))
    
#     while total_money > 0:
#         choice = input("Select an item (or type 'exit' to finish): ").capitalize()
        
#         if choice == 'Exit':
#             print(f"Returning ${total_money:.2f} change.")
#             break
#         elif choice in items:
#             item_price = items[choice]
#             if total_money >= item_price:
#                 total_money -= item_price
#                 print(f"Dispensing {choice}. Remaining balance: ${total_money:.2f}")
#             else:
#                 print("Insufficient funds. Please add more money or choose a cheaper item.")
#         else:
#             print("Invalid selection.")
    
#     if total_money == 0:
#         print("No money left. Thank you for using the vending machine!")

# # Run the vending machine simulation
# vending_machine()

# 1,5,9 squeence from 1 to 10th terms where space from each 4
# i=1
# p=1
# for i in range(1,11):
#   p=1+4
#   p+=1
#   print(p)

# i=1
# c=1
# while  i<11:
#   print(f"index{i} : {c}")
#   c=c+4
#   i+=1

 
#2 print sum of 10 even numbers:
# sum1=0
# a=0
# for i in range(1,21):
#   sum1=sum1+a
#   a=a+2
# print(sum1)








  

# #2 89,86,83 up to 10 terms
# i=1
# c=89
# while  i<11:
#   print(f"index{i} : {c}")
#   c=c-3
#   i+=1


#3 20,33,48:up to 10th terms

#4 1,4,9 

# i=1

# while  i<11:
#  print(f"index:{i} = {i*i}")
#  i+=1
 


#5
# 8,27,64
# i=2

# while  i<11:
#  print(f"index:{i} = {i*i*i}")
#  i+=1
 

# #6 
# #1,2,9,4,25 hint odd is square 
# i=1
# c=1
# while  i<11:
#   if c%2==0:
#     print(f"index{i} = {c}")
#   else:
#     print(f"index{i} = {c*c}")
#   c+=1
#   i+=1

  
#7 
# 1,4,27,16 even squARE or odd xa vane cube

# i=1
# c=1
# while  i<11:
#   if c%2==0:
#     print(f"index{i} = {c*c}")
#   else:
#     print(f"index{i} = {c*c*c}")
#   c+=1
#   i+=1


# #8 1,1,2,3,5 
# i = 1
# num1 = 1
# num2 = 1

# while i <= 10:
#     print(num1)
#     nexValue = num1 + num2  # Calculate the next Fibonacci number
#     num1 = num2  # Move num2 to num1
#     num2 = nexValue  # Move nexValue to num2
#     i += 1


# n = int(input("Enter num:"))

# if n % 2 == 0:
#     if 2 <= n <= 5:
#         print("Not Weird")
#     elif 6 <= n <= 20:
#         print("Weird")
#     elif n > 20:
#         print("Not Weird")
# else:
#     print("Weird")

    
#   # a program to print  the first 20 whole numbers
# i=1
# w=0
# while (i<=20):
#   print(w)
#   i=i+1
#   w=w+1

#find the sum of first 20 whole number

# i=1
# w=0
# sum=0
# while (i<20):
#   w=w+1
#   i=i+1
# #   sum=sum+w

# print(sum)



# find multiplication table of 6 up to 10 the terms


# i=1

# while(i<=10):
#   mul=6*i
#   print(f"{6} * {i} = {mul}") 
# #   print("6*"+ str(i))
#   i+=1


# #TO PRINT MULTIPLICATION TABLE FROM 1 TO 10 UP TO 10 TH TERMS
# j = 1
# while j <= 10:  # Rows from 1 to 10
#     i = 1
#     while i <= 10:  # Columns from 1 to 10
#         print(f"{i} * {j} = {i * j}",)
#         i += 1
#     print()  # Move to the next line after each row is complete
#     j += 1

   

# #disaply the number between 100 to 500 and also divisble by 7
# i=100
# while(i<=500):
#         if i%7==0:
#                 print(i)
#         i+=1
               

#sum of all numbers between 50 to 1000 so that also divisble by 9 and 13

# i=50
# sum=0
# while(i<=500):
#   sum=sum+i
#   i+=1
#   if(sum%9==0 and sum%13==0):
#    print(sum)




# to find the multiplication  table of user given number
# i=1
# n=int(input("which multilication table you want to print"))
# while(i<=10):
#   pro=n*i
#   print(f" {n} *  {i} = {pro}")
#   i+=1
  
# # #to find the reverse of a given number
# n=int(input("Enter the number which you want to do reverse :"))
# rer=0
# num=n
# sum=0
# while n!=0:
#   lastNum=n%10
#   rer=rer*10+lastNum
#   sum=sum+lastNum
#   n=n//10


# if(num==rer):
 
#   print(f"{num} is palidrome")



# print(f"{rer} is rerverse of {n}")

# print(f"the sum is {sum}")



#ARMStrom NUMbers

# n=int(input("Enter the number :"))
# digitNum=str(len(n))
# Arms=sum((int(digit)**digitNum for digit in n))

# i=1

# while(i<=5):
#   j=1

#   while(j<=i):
#    print(j , end="\t")
#    j+=1
#   print()
#   i+=1
 


   
  


   



   
 
     


 

  


  
