class Solution:
    def isValid(self, s: str) -> bool:
        pDict = {')':'(', ']':'[', '}':'{'}
        stk = []

        for c in s:
            if c in pDict:
                if stk and pDict[c] == stk[-1]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        
        if stk:
            return False
        else:
            return True