"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        for i in range(1,len(starts)):
            if starts[i] < ends[i-1]:
                return False
        return True
        
        
