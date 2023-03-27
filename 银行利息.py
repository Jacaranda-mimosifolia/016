"""利息"""
print("""***银行***""")
print("""***功能菜单***
1.查看用户金额
2.存储
3.提取
4.退出""")
A = 0
while True:
    a = int(input("请选择您所办理的业务："))
    if a == 1:
        print(A)
    elif a == 2:
        b = int(input("请输入存储金额："))
        A += b
        print("存储成功")
    elif a == 3:
        b = int(input("请输入提取金额："))
        A -= b
        print("提取成功")
    elif a == 4:
        print("Bye!!!")
        break

print("***活期利息***")
print("利率：0.30%")
a = int(input("存储年数："))
for i in range(a):
    B = A * 0.003
    A += B
a=f"{A}"
print("总金额：%A")