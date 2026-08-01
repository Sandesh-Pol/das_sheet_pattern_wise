def merge(nums, l, m, r):
    # fix the size of two divided array
    s1 = m - l + 1
    s2 = r - m

    L = [0] * s1
    R = [0] * s2

    # copy the elements in main array to two dicided arrat
    for i in range(s1):
        L[i] = nums[l + i]

    for j in range(s2):
        R[j] = nums[m + 1 + j]

    i = j = 0
    k = l

    # here compire the array elements of both array

    while i < s1 and j < s2:
        if L[i] <= R[j]:
            nums[k] = L[i]
            i += 1
        else:
            nums[k] = R[j]
            j += 1
        k += 1

    # copy reamining elements as it is

    while i < s1:
        nums[k] = L[i]
        i += 1
        k += 1

    while j < s2:
        nums[k] = R[j]
        j += 1
        k += 1


def divide(nums, l, r):
    if l < r:
        # find the mid
        m = (l + r) // 2

        # diveide the array on two parts
        divide(nums, l, m)
        divide(nums, m + 1, r)

        # merge with logic
        merge(nums, l, m, r)

    return nums


arr = [7, 8, 1, 5, 3, 2, 6, 4]
print(divide(arr, 0, len(arr) - 1))
