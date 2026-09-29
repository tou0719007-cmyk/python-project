a = float(input("请输入第一个数字："))
b = float(input("请输入第二个数字："))

print("加法结果：", a + b)
print("减法结果：", a - b)
print("乘法结果：", a * b)
if b == 0:
    print("除法结果：不能除以0")
else:
    print("除法结果：", a / b)
    