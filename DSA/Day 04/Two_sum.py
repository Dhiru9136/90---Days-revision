# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# nums = [2,7,11,15]
class Solution(object):
    def two_sum(self, nums, target):
        for i in nums:
            for j in nums:
                if i + j == target:
                    return nums.index(i),nums.index(j)

obj=Solution()
print(obj.two_sum([2,7,11,15],9))