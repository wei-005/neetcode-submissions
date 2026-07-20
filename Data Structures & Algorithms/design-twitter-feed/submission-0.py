class Twitter:

    def __init__(self):
        self.time = 0
        self.twitter = defaultdict(list)
        self.followmap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.twitter[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = self.twitter[userId][:]
        for follow in self.followmap[userId]:
            res += self.twitter[follow]

        res.sort(key=lambda x:x[0], reverse=True)

        feed = [tweetId for time, tweetId in res[:10]]

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # if followeeId in self.follow[followerId]:
        #     self.follow[followerId].remove(followeeId)
        self.followmap[followerId].discard(followeeId)
