'''
Task:
  Given an array, a, of size n distinct elements, sort the array
  in ascending order using the Bubble Sort algorithm above.
  Once sorted, print the following 3 lines:
  1 - Array is sorted in numSwaps swaps.
      where numSwaps is the number of swaps that took place.
  2 - First Element: firstElement
      where firstElement is the first element in the sorted array.
  3 - Last Element: lastElement
      where lastElement is the last element in the sorted array.
Hint:
  To complete this challenge, you will need to add a variable that keeps
  a running tally of all swaps that occur during execution.
'''

# Solution
n = int(input('Enter the number of swaps: ').strip())
a = list(map(int, input('Enter the numbers separate by one space: ').strip().split(' ')))

swaps = 0

while True:
  for i in range(n - 1):
    if  a[i] > a[i + 1]:
      a[i], a[i + 1] = a[i + 1], a[i]
      swaps += 1
      break
  else:
      break

print(f'➡ Array is sorted in {swaps} swaps.')
print('➡ First Element:', a[0])
print('➡ Last Element:', a[-1])
