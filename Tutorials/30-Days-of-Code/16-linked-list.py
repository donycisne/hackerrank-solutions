'''
Task:
  Complete the insert function in your editor so that it creates a new Node
  (pass data as the Node constructor argument) and inserts it at the tail
  of the linked list referenced by the head parameter.
  Once the new node is added, return the reference to the head node.
Note:
  If the head argument passed to the insert function is null,
  then the initial list is empty.
'''

# Solution:
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class Solution:
  def display(self,head):
    current = head
    print('|=== Display ===|'),
    while current:
      print(current.data,end=' ')
      current = current.next
    print('')

  def insert(self,head,data):
  #Complete this method
    if (head == None):
      head = Node(data)
    elif (head.next == None):
      head.next = Node(data)
    else:
      self.insert(head.next, data)
    return head

mylist= Solution()
T=int(input('Enter a number: '))
head=None
for i in range(T):
  data=int(input('Enter another number: '))
  head=mylist.insert(head,data)
mylist.display(head);
