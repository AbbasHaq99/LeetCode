class Solution:
    def romanToInt(self, s: str) -> int:

        my_nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        #iterate over string while checking pairs of chars
        total = 0

        for i in range(len(s) - 1):
        #the -1 is because the last number
            if my_nums[s[i]] < my_nums[s[i + 1]]:
            #the error looks here
                total -= my_nums[s[i]]
            else:
                total += my_nums[s[i]]
        total +=my_nums[s[-1]]

        return total