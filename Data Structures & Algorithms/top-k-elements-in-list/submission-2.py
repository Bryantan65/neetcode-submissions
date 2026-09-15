class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        res = []

        #loop through capture the count of it
        for n in nums:
            counter[n] = counter.get(n,0) +1

        #return it by another for loop?
        for i in range(k):
            best = max(counter, key=counter.get)
            res.append(best)
            del counter[best]
        return res