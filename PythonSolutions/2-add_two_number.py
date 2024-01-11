""" 
2. Add Two Numbers
"""



from typing import Optional

class ListNode: 
    """ Linkedlist """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        booln = ListNode(0)
        curr = booln
        a = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            sum1 = a + x + y
            a = sum1//10
            curr.next = ListNode(sum1 % 10)
            curr = curr.next

            if l1:
               l1 = l1.next
            if l2:
                l2 = l2.next

        if a > 0:
            curr.next = ListNode(a)

        return booln.next
    
def main():
    # TestCase
    # 342 + 465 = 807
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    while result: #print the terminal
        print(result.val, end=" ")
        result = result.next
    print()

if __name__ == "__main__": # run code
    main()