# Brute Force solution
# class Solution:
#     def findPeakElement(self, arr:list[int])-> int:
#         n = len(arr)
#         if n == 0:
#             return -1
#         if n == 1:
#             return 0
#         for i in range(n):
#             if arr[i-1] == None:
#                 if arr[i+1] < arr[i]:
#                     return i
#             elif arr[i+1] == None:
#                 if arr[i-1] < arr[i]:
#                     return i
#             else:
#                 if arr[i-1]<arr[i] and arr[i+1]<arr[i]:
#                     return i     
#         return -1
# Optimal Solution
class Solution:
    def findPeakElement(self, arr:list[int])-> int:
        n = len(arr)
        low = 0
        high = n -1
        while(low<high):
            mid = low + (high - low) // 2
            if arr[mid] < arr[mid+1]:
                low =mid+1
            else:
                high = mid
        return low

# Driver code starts
def main() -> None:
    nums: list[int] = [1, 2, 1, 3, 5, 6, 4]
 
    obj = Solution()
    print(obj.findPeakElement(nums))
 
 
if __name__ == "__main__":
    main()