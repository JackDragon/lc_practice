class AB:
    def createString(self, N, K):
        num_a = N//2
        num_b = N-num_a
        if K > N//2*(N-N//2):
            return ""
        # Num of b's after a's
        counter = K//num_a
        leftover = K%num_a
        prefix = (num_b-counter-1)*"B"+leftover*"A"+"B" if counter < num_b else ""
        # print("num_a", num_a, "num_b", num_b, "counter", counter, "leftover", leftover)
        # print((num_b-counter-1),leftover,1,(num_a-leftover),counter)
        return prefix+(num_a-leftover)*"A"+counter*"B"
        # ret_val = (num_b-counter-1)*"B" if ((num_b-counter-1)>0) else ""
        # print("ret_val", ret_val)
        # return ret_val + leftover*"A"+"B"+(num_a-leftover)*"A"+counter*"B"

sol = AB()

print(sol.createString(3, 2))
print(sol.createString(2, 0))
print(sol.createString(5, 8))
print(sol.createString(10, 12))
print(sol.createString(2, 1))