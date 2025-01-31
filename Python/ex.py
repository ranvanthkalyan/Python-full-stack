'''#print("This doesnot "execute")
#print("This will\"execute")
#print('This will "execute"')


#print("Hey",6,7,sep="^")
#print("Hey",6,7,sep="^",end="00312")
#print("Minnu")'''

#Type Casting
'''a="15"
b=3
c=int(a)
d=b+c
print(d)

a=3.12
b=12
c=a+b
print(c)'''


#Taking user input
'''a=int(input())
b=float(input())'''

#strings
'''name = "Minnu"
print("Hello" + name)

a= """ welcome to Programming
The programming is easy"""
print(a)'''

#Accessing characters of a string
'''name="Minnu"
print(name[0])
print(name[3])
a="""welcome to Programming
The programming is easy"""
for character in a:
    print(character)'''


#length of a string
'''name="Minnu"
len1=len(name)
print(len(name))'''

#String slicing
'''a="ApplePie"
print(a[:5])# Slicing from start
print(a[5:])# slicing till end
print(a[2:6])# slicing in between
print(a[-8])# Slicing using -ve index'''


#String methods
'''str = "ABcdeFgHi"
print(str.upper())#changes the alphabets to uppercase
print(str.lower())#changes the alphabets to lowercase
#strip() methods removes any white spaces before and after the string
#rstrip()"            "    " trailing characters
str="Hello!!!"
print(str.rstrip("!"))
print(str.replace("H","R")) # replace() method replaces all occurences of a string with another string
str2="Sliver Spoon"
print(str2.split())'''



#If-else
'''a=120
b=100
if (a<=b):
    print("true")
else:
    print("false")
#elif
a=0
if (a<0):
    print("-ve")
elif(a==0):
    print("0")
else:
    print("+ve")
#Nested if
a=18
if (a<0):
    print("-ve")
elif(a>0):
    if (a<=10):
        print("b/w 1-10")
    elif(a>10 and a<=20):
        print("b/w 11-20")
    else:
        print("greater than 20")
else:
    print("Zero")'''


#Match Case
'''x=4 #x is the variable to match
match x:
    #if x is 0
    case 0:
        print("x is zero")
    #case with if condition
    case 4 if x%2==0:
        print("x%2==0 and case is 4")
    #empty case with if condition
    case _ if x<10:
        print("x is < 10")
    #default case(will only be matched if the above cases were not matched)
    #so it is basically just an else
    case _:
        print(x)'''

#the for loop
'''name='Minnu'
for i in name:
    print(i,end=",")
colours=("Blue","White","Yellow","Red")
for x in colours:
    print(x)
for k in range(4,9):
    print(k)'''

#While loop
'''x=5
while(x>0):
    print(x)
    x=x-1'''
#else with while loop
'''x=5
while(x>0):
    print(x)
    x=x-1
else:    
    print('counter is o')'''

#do-while loop
'''while True :
    a=int(input("Enter a +ve no:"))
    print(a)
    if not a>0:
        break'''

#Break statement
'''for i in range(1,101,1):
    print(i,end=" ")
    if (i==50):
        break
    else:
        print("Mississippi")
print("Thank You")'''

#Continue statement
'''for i in[2,3,4,6,8,0]:
    if(i%2!=0):
        continue
    print(i)'''

#Python Functions
def function_name(parameters):
    pass
    #code and statements

def name(fname,lname):
    print("Hello,",fname,lname)
name("sam","Wilson")
