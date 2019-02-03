'''
  Task:
    Given an array, A, of N integers, print A's elements in reverse order
    as a single line of space-separated numbers.
'''

# Solution
if __name__ == '__main__':
  n = int(input("Enter how many numbers you want to enter: "))
  arr = list(map(
          int, input('Enter the numbers separated by a space: ')
          .rstrip()
          .split()
          )
        )

  print('➡', *arr[::-1])
