#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""

x = float(input("Enter a number: "))
while x%1 != 0 and x%2 != 0:
    print("That is not an even interger")
    x = float(input("Enter a number: "))
if x%1 == 0 and x%2 == 0:
    print("That is an even integer")