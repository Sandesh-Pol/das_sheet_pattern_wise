def partition(nums, l, r):
    pivot = nums[l]
    i = l + 1
    j = r

    while True:
        while i <= j and nums[i] <= pivot:
            i += 1

        while i <= j and nums[j] > pivot:
            j -= 1

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        else:
            break

    nums[l], nums[j] = nums[j], nums[l]
    return j


def quick_sort(nums, l, r):
    if l < r:
        p = partition(nums, l, r)
        quick_sort(nums, l, p - 1)
        quick_sort(nums, p + 1, r)


nums = [11, 9, 17, 2, 12, 4]
quick_sort(nums, 0, len(nums) - 1)
print(nums)
