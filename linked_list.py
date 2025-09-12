# given two linked lists, reverse the list and return the summation of the linked lists
# for example: l1 = (3 -> 2 -> 1), l2 = (6 -> 5 -> 4)
# reverse l1 = 123, reverse l2 = 456
# 123 + 456 = 579
# return (9 -> 7 -> 5)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        current = l1
        l1_nums = []
        while current:
            l1_nums.append(current.val)
            current = current.next
        
        current2 = l2
        l2_nums = []
        while current2:
            l2_nums.append(current2.val)
            current2 = current2.next

        l1_reverse = l1_nums[::-1]
        l2_reverse = l2_nums[::-1]

        num1 = int("".join(map(str, l1_reverse)))
        num2 = int("".join(map(str, l2_reverse)))

        total = num1 + num2

        dummy = ListNode(0)
        current = dummy
        for digit in reversed(str(total)):
            current.next = ListNode(int(digit))
            current = current.next 
        
        return dummy.next
