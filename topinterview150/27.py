class Solution:
    def removeElement (self, nums: list[int], val: int) -> int:
        k = 0 # i initialize k in 0 to track all the positions in nums where val isnt found
        for num in nums: # for loop that iterates over each value of nums
            if num != val: # check if the value (num) is not equal to the target (val)
                nums[k] = num # if num != val, i assign it to k position in nums, overwriting the elements equal to val
                k += 1 #i increment the k to continue searching in nums
        return k # returns value of k which is the number of elements in the list that are not equal to val