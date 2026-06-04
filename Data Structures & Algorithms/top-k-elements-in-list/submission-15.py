class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictd = {}
        final = []
        for num in nums:
            if num in dictd:
                dictd[num] += 1
            else:
                dictd[num] = 1
        for i in range(k):
            key = max(dictd, key=dictd.get)
            del dictd[key]
            final.append(key)
        return final
        