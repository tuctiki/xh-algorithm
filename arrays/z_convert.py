


def basic(strs, lines):
    print('')
    i = 0
    while i < lines:
        j = 0
        while j < len(strs):
            rem = j % (lines - 1)
            group = (j // (lines - 1)) % 2
            if rem == i and group == 0:
                print(strs[j], end = '')
                for s in range(lines - rem - 2):
                    print (' ', end = '')
            elif group == 1 and rem + i == lines - 1:
                print(strs[j], end = '')
                for s in range(lines - rem - 2):
                    print (' ', end = '')
            j = j + 1
        print('')
        i = i + 1
    return

