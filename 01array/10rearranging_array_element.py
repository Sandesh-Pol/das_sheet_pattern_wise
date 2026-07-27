def rearranging_elements(nums):

    pos = []
    neg = []

    for i in nums:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)


    ans = []

    for i in range(len(pos)):
        ans.append(pos[i])
        ans.append(neg[i])

    return ans

def rearranging_element_opt(nums):

    ans = [0] * len(nums)

    pos = 0
    neg = 1

    for num in nums:

        if num > 0:
            ans[pos] = num
            pos+=2
        else:
            ans[neg] = num
            neg+=2

    return ans








print(rearranging_elements([3,1,-2,-5,2,-4]))
print(rearranging_element_opt([3,1,-2,-5,2,-4]))
