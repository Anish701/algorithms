from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l = len(board)

        for r in range(l):
            st = set()

            for c in range(l):
                val = board[r][c]
                
                if val == ".":
                    continue
                elif val in st:
                    print('r')
                    return False
                else:
                    st.add(val)

        for c in range(l):
            st = set()

            for r in range(l):
                val = board[r][c]

                if val == ".":
                    continue
                elif val in st:
                    print('c')
                    return False
                else:
                    st.add(val)

        for b in range(l):
            st = set()

            for r in range(l//3):
                for c in range(l//3):
                    val = board[3*(b//3) + r][3*(b%3) + c]

                    if val == ".":
                        continue
                    elif val in st:
                        return False
                    else:
                        st.add(val)

        return True