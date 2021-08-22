class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.curr_sum = 0
        self.db_of_300_hits = collections.deque([])

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.db_of_300_hits.append(timestamp)
        self.curr_sum += 1
        
        self.update(timestamp)
    
    def update(self, timestamp : int):
        """
        Updates DB and curr_sum
        """
        
        while self.db_of_300_hits and timestamp - self.db_of_300_hits[0] > 299:
            self.db_of_300_hits.popleft()
            self.curr_sum -= 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        
        self.update(timestamp)
    
        return self.curr_sum


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)