class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        change_nums = []
        if k == 0:
            max_count = 0
            count = 0
            for n in nums:
                if n == 1:
                    count += 1
                    max_count = max(max_count, count)
                else:
                    count = 0
            return max_count
        if k >= nums.count(0):  
            return len(nums)
        for r in nums:
            if r == 0:
                change_nums += [1]
            else:
                change_nums += [0]
        i = 0
        r = 0
        a = 0 
        b = 0
        while r < len(nums):
            a += change_nums[r]
            while a > k:         
                a -= change_nums[i]
                i += 1
            b = max(b, r - i + 1)  
            r += 1
        return b
