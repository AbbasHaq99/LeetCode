class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lenNums = len(nums) - 1
        
        l = 0
        r = lenNums

        if nums[l] == target:
            return l
        if nums[r] == target:
            return r

        while l <= r:
            
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1

        return -1                