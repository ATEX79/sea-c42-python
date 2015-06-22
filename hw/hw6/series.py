# is import sys necessary?
# import sys

print ("Let's experiment with the Fibonacci and Lucas Numbers Series.")

# Fibonacci series

print ("First let's work with the Fibonacci Series.")

n = input("Please type any number. Don't include any commas or negative numbers. > ")
i = int(n)


def fibonacci(i):
    if (i == 0):
        return(0)
    elif (i == 1):
        return(1)
    elif (i > 1):
        return(fibonacci(i - 1) + fibonacci(i - 2))


print (fibonacci(i))

# Lucas Numbers

print ("Now let's work with Lucas Numbers Series.")

l = input("Please type any number and don't use commas or negative numbers. > ")
m = int(l)


def lucas(m):
    if (m == 0):
        return(2)
    elif (m == 1):
        return(1)
    elif (m > 1):
        return(lucas(m - 1) + lucas(m - 2))

print (lucas(m))


# Sum Series

r = input("Let's call the Fibonacci and Lucas functions again by typing in one paramater. > ")
s = int(r)


def sum_series(s, x=0, y=1):
    if (x == 0):
        return(0)
    elif (y == 1):
        return(1)
    elif (s > 1):
        return(sum_series(s - 1) + sum_series(s - 2))

print ("Fibonacci:", sum_series(s), "Lucas:", sum_series(s, x=2, y=1))
