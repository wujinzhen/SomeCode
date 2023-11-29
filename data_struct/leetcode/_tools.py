"""tool"""
import random

def get_random_list(count=10, up=100, low=0):
    return [random.randint(low, up) for i in range(count)]
