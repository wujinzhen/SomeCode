"""
暴力搜索改进
"""

def rk(main, pattern):
    m = len(main)
    n = len(pattern)
    if n > m:
        return -1
    hash_p = simple_hash(pattern, 0, n-1)
    hash_list = []  # 缓存之前的计算结果
    for i in range(m-n+1):
        if i == 0:
            cur_h = simple_hash(main, 0, n-1)
            hash_list.append(cur_h)
        else:
            cur_h = hash_list[i-1] - simple_hash(main, i-1, i-1) + simple_hash(main, i+n-1, i+n-1)
            hash_list.append(cur_h)
        if cur_h == hash_p:
            if main[i:n+i] == pattern:
                return 1
    return -1



def simple_hash(main, start, end):
    "计算字符串的简单hash值"
    ret = 0
    for c in main[start:end+1]:
        ret += ord(c)
    return ret


if __name__ == '__main__':
    print(rk('jiji8adnfi33ad', 'nfi33'))