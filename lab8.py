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
