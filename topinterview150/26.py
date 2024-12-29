# Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        for num in nums: #loop for each element of nums [1, 1, 2]
            if i < 1 or num > nums [i - 1]: #i < 1 always includes the first element
                # num > nums [i - 1] ensures that the current number is bigger than the last one added
                # making sure that only unique numbers are added to i
                nums[i] = num # places the current num at the i index of nums (overwrites any duplications)
                i += 1 #increment
        return i #return from the function