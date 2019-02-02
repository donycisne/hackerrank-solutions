'''
  Task:
   Given an integer, n, print its first 10 multiples.
   Each multiple n * i(where 1 <= i <= 10) should be printed on a new line
   in the form: n x i = result.
'''

# Solution
n = int(input("Enter a number to see its first 10 multiples: "))

for multiple in range(1, 11):
  # My Solution
  print(f"{n} x {multiple} = {n*multiple}")
  # HackerRank Solution
  # print(n, "x", multiples, "=", n*multiples)
  pass
