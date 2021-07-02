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
            j = 1
            while j < len(strs):
                if i < len(strs[j]) and strs[j][i] == s:
                    j += 1
                else:
                    done = True
                    break
            if done:
                break
            result += s
            i += 1
        return result
