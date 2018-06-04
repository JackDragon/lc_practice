# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return
        p1 = p2 = head
        while p1.next and p2.next:
            p2 = p2.next
            if p2.next == p1.next:
                return p1
            if not p2.next:
                return
            p2 = p2.next
            if p2.next == p1.next:
                return p1
            p1 = p1.next
            if p2.next == p1.next:
                return p1
        return

solution = Solution()

n1, n2, n3, n4 = ListNode(1),ListNode(2),ListNode(3),ListNode(1)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = None
print(solution.detectCycle(n1))
