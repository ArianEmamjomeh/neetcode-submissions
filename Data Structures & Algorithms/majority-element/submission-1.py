class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictd = {}
        for num in nums:
            if num not in dictd:
                dictd[num] = 1
            else: 
                dictd[num] += 1
        
        majority = max(dictd, key=dictd.get)
        return majority