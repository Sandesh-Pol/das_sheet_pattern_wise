from sys import prefix


def product_of_array_without_self(nums):

    n = len(nums)

    ans = [1] * n
    for i in range(n):
        prod = 1

        for j in range(n):

            if i!=j:
                prod*=nums[j]

            ans[i] = prod

    return ans

def productExceptSelf(nums):

    n = len(nums)
    ans = [1] * n

    prefix = 1
    for i in range(n):
        ans[i] = prefix
        prefix*=nums[i]

    suffix = 1
    for i in range(n-1,-1,-1):
        ans[i] *= suffix
        suffix*=nums[i]

    return ans



print(product_of_array_without_self([1,2,3,4]))
print(productExceptSelf([1,2,3,4]))
