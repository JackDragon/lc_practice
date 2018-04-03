## https://leetcode.com/problems/add-two-numbers/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def validateSLL(l):
            if l.val < 10:
                return
            if l.next:
                l.next.val += 1
                l.val = l.val % 10
                validateSLL(l.next)
            else:
                l.next = ListNode(1)
                l.val = l.val % 10
                return
        l1_original = l1
        l2_original = l2
        while True:
            temp_total = l1.val + l2.val
            carryover = temp_total // 10
            mod = temp_total % 10
            # print("MOD: " + str(mod))
            l1.val, l2.val = mod, mod
            if not l1.next:
                if l2.next:
                    l2.next.val += carryover
                    validateSLL(l2.next)
                elif carryover:
                    l2.next = ListNode(carryover)
                return l2_original
            if not l2.next:
                if l1.next:
                    l1.next.val += carryover
                    validateSLL(l1.next)
                elif carryover:
                    l1.next = ListNode(carryover)
                return l1_original
            l1.next.val += carryover
            l1 = l1.next
            l2 = l2.next