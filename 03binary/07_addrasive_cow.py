def can_place(stalls,cows,min_distance):
    count = 1
    last_pos = stalls[0]

    for i in range(1,len(stalls)):
        if stalls[i] - last_pos >= min_distance:
            count += 1
            last_pos = stalls[i]

            if count == cows:
                return True

    return False

def aggressive_cow(stalls,cows):

    low = 1
    high = stalls[-1] - stalls[0]
    ans = 0

    while low <= high:


        mid = low + (high-low) // 2

        if can_place(stalls,cows,mid):
            ans = mid
            low = mid + 1

        else:
            high = mid - 1

    return ans


print(aggressive_cow([1, 2, 4, 8, 9],3))
