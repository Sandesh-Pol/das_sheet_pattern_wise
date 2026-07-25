# gridy variable tracking pattern

def largest_(nums):
    first = float('-inf')
    second = float('-inf')

    for num in nums:

        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return first,second

nums = [7, 2, 9, 4, 8]
print(largest_(nums))
