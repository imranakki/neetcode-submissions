import heapq
from collections import defaultdict, deque
from sortedcontainers import SortedList
class Twitter:

    def __init__(self):
        self.feed = defaultdict(deque)
        self.time = 0
        self.followee = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.followee[userId].add(userId)
        tweet = (self.time, tweetId)
        if len(self.feed[userId]) == 10:
            self.feed[userId].popleft()

        self.feed[userId].append(tweet)

        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        ans =  []
        for u in self.followee[userId]:
            ans.extend(list(self.feed[u]))

        ans.sort(reverse=True)
        return [e[1] for e in ans[:min(len(ans), 10)]]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        try:
            self.followee[followerId].remove(followeeId)
        except:
            return