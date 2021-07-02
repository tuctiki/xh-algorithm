def basic(strs):
    if len(strs) == 0:
        return ''
    elif len(strs) == 1:
        return strs[0]
    else:
        done = False
        result = ''
        i = 0
        for s in strs[0]:
            j = 0
            while True:
                if j < len(strs) - 1:
                    if i < len(strs[j]) and i < len(strs[j+1]) and strs[j][i] == strs[j + 1][i]:
                        j += 1
                    else:
                        done = True
                        break
                else:
                    break
            if done:
                break
            result += s
            i += 1
        return result
