# Leetcode Problem 206 - Reverse a Linked List
# Sener Topaloglu

# 1 -> 2 -> 3 -> 4 -> 5 -> becomes:
# <- 1 <- 2 <- 3 <- 4 <- 5 where 5 is new head

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
  
class Solution:  
  def reverseList(self, head):
    prev = None
    while head:
      temp = head
      head = head.next
      
      temp.next = prev
      prev = temp
    return prev
 
def traverseList(head):
  temp = head
  while temp:
    print(temp.val)
    temp = temp.next
    
node1 = ListNode(1)

node2 = ListNode(2)
node1.next = node2

node3 = ListNode(3)
node2.next = node3

node4 = ListNode(4)
node3.next = node4

node5 = ListNode(5)
node4.next = node5

print("Input: ")
traverseList(node1)

print("Output: ")
result_head = Solution().reverseList(head=node1)
traverseList(result_head)
