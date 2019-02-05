'''
  Task:
    Given a base-10 integer, n, convert it to binary (base-2).
    Then find and print the base-10 integer denoting the maximum number
    of consecutive 1's in n's binary representation.
'''

# Solution
if __name__ == '__main__':
  n = int(input('Enter a number: '))
  print('➡ ',
    max(
      len(length)
        for length in str(
          "{0:b}".format(n)
        )
        .split('0')
    )
  )
