"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)
        l =0
        r =0
        maximum = 0
        count = 0

        print(start,end)
        while l < len(start):
            if start[l] >= end[r]:
                count-=1
                r+=1
            else:
                count+=1
                maximum = max(maximum,count)
                l+=1
            
        return maximum

