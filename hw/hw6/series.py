print "Let's experiment with the Fibonacci Sequence."

n = raw_input("Please type any number. Don't include any commas! > ")
i = int(n)


def fib(i):
    x = (i - 1) + i
    return x

print fib(i)
