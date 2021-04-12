#6. Write a Python class to find the three elements that sum to zero from a set of n real numbers. Go to the editor
#Input array [-25, -10, -7, -3, 2, 4, 8, 10]
#Output [[-10, 2, 8], [-7, -3, 10]]

class sum3equals0:
    def __init__(self):
        self.arr = [-25, -10, -7, -3, 2, 4, 8, 10]
        self.target = 0

    def findPairs(self):
        nums = []
        for i in self.arr:
            for j in self.arr:
                for k in self.arr:
                    if i+j+k == self.target:
                        triples = [i,j,k]
                        if triples in nums:
                            continue
                        else:
                            nums.append(triples)
        return nums

    def threeSum(self, nums):
        nums = sorted(nums)
        result = []
        i = 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

x = sum3equals0()
print(x.findPairs())
print(x.threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))