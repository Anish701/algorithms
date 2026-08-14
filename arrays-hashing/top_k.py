from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can first create a dict of number -> frequency
        # then we traverse the dict and find frequency index in array and append key to it
        
        # array where each index represents frequency 
        # and the value is the numbers having that frequency
        # then you just traverse that array reverse order until you get k most frequent

        mp = {}

        for n in nums:
            mp[n] = mp.get(n, 0) + 1
        
        arr = [[] for _ in range(len(nums) + 1)]

        for key, val in mp.items():
            arr[val].append(key)

        res = []
        for lst in reversed(arr):
            res.extend(lst)
            if len(res) >= k:
                return res