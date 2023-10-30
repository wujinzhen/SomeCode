"""
暴力搜索
"""

def bf(main, pattern):
    m = len(main)
    n = len(pattern)

    if n > m:
        return -1

    for i in range(m-n+1):
        if main[i:i+n] == pattern:
            return 1
    return -1


if __name__ == '__main__':
    print(bf('jiji8adnfi33ad', 'nf8'))