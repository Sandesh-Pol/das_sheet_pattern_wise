def max_stringth(nums):

    def gcd(a,b):
        while b:
            a,b = b,a%b
        return a
    n = len(nums)
    ans = 0

    for i in range(n):
        for j in range(i+1,n):
            gc = gcd(nums[i],nums[j])

            ans = max(ans,(nums[i] * nums[j]//(gc*gc)))

    return ans

print(max_stringth([2,3,5]))

