# is import sys necessary?
# import sys

print ("Let's experiment with the Fibonacci and Lucas Numbers Series.")

# Fibonacci series

print ("First let's work with the Fibonacci Series.")

n = raw_input("Please type any number. Don't include any commas or negative numbers! > ")
i = int(n)


def fibonacci(i):
    if (i == 0):
        return(0)
    elif (i == 1):
        return(1)
    elif (i > 1):
        return(fibonacci(i - 1) + fibonacci(i - 2))

# should I call the function now or later in "part 3" or "finally" section?
# print fibonacci(i)

# Lucas Numbers

print ("Now let's work with Lucas Numbers Series.")

l = raw_input("Please type any number and don't use commas or negative numbers. > ")
m = int(l)


def lucas(m, ):
    if (m == 0):
        return(2)
    elif (m == 1):
        return(1)
    elif (m > 1):
        return(lucas(m - 1) + lucas(m - 2))

# should I call this function now or in part 3 or "finally"?
print lucas(m)


# part 3 "sum series" - this is where I'm not sure how to proceed. ignore the code.
# it's a rough draft, incomplete, and incorrect.

r = raw_input("Please call the Fibonacci function by typing in one paramater.  Call the Lucas function by typing in one paramater + 2, 1. > ")
s = int(r)


"""def sum_series(s, *args):
       if (b == 0):
        return(0)
    elif (i == 1):
        return(1)
    elif (i > 1):
        return(fibonacci(i - 1) + fibonacci(i - 2))

def sum_series (m, )"""

def sum_series(s, *args):
    if args = 2 or args = 1:
        print lucas(s, args)
