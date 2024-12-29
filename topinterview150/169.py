#find an element in the array that appears more than n / 2 times
def majorityElement(self, nums):
    count = 0
    ans = None
    
    for num in nums:
        if count == 0:
            ans = num
        count += (1 if num == ans else -1)

    return ans