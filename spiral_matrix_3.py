class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        output = []
        counter, s_l, next_check, direction, x, y, TOTAL = 0, 1, False, 0, c0, r0, R*C
        while counter < TOTAL:
            if 0 <= x < C and 0 <= y < R:
                output.append([y, x])
                counter += 1
            if next_check:
                if direction == 3:
                    s_l += 1
                direction = (direction+1) % 4
            if direction == 0:
                x+=1
                next_check = (x+1)-c0 > s_l
            elif direction == 3:
                y-=1
                next_check = r0-(y-1) > s_l
            elif direction == 2:
                x-=1
                next_check = c0-(x-1) > s_l
            else:
                y+=1
                next_check = (y+1)-r0 > s_l
            # if 0 <= x < C and 0 <= y < R:
            #     output.append([x, y])
            #     counter += 1
            #     print("append {},{}".format(x,y) )
            #     if (counter > 3):
            #         print(output)
            # else:
            #     print("{}: no append {},{}".format(s_l,x,y), 0 <= x < C, 0 <= y < R )
            # print(x,y, next_check)
        return output