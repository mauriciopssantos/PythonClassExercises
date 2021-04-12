#5. Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
class findPair:
    def __init__(self):
        self.target = 40
        self.x = [5,10,15,20,25,30,50]
    
    def findPairs(self):
        nums = []
        for i in range(len(self.x)):
            for j in range(len(self.x)):
                if self.x[i]+self.x[j] == self.target and not i==j:
                    nums.append((i,j))
        return nums
y = findPair()
print(y.findPairs())