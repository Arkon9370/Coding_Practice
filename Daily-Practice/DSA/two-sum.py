# brute force solution
# class Solution:
#     def twoSum(self, nums, target):
#         answer_list = []
#         length = len(nums)
#         for i in range(length):
#             for j in range(i,length):
#                 if nums[i] + nums[j] == target:
#                     answer_list = [i,j]
#         return answer_list
# Better solution
# class Solution:
#     def twoSum(self, nums, target):
#         length = len(nums)
#         if length < 2:
#             return []
#         pairs = [(nums[i],i) for i in range(length)]
#         pairs.sort()
#         left = 0
#         right = length - 1
#         while left < right:
#             current_sum = pairs[left][0] + pairs[right][0]
#             if current_sum == target:
#                 return [pairs[left][1], pairs[right][1]]
#             if current_sum > target:
#                 right -= 1
#             else:
#                 left += 1 
#         return []
# Optimal Solution
class Solution:
    def twoSum(self, nums, target):
        length = len(nums)
        if length<2:
            return []
        value_index = {}
        for i in range(length):
            complement = target - nums[i]
            if complement in value_index:
                return[value_index[complement],i]
            value_index[nums[i]] = i
        return []
if __name__ == "__main__":
    nums = [1, 6, 2, 10, 3]
    target = 7
 
    solution = Solution()
    answer = solution.twoSum(nums, target)
 
    print(*answer)        