# Name: Jacob Newby
# Date: 11/7/2022
# Description: The program decides if the student has made the Dean's list or Honor Roll

# Ask user to enter student last name
lastname = input("Enter Student Last Name: ")

# Check if last name entered is 'ZZZ' or not
while lastname != "ZZZ":
    # Ask user to enter student first name
    firstname = input("Enter Student First Name: ")
    # Ask user to enter student gpa
    gpa = float(input("Enter Student GPA: "))
    # Check if student gpa is 3.5 or more
    if gpa >= 3.5:
        print("{} {} has made the Dean's List.".format(firstname, lastname))
    # Check if student gpa is 3.25 or more
    else:
        if gpa >= 3.25:
            print("{} {} has made the Honor Roll.".format(firstname, lastname))
    lastname = input("\nEnter Student Last Name: ")
    # This will repeat until 'ZZZ' is entered