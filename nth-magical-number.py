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
        # n_common = self.nCommonFactors(A, B)
        # if A%B == 0:
        #     counter = A
        # elif B%A == 0:
        #     counter = B
        # else:
        #     counter = A+B-math.factorial(n_common)
        lcm = self.lcm(A,B)
        counter = lcm//A+lcm//B-1
        n_AB = N // counter
        ret_val = n_AB * lcm
        # print(N, A, B)
        # print(lcm, counter, n_AB, ret_val)
        counter = counter * n_AB
        # print(N, counter)
        # N = N%counter
        n_a = 0
        n_b = 0
        # print(lcm, n_AB, ret_val, counter, N)
        while counter < N:
            if n_a * A == n_b * B:
                n_a += 1
                n_b += 1
            elif n_a * A < n_b * B:
                n_a += 1
            else:
                n_b += 1
            counter += 1
        return (ret_val+min(n_a*A, n_b*B))%1000000007

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def lcm(self, a, b):
        return (a * b) // self.gcd(a, b)

sol = Solution()

# print(sol.nCommonFactors(33333, 34919))
# print(sol.nCommonFactors(4, 6))
# print(sol.nCommonFactors(4, 8))
# 4, 8, 12, 16, 20, 24, 28, 32 = 8 = 32/4 + 32/8 - 4 = 8
# 4, 6, 8, 12, 16, 18, 20, 24 = 8 = 24/4 + 24/6 - 2
# 3, 6, 8, 9, 12, 15, 16, 18, 21, 24 = 10 = 24/3 + 24/8 - 1

print(sol.nthMagicalNumber(1, 2, 3), 2)
print(sol.nthMagicalNumber(4, 2, 3), 6)
print(sol.nthMagicalNumber(5, 2, 4), 10) # 2, 4, 6, 8
print(sol.nthMagicalNumber(3, 6, 4), 8)
# a, b, l = 39999, 40000, sol.lcm(39999, 40000)
# print(sol.lcm(39999, 40000), l/a+l/b-1)
print(sol.nthMagicalNumber(1000000000, 39999, 40000), 499900006)
# print(sol.nthMagicalNumber(99999999, 33333, 34919))