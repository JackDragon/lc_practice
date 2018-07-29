# import math
class Solution:
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        # how many numbers are in A*B
        # counter = 0
        # for i in range(min(A,B),A*B+1):
        #     if i % A == 0 or i % B == 0:
        #         counter += 1
        #         if counter == N:
        #             return i
        n_common = self.nCommonFactors(A, B)
        # if A%B == 0:
        #     counter = A
        # elif B%A == 0:
        #     counter = B
        # else:
        #     counter = A+B-math.factorial(n_common)
        counter = A+B-n_common
        n_AB = N // counter
        ret_val = n_AB * A * B
        # print(n_AB, ret_val, counter)
        counter = counter * n_AB
        # print("counter2", counter)
        while counter < N:
            ret_val += 1
            if ret_val % A == 0 or ret_val % B == 0:
                counter += 1
        return ret_val%1000000007

    def nCommonFactors(self, a, b):
        counter = 0
        for i in range(2, min(a, b) + 1):
            if a % i == b % i == 0:
                print(a, b, i, (a * b) // i - 1)
                counter += (a*b)//i-1
        return counter
sol = Solution()

print(sol.nCommonFactors(33333, 34919))
print(sol.nCommonFactors(4, 6))
print(sol.nCommonFactors(4, 8))
# 4, 8, 12, 16, 20, 24, 28, 32 = 8 = 32/4 + 32/8 - 4 = 8
# 4, 6, 8, 12, 16, 18, 20, 24 = 8 = 24/4 + 24/6 - 2
# 3, 6, 8, 9, 12, 15, 16, 18, 21, 24 = 10 = 24/3 + 24/8 - 1
print(sol.nthMagicalNumber(1, 2, 3), 2)
print(sol.nthMagicalNumber(4, 2, 3), 6)
print(sol.nthMagicalNumber(5, 2, 4), 10) # 2, 4, 6, 8
print(sol.nthMagicalNumber(3, 6, 4), 8)
#print(sol.nthMagicalNumber(99999999, 33333, 34919))