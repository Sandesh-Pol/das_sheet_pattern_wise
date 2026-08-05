# [1,2,1,3,5,6,4]

def find_peak_element(nums):
    l = 0
    r = len(nums)

    while l < r:
        mid = l + (r-l) // 2

        if nums[mid] < nums[mid+1]:
            l = mid + 1
        else:
            r = mid

    return l

print(find_peak_element([1,2,1,3,5,6,4]))
