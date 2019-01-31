'''
Task:
  Complete the code in the editor below. The variables i, d, and s
  are already declared and initialized for you. You must:
  1 - Declare 3 variables: one of type int, one of type double, and one of type String.
  2 - Read 3 lines of input from stdin (according to the sequence
      given in the Input Format section below) and initialize your 3 variables.
  3 - Use the + operator to perform the following operations:
    a - Print the sum of i plus your int variable on a new line.
    b - Print the sum of d plus your double variable to a scale of one decimal place on a new line.
    c - Concatenate s with the string you read as input and print the result on a new line.
'''

# Solution
i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
int_2 = input('Enter an integer number: ')
double_2 = input('Enter a decimal number: ')
string_2 = input('Enter a cool word: ')
# Read and save an integer, double, and String to your variables.
i_2 = int(int_2)
d_2 = float(double_2)
s_2 = string_2
# Print the sum of both integer variables on a new line.
print(f'➡ {i + i_2}')
# Print the sum of the double variables on a new line.
print(f'➡ {d + d_2}')
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(f'➡ {s + s_2}')
