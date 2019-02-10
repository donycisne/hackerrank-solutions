'''
Task:
  The AdvancedArithmetic interface and the method declaration for the abstract
  divisorSum(n) method are provided for you in the editor below.
  Complete the implementation of Calculator class, which implementsthe
  AdvancedArithmetic interface. The implementation for the divisorSum(n) method
  must return the sum of all divisors of n.
'''
 # Solution
class AdvancedArithmetic(object):
  def divisorSum(self, n):
    raise NotImplementedError

class Calculator(AdvancedArithmetic):
  def divisorSum(self, n):
    x = []
    for i in range(1, n+1):
      if n % i == 0:
        x.append(i)
      else:
        pass
    return sum(x)

n = int(input('Enter a number: '))
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print('➡', s)
