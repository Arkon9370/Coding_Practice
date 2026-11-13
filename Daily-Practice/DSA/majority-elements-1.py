# Brute Force (DOUBLE LOOPS)
# class Solution:
#     def majorityElement(self, nums):
#         n = len(nums)
#         threshold = n//2
#         for num in nums:
#             freq = 0
#             for i in nums:
#                 if num == i:
#                     freq = freq + 1
#             if freq > threshold:
#                 return num
#         return -1

# Better Approach (HASH MAPS)
# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         threshold = len(nums)//2
#         freq: dict[int,int] = {}
#         for num in nums:
#             # freq[num] = freq.get(num, 0) + 1
#             if num not in freq:
#                 freq[num] = 1
#             else:
#                 freq[num] = freq[num] + 1
#             if freq[num] > threshold:
#                 return num
#         return -1

# Optimal Apporach (Boyer-Moore Voting)
class Solution:
    def majorityElement(self, nums:list[int]) -> int:
        # threshold = len(nums)//2
        candidate = 0
        balance = 0
        for num in nums:
            if balance == 0:
                candidate = num
            if num == candidate:
                balance += 1
            else:
                balance -= 1
        return candidate

# Driver code
def main() -> None:
    nums: list[int] = [2, 1, 1]
 
    # instance for class Solution
    sol: Solution = Solution()
 
    print(sol.majorityElement(nums))
 
 
# Run the driver when this file is executed directly.
if __name__ == "__main__":
    main()