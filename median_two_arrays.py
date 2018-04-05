class Solution(object):
    def nth(self, a, b, n):
        if not a or not b:
            return (a+b)[n]
        ai = len(a) >> 1
        bi = len(b) >> 1
        med_a = a[ai]
        med_b = b[bi]
        if ai + bi >= n:
            if med_a <= med_b:
                return self.nth(a, b[:bi], n)
            else:
                return self.nth(a[:ai], b, n)
        else:
            if med_a <= med_b:
                return self.nth(a[ai +1:], b, n-ai-1)
            else:
                return self.nth(a, b[bi+1:], n-bi-1)
                
    def findMedianSortedArrays(self, A, B):
        total_len = len(A) + len(B)
        if total_len % 2 == 0:
            return (self.nth(A, B, total_len >> 1) + self.nth(A, B, (total_len>>1)-1)) * 0.5
        else:
            return self.nth(A, B, total_len >> 1)