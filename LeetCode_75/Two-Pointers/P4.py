'''
Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array
whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the 
array
'''


n = int(input("Enter the length of nums:-"))
nums = []
k = int(input("Enter the integer:-")) 

for i in range(n):
    value = int(input("Enter the value for nums:-"))
    nums.append(value)
print("Array nums is", nums)

count = 0

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == k:
            count += 1
print("Maximum operations possible = ", count)

'''
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        count = 0

        while True:

            found = False

            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):

                    if nums[i] + nums[j] == k:

                        nums.pop(j)
                        nums.pop(i)

                        count += 1
                        found = True
                        break

                if found:
                    break

            if not found:
                break

        return count
        '''

'''
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        freq = {}
        count = 0

        for num in nums:

            complement = k - num

            if complement in freq and freq[complement] > 0:

                count += 1
                freq[complement] -= 1

            else:

                if num not in freq:
                    freq[num] = 0

                freq[num] += 1

        return count
        '''


































































































































































































































































































