class RecentCounter:
    def __init__(self):
        self.requests = []
    def ping(self, t: int) -> int:
        self.counter = 0
        self.requests.append(t)
        i = 0
        while self.requests[i] < t-3000: 
            self.requests.pop(i)
        self.requests = self.requests[::-1]
        while self.requests[i] > t:
            self.requests.pop(i)
        self.requests = self.requests[::-1]
        return len(self.requests)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)