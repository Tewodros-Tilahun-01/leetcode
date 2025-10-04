class UndergroundSystem:

    def __init__(self):
        self.start = {}
        self.total = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id] = {"start":stationName ,"time":t}

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        info = self.start[id]
        key = info["start"] + stationName + stationName +info["start"]
        total , count = self.total.get(key,(0,0))
        total += (t - info["time"])
        count += 1
        self.total[key] = (total,count)
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total ,count = self.total[startStation+endStation+endStation+startStation]
        return total / count
        
            

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)