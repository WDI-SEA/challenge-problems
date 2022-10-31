class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        strlist=[i for a,i in enumerate(coordinates)]
        for i in range(len(strlist)):
            if strlist[i] == "a" or strlist[i] == "c" or strlist[i] == "e" or strlist[i] == "g":
                if int(strlist[1])%2==0:
                    return True
                else:
                    return False
            else:
                if int(strlist[1])%2==1:
                    return True
                else:
                    return False
