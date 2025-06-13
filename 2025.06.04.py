import math

n = 3  # 当前计算的是正n边形的周长，n代表了边数
pi = 0  # pi代表了使用正多边形计算的近似值，math.pi代表了真实值

while True:  # 构造无限循环

    pi = n * math.sin(math.pi / n)  # 按照公式计算近似值pi=n * sin(π/n)

    if math.fabs(math.pi - pi) < 0.0001:  # 当近似值与真实值差距的绝对值小于0.0001，跳出循环
        print(f"正" + str(n) + "边形计算的π近似值为" + str(pi))  # 输出当前使用的正n边形及其对应的近似值pi
        break

    n += 1
