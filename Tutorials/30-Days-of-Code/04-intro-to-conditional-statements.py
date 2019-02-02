'''
  Task:
    Given an integer, n, perform the following conditional actions:
    - If n is odd, print Weird
    - If n is even and in the inclusive range of 2 to 5, print Not Weird
    - If n is even and in the inclusive range of 6 to 20, print Weird
    - If n is even and greater than 20, print Not Weird
'''

# Solution
N = int(input('Enter a number: '))

if (N % 2 == 1) or (N > 5 and N < 21):
 print("➡ Weird 🙃")
else:
  print("➡ Not Weird 🙂")
