# 字符串匹配 中
"""
该算法的核心就是利用不匹配的字符的各种情况，跳过一定不能匹配的字符的情况将字符往后多移动
    滑动窗口字符的额匹配从后往前
坏字符规则：
    1.出现不匹配的字符，如果该字符在模式串中不存在，则可以直接将字符往后移动模式串的长度M，
    2.如果存在则将模式串中还没匹配部分的最后一个该字符移动到和主串对齐的位置
    总结一下可以得出一下移动计算公式：该不匹配字符在模式串中的下标Si，存在与模式串中另外靠后的相同字符下标Xi（如果不存在则是-1），
        两者相减就是此次字符串该移动的最大位数

好后缀规则：
    在匹配了一定长度的后缀之后出现不匹配字符的情况，则此时存在匹配好的好后缀，可以利用好后缀规则
    1.记匹配好的后缀为U，则如果模式串中还存在U~和U匹配，则将两者对齐
    2.以上情况不存在，则对比好后缀的后缀子串 和 模式串的前缀子串，找到两者之间能匹配的最长长度子串，移动到对齐
    3.如果以上都不匹配则直接将模式串移动到该不匹配的位置后面

对于两个规则的选择，选一个最终能移动的长度最大的规则
"""


def BM(max_str, min_str):
    """
    BM算法 坏字符规则 + 好后缀规则
    :param max_str:
    :param min_str:
    :return:
    """
    # 坏字符规则
    i = 0  # 初始化对齐位置
    max_len, min_len = len(max_str) - 1, len(min_str) - 1
    suffix, prefix = generateDoodSuffix(min_len, min_str)
    while i < max_len - min_len:
        is_bad = -1
        for j in range(min_len, -1, -1):  # 逐个遍历该窗口内的字符
            if max_str[j + i] != min_str[j]:
                is_bad = j  # 坏字符位置
                break
        if is_bad == -1:  # 说明遍历完并且全部匹配
            return i, i + min_len

        # 好后缀规则
        gap2 = 0  # 好后缀初始化位移数
        if is_bad < min_len:  # 存在好后缀
            # 寻找好后缀的最佳位移位置
            gap2 = get_gap2(is_bad, min_len, suffix, prefix)

        gap1 = min_len - min_str[:is_bad].rfind(max_str[is_bad])  # 在模式串的j位置之前的字符串中看看是否能找到和坏字符相同的字符
        i += max(gap1, gap2)  # 取两者最大的位移数


# 好后缀规则
def generateDoodSuffix(min_len, min_str):
    suffix = [-1] * min_len  # 模式串前缀匹配数组，下标表示匹配的字符长度，值表示在模式串中匹配的起始位置
    prefix = [False] * min_len  # 对应位置的前缀匹配起始位置为0的为True
    # 该for初始化suffix和prefix两个数组，TODO 看不懂
    for i in range(min_len):
        j, k = i, 0
        while j >= 0 and min_str[j] == min_str[min_len - k]:
            # 匹配从后往前，如果匹配则往前更新一位
            j -= 1
            k += 1
            suffix[k] = j + 1
        if j == -1:
            prefix[k] = True
    return suffix, prefix


def get_gap2(is_bad, min_len, suffix, prefix):
    """
    suffix数组储存的是模式串匹配到的子后缀最靠后位置的起始坐标，为什么是最靠后是怕滑动过头。
    而这种存储方式是为suffix[好后缀size]！=-1时候服务的，也就是能匹配到完整好后缀的时候用的，所以才存储靠后的。
    而当suffix[好后缀size]=-1时候，即完整好后缀在模式串中不存在的时候，
    我们需要去前缀中去找suffix[好后缀size-n]这样的好后缀的子串，
    而如果有多个重复匹配suffix注定不能粗糙前缀匹配到的起始位置，也就是0，所以才需要prefix数组
    """
    k = min_len - is_bad  # 一共有k位好后缀
    if suffix[k] != -1:  # 如果模式串中存在与K位好后缀相同的子串
        return is_bad + 1 - suffix[k]
    for i in range(is_bad + 2, min_len + 1):  # 如果好后缀中存在是以index=0的模式串开头的前缀子串
        if prefix[min_len + 1 - i] is True:
            return i
        i += 1
    return min_len + 1  # 以上两个情况不匹配，则直接位移整个模式串长度


if __name__ == '__main__':
    max_str = 'asdfjkzhol;'
    min_str = 'zho'
    print(BM(max_str, min_str))
