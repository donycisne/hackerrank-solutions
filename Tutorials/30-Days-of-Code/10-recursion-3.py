'''
  Task:
    Write a factorial function that takes a positive integer, N as a parameter
    and prints the result of ( factorial).
'''

# Solution
def factorial(n):
  return 1 if n <= 1 else n * factorial(n-1)

if __name__ == '__main__':
  n = int(input('Factorial of the number: '))
  result = factorial(n)
  print(f'➡ {result}')
