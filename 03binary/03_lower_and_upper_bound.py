def searchRange(nums, target):

    def find_left_bound(nums, target):
        index = -1
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                index = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return index

    def find_right_bound(nums, target):
        index = -1
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                index = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return index

    return [find_left_bound(nums, target), find_right_bound(nums, target)]


print(searchRange([1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5], 4))
