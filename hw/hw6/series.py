print ("Let's experiment with the Fibonacci and Lucas Numbers Series.")

# Fibonacci series

print ("First let's work with the Fibonacci Series.")

n = input("Please type any number with no commas or negative numbers. > ")
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

l = input("Please type any number with no commas or negative numbers. > ")
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

r = input("Let's call the sum_series function. Please type any number; no negatives or commas. > ")
s = int(r)

"""This function calls either the Fibonacci or Lucas function based on optional parameters."""
def sum_series(s, x=0, y=1):
    if (x == 0 and y == 1):
        return(fibonacci(s))
    if (x == 2 and y == 1):
        return(lucas(s))

print ("Fibonacci Series:", sum_series(s))
print ("Lucas Series:", sum_series(s, x=2, y=1))
