class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
       
        #intervals end < newinterval start
        #intervals start > newinterval end
        #else overlap and merge
        res = []
        i = 0

        for interval in intervals:
            if interval[1] < newInterval[0]:
                #interval smaller , insert it in
                res.append(interval)
            elif interval[0] > newInterval[1]:
                #interval bigger, how do we insert it though ?
                res.append(newInterval)
                newInterval = interval
            else:
             
                newInterval = [min(interval[0],newInterval[0]) , max(interval[1],newInterval[1])]  
        res.append(newInterval)

        return res