

def unfinishedTasks(tasks, shifts):

    remain = tasks[:]
    cur = 0

    ans = []

    for time in shifts:

        while cur < len(tasks) and time > 0:

            if time >= remain[cur]:

                time -= remain[cur]
                remain[cur] = 0
                cur += 1

            else:

                remain[cur] -= time
                time = 0

        ans.append(len(tasks) - cur)

        if cur == len(tasks):
            remain = tasks[:]
            cur = 0

    return ans


print(unfinishedTasks([1,4,4],[9,1,4]))