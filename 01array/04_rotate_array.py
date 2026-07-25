def rotate_array_with_space(nums,k):
    n = len(nums)
    k %= n

    temp = [0] * n
    for i in range(n):

        temp[(i+k)%n] = nums[i]

    for i in range(n):
        nums[i] = temp[i]

    return nums

def rotate_array_no_extra_space(nums,k):
    n = len(nums)
    k %= n

    def reverse(l,r):
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1

    reverse(0,n-1)
    reverse(0,k-1)
    reverse(k,n-1)

    return nums




print(rotate_array_with_space([1,2,3,4],2))
print(rotate_array_no_extra_space([1,2,3,4],2))
