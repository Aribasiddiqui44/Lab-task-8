# LAB 8 QUESTION 5
message = "The secret of this message is that it is secret."
length = len(message)
count = message.count("secret")
censored = message.replace("secret", "xxxxxx")
print("message=", message,"\n", "length=", length,"\n", "count=", count,"\n", "censored=", censored)
print()


# lab 8 Qno.4

first = "John"
last = "Doe"
street = "Main Street"
number = "123"
city = "Karachi"
state = "Pakistan"
zipcode = "09876"
print(first + " " + last + "\n", number + " " + street, "\n" + city + ", " + state + ", " + zipcode)


# lab 8 Qno.6

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
