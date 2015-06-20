"""print "Let's experiment with the Fibonacci and Lucas Numbers Series."

# Fibonacci series

print "First let's work with the Fibonacci Series."

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

print "Now let's work with Lucas Numbers Series."

l = raw_input("Please type any number and don't use commas or negative numbers. > ")
m = int(l)


def lucas(m):
    if (m == 0):
        return(2)
    elif (m == 1):
        return(1)
    elif (m > 1):
        return(lucas(m - 1) + lucas(m - 2))

# should I call this function now or later?
print lucas(m)"""

# part 3 "sum series"

"""print "And finally you can choose Lucas or Fibonacci by following these instructions."
print "If you would like to run the Fibonacci Series, type just ONE number, and it may be any number you like."
print "If you sould like to run the Lucas Series, type any number followed by 2 and 1.  For example, 6 2 1."

# r = raw_input("Please type a number or numbers as described above. > ")
# s = int(r)"""


def sum_series(s, b=0, c=1):
       if (i == 0):
        return(0)
    elif (i == 1):
        return(1)
    elif (i > 1):
        return(fibonacci(i - 1) + fibonacci(i - 2))

def sum_series (m, )
