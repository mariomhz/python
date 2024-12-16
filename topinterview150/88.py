#nums1 = [1, 2, 3, 0, 0, 0] # m=3
# nums2 = [2, 5, 6] # n = 3
# the goal is to merge the two arrays without generating a third array
# nums1 has enough space for the all the values in nums2
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n:int) -> None:
        # last index of nums1
        last = m + n - 1

        # merge them in reverse
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2 [n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
            
        #fill nums1
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1

def main():
        nums1 = [1, 2, 3, 0, 0, 0]  
        m = 3  
        nums2 = [2, 5, 6]  
        n = 3
        solution = Solution()
        solution.merge(nums1, m, nums2, n)
        print(nums1)

if __name__ == "__main__":
    main()