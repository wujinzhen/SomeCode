import random


def get_random_list(nums: int = 10, limit: int = 100):
    """随机生成一个包含nums个数的最大数不超过limit的列表"""
    return random.sample(range(1, limit), nums)
