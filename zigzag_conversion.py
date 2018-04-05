def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        """
        0   4   8           i(2n-2)
        1 3 5 7 9           i(2n-2)+1, (i+1)(2n-2)-1
        2   6   10          i(2n-2)+n
        -> 1 5 11 2 4 6 8 10 3 7 9
        0     6     12      i(2n-2)                         iC+r+1
        1   5 7   1113      i(2n-2)+1, (i+1)(2n-2)-1           iC+r+1
        2 4   8 10  14      i(2n-2)+2, (i+1)(2n-2)-2
        3     9     15      i(2n-2)+n
        """
        rows = [[] for _ in range(numRows)]
        for n in range(numRows):
            C = (2*numRows - 2)
            i = 0
            while True:
                total = i*C+n
                if total >= len(s):
                    break
                rows[n].append(s[total])
                if n not in [0, numRows-1]:
                    total = (i+1)*C-n
                    if total >= 0 and total < len(s):
                        rows[n].append(s[total])
                i += 1
        return "".join("".join(row) for row in rows)

convert("PAYPALISHIRING", 3)