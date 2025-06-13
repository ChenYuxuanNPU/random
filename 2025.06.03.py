x = int(input("请输入待求阶乘的正整数："))  # 将需要求阶乘的正整数保存至x

# 方法1：使用由1不断自增至x的变量i做乘数，通过while循环进行计算
sum = 1
i = 1

while i <= x:
    sum = sum * i
    i = i + 1

print("方法1中，正整数", x, "的阶乘为：", sum)

# 方法2：使用range函数生成1至x的数字序列，并分别与sum相乘
sum = 1

for i in range(1, x + 1, 1):
    sum = sum * i

print("方法2中，正整数", x, "的阶乘为：", sum)
