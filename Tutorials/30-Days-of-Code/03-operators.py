'''
Task:
  Given the meal price (base cost of a meal),
  tip percent (the percentage of the meal price being added as tip),
  and tax percent (the percentage of the meal price being added as tax) for a meal,
  find and print the meal's total cost.
'''

# Solution
def solve(meal_cost, tip_percent, tax_percent):
  tip_amount = meal_cost * tip_percent / 100
  tax_amount = meal_cost * tax_percent / 100
  total_cost = round(meal_cost + tip_amount + tax_amount)
  print(f'➡ Total Cost: {total_cost}')

if __name__ == '__main__':
  meal_cost = float(input('Enter a meal cost: '))
  tip_percent = int(input('Enter a tip percent: '))
  tax_percent = int(input('Enter a tax percent: '))
  solve(meal_cost, tip_percent, tax_percent)
