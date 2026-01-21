"""
1. Two Sum
input:
nums = [2,7,11,15]
target = 9
output : [0,1]
"""
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        len_n = len(nums)

        for i in range(len_n):
            for j in range(i+1,len_n):

                if nums[i] + nums[j] == target:

                    return [i,j]
                
if __name__ == "__main__":

    nums = [2,7,11,15]
    target = 9

    cls_obj = Solution()
    res = cls_obj.twoSum(nums,target)
    print(res)