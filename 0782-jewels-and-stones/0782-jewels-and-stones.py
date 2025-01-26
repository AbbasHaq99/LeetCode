class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        #.count returns once, for loop it to make sure it returns multipul times
        return sum(stones.count(j) for j in jewels)