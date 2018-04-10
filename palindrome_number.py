import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # x = -x if x < 0 else x
        if x < 0:
            return False
        elif x < 10:
            return True
        # length = len(x)
        # if len(x) < 2:
        #     return True
        # for i in range(length >> 1):
        #     if x[i] != x[length-1-i]:
        #         return False
        # return True
        counter = int(math.log(x, 10))
        while x > 99:
            if x // 10 ** counter != x % 10:
                return False
            # print("Counter", counter)
            x -= 10 ** counter * (x // 10 ** counter)
            # print("x1",x)
            x = x//10
            # print("x2",x)
            # print(x, 10 **(counter+1)-1-x)
            counter -= 2
            x = max(x, 10 **(counter+1)-1-x)
            # print(x)
        if x > 9:
            return x // 10 == x % 10
        return True