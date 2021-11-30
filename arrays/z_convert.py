"""
=======
Z字形变换
=======
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
"""

def opt(strs, lines):
    print('')
    res = []
    for l in range(lines):
        res.append('')

    for i in range(len(strs)):
        # row count
        rem = i % (lines - 1) 
        # either in group | for 0 or in group / for 1
        group = (i // (lines - 1)) % 2 
        s = strs[i]
        for j in range(lines - rem - 2):
            s = s + ' '
        if group == 0:
            res[rem] += s
        else:
            res[lines - rem - 1] += s
    
    for k in res:
        print(k)
