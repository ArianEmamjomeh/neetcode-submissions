class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        majority = 1
        for num in nums:
            if counter == 0:
                majority = num
                counter += 1
            if num == majority:
                counter += 1
            else:
                counter -= 1
        return majority
                

