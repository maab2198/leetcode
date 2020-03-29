class UndergroundSystem:

    def __init__(self):
        self.mem={}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if stationName in self.mem:
            self.mem[stationName][id] = t
        else:
            self.mem[stationName] = {id:t}
            
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if stationName in self.mem:
            self.mem[stationName][id] = t
        else:
            self.mem[stationName] = {id:t}    

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        arr1 = self.mem[startStation]
        arr2 = self.mem[endStation]
        n = len(arr2.keys())
        count = 0
        d = 0
        for key in arr2.keys():
            if key in arr1:
                count +=1
                d += arr2[key] - arr1[key]
        res = d/count if count > 0 else count 
        return res
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)