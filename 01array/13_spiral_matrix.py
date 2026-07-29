def set_spiral_order(mat):

    ans = []

    top = 0
    right = len(mat[0]) - 1
    left = 0
    bottom =  len(mat) - 1

    while top <= bottom and left <= right:

        for col in range(left , right+1):
            ans.append(mat[top][col])
        top+=1

        for row in range(top,bottom+1):
            ans.append(mat[row][right])
        right-=1

        if top<= bottom:
            for col in range(right,left-1,-1):
                ans.append(mat[bottom][col])
            bottom-=1

        if left <= right:
            for row in range(bottom,top-1,-1):
                ans.append(mat[row][left])
            left-=1

    return ans

print(set_spiral_order([[1,2,3],[4,5,6],[7,8,9]]))
