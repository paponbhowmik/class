# Q1: take values of length breadth of a rectangle from user and check if it is square or not.
length = int(input("type a length value: "))
breadth = int(input("type a breadth value: "))
if length==breadth:
    print("The rectangle is a square.")
else:
    print("The rectangle is not a square.")

# Q2: A shop will give discount of 10% if the cost of purchased quantify is more than 1000. Ask user for quantity suppose, one unit will cost 100. judge and print total cost for user.
purchase = int(input("Give the value of how much you bought: "))
purchase*=100
if purchase > 1000:
    print(purchase - (purchase*.10))
else:
    print("No discount")

# Q3: A school has following rules for grading system:
# a.Below 25 - F
# b.25 to 45 - E
# c.45 to 50 - D
# d.50 to 60 - C
# e.60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.
a = int(input("Enter your mark: "))
if a < 25 :
    print("F")
elif a < 45 :
    print("E")
elif a < 50 :
    print("D")
elif a < 60 :
    print("C")
elif a < 80 :
    print("B")
elif a < 80 :
    print("B")
else:
    print("A")

# Q4: Write a program to print absolute value of a number entered by user. E.g-
#     INPUT : 1 OUTPUT : 1
#     INPUT : 1 OUTPUT : 1
number = int(input("Type a nymber: "))
if number < 0 :
    print(-number)
else:
    print(number)

# Q5: ask input of age of 3 people by user and determine oldest and youngest among them.
age1=int(input('enter age1: '))
age2=int(input('enter age2: '))
age3=int(input('enter age3: '))
if age1>age2 :
    print('age1 is oldest')
elif age1>age3 : 
    print('age1 is oldest')
elif age2>age1 :
    print('age2 is oldest')
elif age2>age3 :
    print('age2 is oldest')
else:
    print('age3 is oldest')
if age1<age2 :
    print('age1 is youngest')
elif age1<age3 :
    print('age1 is youngest')
elif age2<age1 :
    print('age2 is youngest')
elif age2<age3 :
    print('age2 is youngest')
else:
     print('age3 is youngest')

# Q6: A student will not be allowed to sit in exam if his/her attendence is less than 75%. Take following input from user Number of classes held Number of classes attended. And print percentage of class attended is student is allowed to sit in exam or not.
attendence = float(input("Type your attendence percentage: "))
a = (100*0.75)
if attendence < a:
    print("not allow")
elif attendence >= a :
    print("allow")
else:
    print("wrong percentage")

# Q7: Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ('Y' or 'N') and print accordingly.
b = input("Type your medical issue yes/no: ")
c = ("yes")
d = ("no")
if b == c:
    print("allow student to sit")
elif b == d:
    print("not allow student to sit")
else:
    print("Error")
