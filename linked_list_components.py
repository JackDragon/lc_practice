# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        # G = sorted(G)
        # cur_length = 0
        # count = 0
        # for i in G:
        #     counter = 0
        #     # print(i)
        #     while head.val < i and head.next:
        #         head = head.next
        #         counter += 1
        #     if i == head.val and counter < 2:
        #         cur_length += 1
        #     elif i == head.val:
        #         cur_length = 1
        #     else:
        #         cur_length = 0
        #     if cur_length < 2:
        #         count += 1
        #     print("i", i, "head.val", head.val, "cur_length", cur_length, "count", count)
        # return count
        G = set(G)
        count = 0
        cur_length = 0
        total_connected = 0
        while True:
            if head.val in G:
                cur_length += 1
            else:
                if cur_length > 1:
                    total_connected += cur_length
                    count += 1
                cur_length = 0
            # print(head.val, cur_length, count)
            if not head.next:
                if cur_length > 1:
                    total_connected += cur_length
                    count += 1
                # print(count + len(G) - total_connected)
                return count + len(G) - total_connected
            head = head.next
# n1 = ListNode(0)
# n2 = ListNode(2)
# n1.next = n2
# s = Solution()
# print(s.numComponents(n1, [0, 1, 2]))