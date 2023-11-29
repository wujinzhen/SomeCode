"""
Boyer-Moore算法
从后往前匹配字符串, 该算法的目的是通过计算尽可能的让模式串移动多位, 从而达到快速比较字符的目的
分为两个规则: 坏字符规则 好后缀规则
坏字符规则:
    在模式串和主串匹配的过程中,如果出现不能匹配的字符,那么该字符即为坏字符,出现坏字符了就要计算当前模式串可移动的距离
这里坏字符对应模式串的位置记为 Si(坏字符在模式串的索引位置)
而坏字符在模式串中的位置记为Xi(如果不存在就是-1), 注意这里的位置要从模式串后面往前找起,避免一次移动过多
那么这里的可移动距离 = Si - Xi

如果只依据坏字符规则可能会出现模式串往前移动的情况,例子如下
    main='aaaaaaaaa'
    pattern='baa'
    这里可移动距离:0-2=-2
所以还需要依赖好后缀规则, 实际要移动的距离取好后缀和坏字符规则的最大移动距离

好后缀规则:
    在匹配过程中,当模式串的后缀一部分与主串后部分都匹配时, 这部分匹配的字符串就称为好后缀
如果好后缀在模式串中找不到也不代表可以将模式串整个移动,因为可能好后缀的后缀子串可能与模式串存在匹配
好后缀的后缀子串可能与模式串其他子串匹配或者与模式串的前缀匹配, 所以要在往后移动过程中计算出最大可移动距离

例子:
    main1='bcdfbc'
    pattern='bc'
    这种属于好后缀的后缀子串与主串的前缀匹配

    main='abcdfabc'
    pattern='bc'
    这种属于好后缀的后缀子串与主串的其他子串匹配
"""


def gen_bad_rule(pattern: str):
    """遍历字符串生成每个字符在字符串中的位置, 如果有多个相同字符则按照靠后的字符算"""
    bad_map = {}
    for i, v in enumerate(pattern):
        bad_map[v] = i
    return bad_map


def gen_good_rule(pattern: str):
    """好后缀规则, 这里还要注意如果有多个要保留最后一个
    一个数组存储按照后缀长度匹配的子串起始位置, 索引是子串的长度, 值是子串的起始位置
    一个数组存储该长度的子串是否与模式串的前缀匹配
    """
    p_len = len(pattern)
    suffix = [-1] * p_len
    prefix = [False] * p_len
    i = 0
    while i < p_len - 1:
        j = i
        k = 0
        while j >= 0 and pattern[j] == pattern[p_len-1+k]:
            j -= 1
            k += 1
            suffix[k] = j + 1
        if j == -1:
            prefix[k] = True
        i += 1
    return suffix, prefix


def get_good_suffix_index(j, p_len, suffix, prefix):
    k = p_len - 1 - j
    if suffix[k] != -1:
        return j - suffix[k] + 1
    r = j - 2
    while r < p_len - 1:
        if prefix[p_len - r] is True:
            return r
    return p_len


def bm(main: str, pattern: str):
    bad_map = gen_bad_rule(pattern)
    suffix, prefix = gen_good_rule(pattern)
    # print(bad_map, suffix, prefix)
    m_len = len(main)
    p_len = len(pattern)
    i = 0  # 表示当前移动的位置长度
    while i <= m_len - p_len:
        # 从模式串长度开始逐一比较
        j = p_len - 1
        while j >= 0:
            if main[j + i] != pattern[j]:
                break
            j -= 1
        # 这种情况就代表模式串与主串全部比较完了
        if j < 0:
            return i
        x = j - bad_map.get(main[j+i], -1)
        y = get_good_suffix_index(j=j, p_len=p_len, suffix=suffix, prefix=prefix)
        i += max(y, x)


if __name__ == '__main__':
    main = "aacdaabcd"
    pattern = 'acd'
    print(bm(main, pattern))