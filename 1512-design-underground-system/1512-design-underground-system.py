class UndergroundSystem:

    def __init__(self):
        self.start = {}
        self.averages = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id] = {"start":stationName ,"time":t}

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        info = self.start[id]
        key = info["start"] + stationName + stationName +info["start"]
        self.averages[key].append(t-info["time"])
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        arr = self.averages[startStation+endStation+endStation+startStation]
        n = len(arr)
        total = 0
        for i in range(n):
            total += arr[i]
        return total / n
            

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)