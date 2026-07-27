def max_sum_kd_alg(nums):

    max_sum = float('-inf')
    current = 0

    for num in nums:
        current += num

        max_sum = max(current, max_sum)

        if current < 0:
            current = 0

    return max_sum

def op_max_sum_kd_alg(nums):
    current = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current = max(nums[i], current + nums[i])
        max_sum = max(max_sum, current)

    return max_sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(max_sum_kd_alg(nums))
