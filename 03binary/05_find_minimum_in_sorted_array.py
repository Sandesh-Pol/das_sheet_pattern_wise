def find_minimim(nums):
    l = 0
    r = len(nums)-1

    while l < r:

        mid = (l+r)//2

        if nums[mid] > nums[r]:
            l = mid + 1

        else:
            r = mid -1

    return nums[l]

print(find_minimim([5,6,7,8,-1,2,3,4]))

def find_minimim2(nums):
    l = 0
    r = len(nums)-1

    while l < r:

        mid = (l+r)//2

        if nums[mid] > nums[r]:
            l = mid + 1

        elif nums[mid] < nums[r]:
            r = mid

        else:
            r-=1

    return nums[l]

print(find_minimim2([2,2,2,0,1]))      # 0
