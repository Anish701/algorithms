import heapq
from typing import List
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userId -> [[tweetId, count]]
        self.followerMap = defaultdict(set) # userId -> (followee1, followee2)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([tweetId, self.count])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.followerMap[userId]
        followees.add(userId)
        
        minHeap = []
        res = []

        for followee in followees:
            tweets = self.tweetMap[followee]
            index = len(tweets) - 1

            if index >= 0:
                tweetId, count = tweets[index]
                heapq.heappush(minHeap, [count, followee, tweetId, index - 1])

        while len(res) < 10 and minHeap:
            count, followee, tweetId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                tweets = self.tweetMap[followee]
                tweetId, count = tweets[index]
                heapq.heappush(minHeap, [count, followee, tweetId, index - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)
