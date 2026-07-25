def majority_element(nums):
    freq = {}

    for num in nums:

        freq[num] = freq.get(num,0) + 1

    for key , value in freq.items():
        if value > len(nums) // 2:
            return key


def majority_sort(nums):
    nums.sort()
    return nums[len(nums)//2]

def majority_element_candidate(nums):

    count = 0
    candidate = None

    for num in nums:

        if count == 0:
            candidate = num

        if num == candidate:
            count+=1
        else:
            count-=1

        return candidate


print(majority_element([1,2,1,2,2]))
