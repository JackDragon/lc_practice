class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        stops = set()
        dominoes = list(dominoes)
        for i in range(len(dominoes)):
            if dominoes[i] == "R":
                a = i+1
                found = 0
                while a < len(dominoes):
                    if dominoes[a] == "L":
                        found = a
                        break
                    elif dominoes[a] == "R":
                        # found = a
                        break
                    a+=1
                if found and (found + i)%2 == 0:
                    # print("Found:", found+i)
                    if dominoes[(found+i)//2] == ".":
                        dominoes[(found+i)//2] = "x"
                elif found:
                    stops.add((found+i)//2)
                    stops.add((found+i+1)//2)
        # print(dominoes)
        # print(stops)
        for i in range(len(dominoes)):
            if i in stops:
                continue
            if dominoes[i] == "L":
                a = i-1
                while a >= 0:
                    if dominoes[a] == ".":
                        dominoes[a] = "L"
                    else:
                        break
                    if a in stops:
                        break
                    a-=1
            elif dominoes[i] == "R":
                a = i+1
                while a < len(dominoes):
                    if dominoes[a] == ".":
                        dominoes[a] = "R"
                    else:
                        break
                    if a in stops:
                        break
                    a+=1
        return "".join(dominoes).replace("x", ".")