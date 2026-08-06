import math


def min_arival_time(dist,hr):

    if hr <= len(dist) - 1:
        return -1

    def can_arrive(speed):
        total = 0

        for i in range(len(dist)-1):

            total += math.ceil(float(dist[i])/speed)

        total+=float(dist[-1])/speed

        return total <= hr


    l = 1
    h = 10 ** 7
    ans = - 1

    while l <= h:

        mid = l + (h-l) // 2

        if can_arrive(mid):
            ans = mid
            h = mid - 1
        else:
            l = mid + 1

    return ans

print(min_arival_time([1,3,2],6))
