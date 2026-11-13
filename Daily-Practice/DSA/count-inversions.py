# Brute force solutions (DOUBLE FOR LOOPS)
# class Solution:
#     def numberOfInversions(self, nums:list[int]) -> int:
#         inversions: int = 0
#         length: int = len(nums)
#         for i in range(length):
#             for j in range(i+1, length):
#                 if nums[i]>nums[j]:
#                     inversions +=1
#         return inversions

# Optimal Solution
class Solution:
    # Merges two sorted ranges and returns their cross inversions.
    def _merge_and_count(self, nums:list[int], left:int, mid:int, right:int)->int:
        merged:list[int] = []
        first:int = left
        second:int = mid + 1
        inversions:int = 0
        # combine both sorted halves and count cross inversions
        while first <= mid and second <= right:
            # Choose the left value when it is not greater; otherwise the right value creates cross inversions.
            if nums[first] <= nums[second]:
                merged.append(nums[first])
                first += 1
            else:
                inversions += mid - first +1
                merged.append(nums[second])
                second += 1
        # Copy any values still remaining in the left half.
        while first <= mid:
            merged.append(nums[first])
            first += 1
        # Copy any values still remaining in the right half.
        while second <= right:
            merged.append(nums[second])
            second +=1
        # Move the sorted values back into the active range.
        for index in range(len(merged)):
            nums[left+index] = merged[index]
        return inversions
    
    # Counts inversions while sorting the current range.
    def _merge_sort(self, nums:list[int], left:int, right:int) -> int:
        if left>=right:
            return 0
        mid:int = left + (right - left)//2
        inversions:int = 0
        # left half
        inversions += self._merge_sort(nums, left, mid)
        # right half
        inversions += self._merge_sort(nums, mid+1, right)
        # count inversions
        inversions += self._merge_and_count(nums, left, mid, right)
        return inversions
    
    def numberOfInversions(self, nums:list[int]) -> int:
        arr:list[int] = nums.copy()
        if len(arr)<=1:
            return 0
        return self._merge_sort(arr, 0, len(arr)-1)

def main() -> None:
    nums:list[int] = [8, 4, 2, 1, 5, 3, 7, 6]
    sol:Solution = Solution()
    print(sol.numberOfInversions(nums))

if __name__ == "__main__":
    main()