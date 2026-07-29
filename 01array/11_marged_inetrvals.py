def merge_intervals(intervals):

    intervals.sort()
    i = 0

    while i < len(intervals) - 1:
        j = i + 1

        while j < len(intervals):

            if intervals[j][0] <= intervals[i][1]:

                intervals[i][1] = max(intervals[j][1], intervals[i][1])
                intervals.pop(j)
            else:

               j+=1
        i+=1

    return intervals

def merge_intervals_obti(intervals):

    intervals.sort()
    ans = [intervals[0]]
    print(ans)

    for current in intervals[1:]:

        last = ans[-1]
        print(last)

        if current[0] <= last[1]:

            last[1] = max(last[1],current[1])

        else:
            ans.append(current)

    return ans

print(merge_intervals_obti([[1,3],[2,6],[8,10],[15,18]]))
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
