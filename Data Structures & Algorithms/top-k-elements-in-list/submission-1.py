class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        result=[]
        for i in nums:
            hashmap[i] = hashmap.get(i, 0)+1
        sorted_items = sorted(hashmap.items(), key=lambda x:x[1], reverse=True)
        for i in range(k):
            print(result.append(sorted_items[i][0]))
        return result