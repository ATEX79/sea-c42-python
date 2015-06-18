def exhibit_name_error():
    print(foo)

def exhibit_type_error():
    print(3 + "a")

def exhibit_attribute_error():
    x = "4.5"
    print (x.__div__(2))

exhibit_name_error()
exhibit_type_error()
exhibit_attribute_error()

# To run this code properly, you need to comment out the other functions, save it,
# then run the code. Repeat for each of the functions to test each error message.
# Code worked as planned.
# Big thanks to Spencer who helped with the code.
