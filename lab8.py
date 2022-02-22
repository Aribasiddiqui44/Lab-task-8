LAB 7:
QUESTION 1:

1.	Use  inbuilt min and max functions to perform the task of getting the minimum and maximum 
value of  in a list of tuples for a particular element position in a tuple.
Sample  = [(2, 3), (4, 7), (8, 11), (3, 6)]

CODE:
Sample  = [(2, 3), (4, 7), (8, 11), (3, 6)]
for i in Sample:
    print("Maximun in",i,"is",max(i))
    print("Minimum in",i,"is",min(i))
    print()
    
OUTPUT:
Maximun in (2, 3) is 3
Minimum in (2, 3) is 2

Maximun in (4, 7) is 7
Minimum in (4, 7) is 4

Maximun in (8, 11) is 11
Minimum in (8, 11) is 8

Maximun in (3, 6) is 6
Minimum in (3, 6) is 3



QUESTION 2:
2.   A dartboard of radius 10 and the wall it is hanging on are represented using the two dimensional
coordinate system, with the board’s center at coordinate (0; 0). Variables x and y store the x- and 
y-coordinate of a dart hit. Write an expression using variables x and y that evaluates to True if the
dart hits (is within) the dartboard, and evaluate the expression for these dart coordinates:
(a) (0; 0)
(b) (10; 10) (c) (6; 6)
(d) (7; 8)

CODE:
import math
a=0
b=0
for  i in range(4):
    x=int(input("Enter x co_ordinate"))
    y=int(input("Enter y co_ordinate"))
    d=math.sqrt((x-a)*2 + (y-a)*2)
    if(d<=10):
        print("Dart is within the dartboard")
    else:
        print("Dart is outside the dart board")
    print()
OUTPUT:
Enter x co_ordinate 0
Enter y co_ordinate 0
Dart is within the dartboard

Enter x co_ordinate 10
Enter y co_ordinate 10
Dart is within the dartboard

Enter x co_ordinate 6
Enter y co_ordinate 6
Dart is within the dartboard

Enter x co_ordinate 7
Enter y co_ordinate 8
Dart is within the dartboard



QUESTION 3:
 Write Python expressions corresponding to these statements:
(a)The number of characters in the word "anachronistically" is 1 more than the number of characters
in the word "counterintuitive."
(b)The word "misinterpretation" appears earlier in the dictionary than the word "misrep- resentation."
(c)The letter "e" does not appear in the word "ﬂoccinaucinihilipiliﬁcation."
(d)The number of characters in the word "counterrevolution" is equal to the sum of the number of
characters in words "counter" and "resolution

