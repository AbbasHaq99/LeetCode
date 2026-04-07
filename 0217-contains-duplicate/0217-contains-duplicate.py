class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        duoMap = {}

        for n in nums:
            if n not in duoMap:
                duoMap[n] = 1
            elif n in duoMap:
                return True

        return False
