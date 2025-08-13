import random

def lunch():
    """随机选择一份午餐并返回结果"""
    午餐列表 = ["盖浇饭", "拉面", "沙拉", "汉堡", "水饺", "披萨"]
    return random.choice(午餐列表)

if __name__ == "__main__":
    result = lunch()
    print("推荐的午餐:", result)