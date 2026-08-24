from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # first attempt (nlogn)
        # posTime = []
        # for i, p in enumerate(position):
        #     time = float(target - p) / speed[i]
        #     posTime.append([p, time])

        # posTime.sort()

        # prevTime = 0
        # res = 0
        # while posTime:
        #     pos, time = posTime.pop()
        #     if time > prevTime:
        #         res += 1
        #         prevTime = time

        # return res

        # second attempt (nlogn but with proper stack use)
        # posTime = [(p, s) for p, s in zip(position, speed)]
        # posTime.sort(reverse=True)
        # stack = []

        # for p, s in posTime:
        #     time = (target - p) / s
        #     stack.append(time)
        #     if len(stack) >= 2 and stack[-1] <= stack[-2]:
        #         stack.pop()
        
        # return len(stack)

        # third attempt (nlogn but this optimizes first attempt)
        posTime = []
        for i, p in enumerate(position):
            time = (target - p) / speed[i]
            posTime.append((p, time))

        posTime.sort(reverse = True)

        res = 0
        prevTime = 0
        for i in range(len(posTime)):
            time = posTime[i][1]
            if time > prevTime:
                res += 1
                prevTime = time

        return res