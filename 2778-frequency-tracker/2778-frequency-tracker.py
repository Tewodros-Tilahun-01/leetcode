class FrequencyTracker:
    def __init__(self):
        self.num_count = {}
        self.freq_count = {}
        
    def add(self, number: int) -> None:
        count = self.num_count.get(number, 0)
        if count > 0:
            self.freq_count[count] = self.freq_count.get(count, 0) - 1
            if self.freq_count[count] == 0:
                del self.freq_count[count]
        self.num_count[number] = count + 1
        self.freq_count[count + 1] = self.freq_count.get(count + 1, 0) + 1
        
    def deleteOne(self, number: int) -> None:
        if number not in self.num_count:
            return
        count = self.num_count[number]
        self.freq_count[count] = self.freq_count[count] - 1
        if self.freq_count[count] == 0:
            del self.freq_count[count]
        if count == 1:
            del self.num_count[number]
        else:
            self.num_count[number] = count - 1
            self.freq_count[count - 1] = self.freq_count.get(count - 1, 0) + 1
        
    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq_count and self.freq_count[frequency] > 0