"""
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

 

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation: 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
Example 2:

Input: nums = [21,21]
Output: 64
Example 3:

Input: nums = [1,2,3,4,5]
Output: 0
 

Constraints:

1 <= nums.length <= 104
1 <= nums[i] <= 105
"""


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            divisior = []
            for j in range(1,nums[i]):
                if nums[i] % j == 0:
                    divisior.append(j)
            divisior.append(nums[i])
            if len(divisior) == 4:
                res.extend(divisior)

        return sum(res)

from math import isqrt
from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        
        for n in nums:
            divisors = set()
            
            for j in range(1, isqrt(n) + 1):
                if n % j == 0:
                    divisors.add(j)
                    divisors.add(n // j)
                
                if len(divisors) > 4:
                    break
            
            if len(divisors) == 4:
                total += sum(divisors)
        
        return total