CODE:
word1="anachronistically"
word2="counterintuitive"
print(len(word1)==len(word2)+1)
word3="misinterpretation"
word4="misrepresentation"
print((word3<word4))
word5="ﬂoccinaucinihilipiliﬁcation"
print("e" in word5)
word6="counterrevolution"
word7="counter"
word8="resolution"
print(len(word6)==len(word7)+len(word8)    
    
   
OUTPUT:
True
True
False
True


QUESTION 4:
Write a program in Python that holds an empty tuple and fill that tuple after taking 
user input for names of provinces of Pakistan n fill an empty tuple and print.
      
CODE:
  Tupl=()
l1=list(Tupl)
print("Enter provinces name")
for i in range(4):
    x=input()
    l1.append(x)
Tupl=tuple(l1)
print(Tupl)

      
OUTPUT:
 Enter provinces name
Sindh
Punjab
Balochistan
KPK
('Sindh', 'Punjab', 'Balochistan', 'KPK')

QUESTION 5:
  5. Start by assigning to variables monthsL and monthsT a list and a tuple, respectively,
      both containing strings 'Jan', 'Feb', 'Mar', and 'May', in that order. Then attempt 
      the following with both containers:
(a)Insert string 'Apr' between 'Mar' and 'May'. (b)Append string 'Jun'.
(c)Pop the container.
(d)Remove the second item in the container. (e)Reverse the order of items in the container.
Note: when attempting these on tuple monthsT you should expect errors.
 CODE:
            # FOR LIST
      INPUT:
      
monthsL=["Jan","Feb","Mar","May"]

monthsL.insert(3,"Apr")
print(monthsL)
monthsL.append("Jun")
print(monthsL)
monthsL.pop()
print(monthsL)
monthsL.remove("Feb")
print(monthsL)
monthsL.reverse()
print(monthsL)
      
      
      OUTPUT:
['Jan', 'Feb', 'Mar', 'Apr', 'May']
['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
['Jan', 'Feb', 'Mar', 'Apr', 'May']
['Jan', 'Mar', 'Apr', 'May']
['May', 'Apr', 'Mar', 'Jan']
  
 # FOR TUPLE
      CODE:
      
monthsT=("Jan","Feb","Mar","May")
monthsT.insert(3,"Apr")
print(monthsT)
monthsT.append("Jun")
print(monthsT)
monthsT.pop()
print(monthsT)
monthsT.remove("Feb")
print(monthsT)
monthsT.reverse()
print(monthsT)
      
      OUTPUT:
Traceback (most recent call last):
  File "C:\Users\computer lab\AppData\Roaming\JetBrains\PyCharmCE2021.3\scratches\scratch_15.py", line 5, in <module>
    monthsT.insert(3,"Apr")
AttributeError: 'tuple' object has no attribute 'insert'

      
    
























# LAB 8 QUESTION 1

# 1.Construct the strings by using the string time format function strftime ()

#   a) (Thursday, July 13 2018')
#   b) ('09:40 PM Central Daylight Time on 07/13/2018')
#   c) ('I will meet you on Thu July 13 at 09:40 PM.')

CODE OF QUESTION 1:
    
from datetime import datetime

timestamp = 1531543200
date_time = datetime.fromtimestamp(timestamp)
print(date_time)
d = date_time.strftime("(%A, %B %d %Y')")
print(d)

d = date_time.strftime("('%I:%M %p Central Daylight Time on %m/%d/%Y')")
print(d)

d = date_time.strftime("('I will meet you on %a %B %d at %I:%M %p.')")
print(d)




# LAB 8 QUESTION 2:

#     2. Assuming that variable forecast has been assigned string 'It will be a sunny day today' Write Python statements corresponding to these assignments:
#    (a) To variable count, the number of occurrences of string 'day' in string forecast. (b) To variable weather, the index where substring 'sunny' starts.
#    (c) To variable change, a copy of forecast in which every occurrence of substring 'sunny' is replaced by 'cloudy'.

# CODE OF QUESTION 2:

forecast = "It will be a sunny day today"
count = forecast.count("day")
weather = forecast.index("sunny")
change = forecast.replace("sunny","cloudy")
print(" forecast = ", forecast, "\n", "count = ", count, "\n", "weather = ", weather, "\n", "change = ", change)
print("\n")




# LAB 8 QUESTION 3:

#   3.   Write function even() that takes a positive integer n as input and prints on the screen all numbers between, and including, 2 and n divisible by 2 or by 3, using this output format:
#   >>> even(17)
#   2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16,
 
    
# CODE OF QUESTION 3:

def even(x):
    for i in range(2,x+1):
        if(i%2==0)or(i%3==0):
            print(i,end=" ")
num=int(input("Enter any positive integer:"))
print(even(num))



# LAB 8 QUESTION 4:
4.   Assume variables first, last, street, number, city, state, zipcode have already been assigned. Write a print statement that creates a mailing label:
 
# CODE OF QUESTION 4:

first = "John"
last = "Doe"
street = "Main Street"
number = "123"
city = "Karachi"
state = "Pakistan"
zipcode = "09876"
print(first + " " + last + "\n", number + " " + street, "\n" + city + ", " + state + ", " + zipcode)



# LAB 8 QUESTION 5:
# 
5.   Translate each part into a Python statement using appropriate string methods:
#   (a) Assign to variable message the string 'The secret of this message is that it is secret.' 
#   (b) Assign to variable length the length of string message, using operator len().
#   (c) Assign to variable count the number of times the substring 'secret' appears in string message, using string method count().
#   (d) Assign to variable censored a copy of string message with every occurrence of substring
'secret' replaced by 'xxxxxx', using string method replace(). 

# CODE OF QUESTION 5:

message = "The secret of this message is that it is secret."
length = len(message)
count = message.count("secret")
censored = message.replace("secret", "xxxxxx")
print("message=", message,"\n", "length=", length,"\n", "count=", count,"\n", "censored=", censored)
print()




# LAB 8 QUESTION 6:
# 6.   Write a function month() that takes a number between 1 and 12 as input and returns the
three-character abbreviation of the corresponding month. Do this without using an if statement, just string operations. Hint: Use a string to store the abbreviations in order.
#     >>> month(1)
#     'Jan'
#     >>> month(11)
#    'Nov'

# CODE OF QUESTION 6:

def month(x, y):
    print(y[x - 1:x])

num = int(input("Enter any number in between 1 to 12"))
abr = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
month(num, abr)



or 
# LAB 8 QUESTION 6

def month(n):
    a = "Jan"
    b = "Feb"
    c = "Mar"
    d = "Apr"
    e = "May"
    f = "Jun"
    g = "Jul"
    h = "Aug"
    i = "Sep"
    j = "Oct"
    k = "Nov"
    l = "Dec"
    while n == 2:
        print("The month is ",b)
        break
    while n == 3:
        print("The month is ",c)
        break
    while n == 4:
        print("The month is ",d)
        break
    while n == 5:
        print("The month is ", e)
        break
    while n == 6:
        print("The month is ", f)
        break
    while n == 7:
        print("The month is ",g)
        break
    while n == 8:
        print("The month is ",h)
        break
    while n == 9:
        print("The month is ",i)
        break
    while n == 10:
        print("The month is ",j)
        break
    while n == 11:
        print("The month is ",k)
        break
    while n == 12:
        print("The month is ",l)
        break

x = int(input("Enter a month no.="))
month(x)



# LAB 8 QUESTION NO.7:

def cheer(team):
    print("How do you spell winner?","\n","I know ,I know!",team.upper()+"!","\n","And that is how you spell winner!","\n","Go",team,"!")

name=input("Enter team name:")
cheer(name)
