def chceck_assinding_decending(nums):
    ascending = True
    descending = True
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            ascending = False
        if nums[i] > nums[i+1]:
            descending = False

    return ascending or descending

print(chceck_assinding_decending([7,1,2,3,4,5]))
