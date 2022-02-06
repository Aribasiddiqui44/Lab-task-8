# LAB 8 QUESTION 5
message = "The secret of this message is that it is secret."
length = len(message)
count = message.count("secret")
censored = message.replace("secret", "xxxxxx")
print("message=", message,"\n", "length=", length,"\n", "count=", count,"\n", "censored=", censored)
print()

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
