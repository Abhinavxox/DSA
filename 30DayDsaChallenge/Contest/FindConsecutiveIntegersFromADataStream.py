class DataStream(object):
    
    def __init__(self, value, k):
        self.value = value
        self.k = k
        self.stream = []
        self.count = 0

    def consec(self, num):
        self.stream.append(num)
        if num == self.value:
            self.count += 1
        else:
            self.count = 0
        return self.count >= self.k
        
