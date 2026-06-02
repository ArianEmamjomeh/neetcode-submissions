class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
    
        items = list(freq.items())

        items.sort(key=lambda pair: pair[1], reverse=True)


        result = []
        for i in range(k):
            result.append(items[i][0])

        return result








        