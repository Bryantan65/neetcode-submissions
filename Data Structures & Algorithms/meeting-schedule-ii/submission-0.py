"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)
        l=0
        r=0
        count = 0
        maximum = 0
        
        print(starts,ends)
        while l < len(starts):
            if starts[l] < ends[r]: # if start if less than end , overlap, a room is being used
                print(starts[l], ends[r])
                count+=1
                maximum = max(maximum, count)
                l+=1
            elif starts[l] >= ends[r]:
                count-=1
                maximum = max(maximum, count)
                r+=1
            
        
        return max(maximum, count)