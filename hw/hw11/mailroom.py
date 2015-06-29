"""
=====================================================================
Goals and Objectives:

(1) Write a list function to print donors to the screen,
        * complete, function name is print_list()
(2) Write a function to see if input is a number,
        * still incomplete.
(3) Write a function to search the list of donors for a name and return that
    element of the list.
    (A) If existing, append new donation amount to list.
        * complete, function name is find_donor()
    (B) If new, create new list item.
        * complete, function name is add_new_donor()
(4) Thank you function.  If donor exists, prints Thank You letter.
        * complete, function name is thank_you()
(5) Print report function.
        * incomplete

=====================================================================
"""

# creates first list and appends new records.
donor_list = [['Matt Biggers', 500, 300, 100]]
donor_list.append(['Mark Seigle', 500, 10, 50])
donor_list.append(['Ryan Nell', 100, 20, 10])
donor_list.append(['Frank Lu', 300, 85, 25])
donor_list.append(['Ashley Kauffman', 700, 3, 980])

# print (donor_list)


# user can print out unformatted donor list, return to Main Menu.
def print_list():
    ask = input("Would you like to print a donor list? (Y)es or (N)o? > ")
    if ask == 'quit':
        main_menu()
    if ask == 'y' or ask == 'Y':
        print (donor_list)
        print ("Returning to the Main Menu.")
        main_menu()
    if ask == 'n' or ask == 'N':
        print ("Thank you. Returning to the Main Menu.")
        main_menu()


def find_donor():
    name = input("Please enter the donor's full name. > ")
    if name == 'quit':
        main_menu()
    # for loop that searches donor list.
    for donor in donor_list:
        # if existing donor, appends amount.
        if name == donor[0]:
            print ("Found donor: " + donor[0])
            # asks for new donation amount and appends it.
            donation = input("What is the new donation amount? > $")
            donor.append(donation)
            print ("The Donor List has been updated.")
            print_list()

    for donor in donor_list:
        # if donor doesn't exist, appends new name and amount to donor list.
        if name != donor[0]:
            print ("New donor name has been added.")
            donation = input("What is the donation amount? > $")
            donor_list.append([name, donation])
            print ("The Donor List has been updated.")
            print_list()


# This function creates a Thank You message.
def thank_you():
    name = input("Please enter the donor's full name. > ")
    if name == 'quit':
        main_menu()
    # for loop that searches donor list.
    for donor in donor_list:
        # if existing donor, prints a Thank You message and returns to Main Menu.
        if donor[0] == name:
            print ("Dear " + name + ", Thank you so much for your generous donation.  The 'American Society for the Oppressed Elites' appreciates your generosity.  These funds will be used to remind the world who is truly in charge.  Viva La Status Quo!")
            main_menu()
    # if donor does not exist, add them to donor database or return to Main Menu
    for donor in donor_list:
        if donor[0] != name:
            print ("That donor does not exist in our database. Would you like to (a)dd this donor to the database?  Or type any other key to return to the Main Menu.")
            p = input("Please type your choice > ")
            if p != 'A' and p != 'a':
                main_menu()
            if p == 'A' or p == 'a':
                find_donor()


# Run a formatted report showing the entire donor list.
def run_report():
    print ("This is a placeholder until the report function is built.  Returning to the Main Menu.")
    main_menu()


# Main Menu that allows users to select their action or quit the program.
def main_menu():
    print ("What would you like to do?")
    print ("(U)pate the donor database?      Create a (T)hank You message?")
    print ("Print a formatted (R)eport?      Print an unformatted donor (list)?")
    print ("(quit) Mailroom Madness?         * you may type (quit) at any time to return to Main Menu.*")
    choice = input(" > ")
    if choice == 'u' or choice == 'U':
        find_donor()
    if choice == 't' or choice == 'T':
        thank_you()
    if choice == 'r' or choice == 'R':
        run_report()
    if choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
        quit()
    if choice == 'list' or choice == 'List' or choice == 'LIST':
        print (donor_list)
        main_menu()
    else:
        print ("Sorry, that is an invalid selection.  Please try again.")
        main_menu()


main_menu()
