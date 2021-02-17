#! python3

"""
Count by 2's and display all the numbers, 1 on each line.
Continue until the current value is 20
(2 marks)
Inputs:
none

Outputs:
Example:
2
4
6
8
10
...
"""
x = 1
while x <= 20:
    x += 1
    if x%2 == 0:
        print(x)