def longest_common_prefix(strs):

    if not strs:
        return ""

    first = strs[0]

    for i in range(len(first)):

        ch = first[i]

        for word in strs[1:]:

            if i >= len(word) or word[i]!=ch:

                return first[:i]

    return first

def longestCommonPrefix(strs):
        if not strs:
            return ""

        for i in range(len(strs[0])):

            for j in range(1, len(strs)):

                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0]

print(longest_common_prefix(["flower","flow","flight"]))

print(longestCommonPrefix(["flower","flow","flight"]))