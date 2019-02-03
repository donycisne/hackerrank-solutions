'''
  Task:
    Given n names and phone numbers, assemble a phone book that maps
    friends' names to their respective phone numbers.
    You will then be given an unknown number of names to query your phone book for.
    For each name queried, print the associated entry from your phone book
    on a new line in the form name=phoneNumber; if an entry for is not found,
    print Not found instead.
'''

# Solution
n = int(input("How many names do you want to enter?: "))
phone_book = dict(input("- Set [name number] ➡ ").split() for _ in range(n))
while n > 0:
  try:
    name = input("Enter a name to show the number: ")
    if name in phone_book:
      print(f"{n-1} attempts left ➡ {name}={phone_book[name]}")
      n-=1
    else:
      print(f"{(n-1)} attempts left ➡ Not found")
      n-=1
  except:
    pass
