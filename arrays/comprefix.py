"""
==========
最长公共前缀
==========
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，则返回''
"""


def basic(strs):
    if not len(strs) == 0:
        i = 0
        for s in strs[0]:
            for t in strs[1:]:
                if not (i < len(t) and t[i] == s):
                    return strs[0][:i]
            i += 1
        return strs[0][:i]
    return ''
