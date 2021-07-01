def basic(num1, num2):
    num3 = []
    for x in num1:
        if x in num2:
            num3.append(x)
            num2.remove(x)
    num3.sort()
    return num3


def by_dict(num1, num2):
    num3 = []
    dict0 = {}
    for x in num1:
        dict0[x] = dict0.get(x, 0) + 1
    for x in num2:
        if dict0.get(x, 0) > 0:
            dict0[x] -= 1
            num3.append(x)
    num3.sort()
    return num3


def for_sored(num1, num2):
    num3 = []
    i, j = 0, 0
    while i < len(num1) and j < len(num2):
        if num1[i] < num2[j]:
            i += 1
        elif num1[i] > num2[j]:
            j += 1
        else:
            num3.append(num1[i])
            i += 1
            j += 1
    return num3


