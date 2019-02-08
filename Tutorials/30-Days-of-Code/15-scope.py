'''
Task:
  Complete the Difference class by writing the following:
  - A class constructor that takes an array of integers as a parameter
    and saves it to the elements instance variable.
  - A computeDifference method that finds the maximum absolute difference between
    any 2 numbers in N and stores it in the maximumDifference instance variable.
'''

# Solution
class Difference:
  def __init__(self, a):
    self.__elements = a

	# Add your code here
  def computeDifference(self):
    self.maximumDifference=max(a)-min(a)

# End of Difference class
_ = input('Enter a number: ')
a = [int(e) for e in input('Enter numbers separated with one space: ').split(' ')]

d = Difference(a)
d.computeDifference()

print('➡', d.maximumDifference)
