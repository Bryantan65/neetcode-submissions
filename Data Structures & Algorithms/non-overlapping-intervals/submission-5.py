class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key = lambda i:i[1])
      
        l=0
        count=0
        prev_end = sorted_intervals[0][1]
        
        for i in sorted_intervals[1:]:
            # print("printing ends", i[0])
            if i[0] < prev_end:
                count+=1
            else:
                prev_end = i[1]
        return count