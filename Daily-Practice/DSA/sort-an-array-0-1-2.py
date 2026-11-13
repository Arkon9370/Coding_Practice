# Brute force (using in-built sort funciton)
# class Solutions:
#     def setZeroOneTwo(self, nums: list[int]) -> None:
#         # sorts the list in numeric ascending order
#         nums.sort()
#         return 

# Optimal Approach 1 (counting all the 0's, 1's and 2's then changing the list)
# class Solutions:
#     def setZeroOneTwo(self, nums: list[int]) -> None:
#         zero_count = 0
#         one_count = 0
#         two_count = 0 
#         for num in nums:
#             if num == 0:
#                 zero_count += 1
#             elif num == 1:
#                 one_count += 1
#             else:
#                 two_count += 1
#         index = 0
#         # # Write all zeroes first.
#         # for _ in range(zero_count):
#         #     nums[index] = 0
#         #     index += 1
 
#         # # Write all ones after the zeroes.
#         # for _ in range(one_count):
#         #     nums[index] = 1
#         #     index += 1
 
#         # # Write all twos at the end.
#         # for _ in range(two_count):
#         #     nums[index] = 2
#         #     index += 1
 
#         for i in range(zero_count+one_count+two_count):
#             if zero_count > 0:
#                 nums[index] = 0
#                 index += 1
#                 zero_count -= 1
#             elif one_count > 0:
#                 nums[index] = 1
#                 index += 1
#                 one_count -= 1
#             elif two_count > 0:
#                 nums[index] = 2
#                 index += 1
#                 two_count -= 1
#             else:
#                 return
#         return

# Optimal Approach 2 (3 pointers left-current-right)
class Solutions:
    def setZeroOneTwo(self, nums:list[int]) -> None:
        left = 0
        current = 0
        right = len(nums)-1
        # move 0 left, leave 1 in the middle and 2 right
        while current <= right:
            if nums[current] ==0:
                nums[current],nums[left] = nums[left], nums[current]
                current += 1
                left += 1
            elif nums[current] ==1:
                current += 1
            else:
                nums[current],nums[right] = nums[right], nums[current]
                right -= 1
        return

def main() -> None:
    nums: list[int] = [2, 0, 2, 1, 1, 0]
    # nums: list[int] = [2, 1, 2, 1, 1, 1]
    sol:Solutions = Solutions()
    sol.setZeroOneTwo(nums)
    print(nums)

if __name__ == "__main__":
    main()