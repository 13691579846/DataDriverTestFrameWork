'''
请直接运行此文件，即可得出对应题目答案^_^
'''

"""
1.python中逻辑运算符有哪些? 它们之间有什么区别?
答：
	and ：a and b 如果表达式a为真，b决定返回值是True还是False 如果b为真 返回True 如果b为假 则返回False；如果a为假，直接返回False
	or    ：a or b 如果表达式a为真 ，不需要再看b表达式的真假，则 整个表达式返回True ；如果a为假，b为真 返回True，a，b都为假返回False
	not  ：not a 如果a为真 表达式返回False； 如果a为假 表达式返回True
	除了以上的不同之外，优先级也不通 not>and>or
"""

"""
2.如下比较运算分别返回什么？
如果a = 15，b = 9，则a == b 、a != b 、a > b 、(a - 5) < b 、a >= b ** 2 、(a + 13 - 10 * 2) <= (b // 2 * 5 + 35 % 4) 
答：
表达式分别返回：False，True，True，False，False，True
"""

"""
3.定义字符串I'm Lemon, I love Python automated testing！
答：
"""
myStr = "I'm Lemon, I love Python automated testing！"

'''
4.把website = 'http://www.python.org'中的python字符串取出来
答：
'''

website = 'http://www.python.org'
print(website[11:17])
# 或者
print(website.split('.')[1])

'''
5.将给定字符串前后的空格除去，把PHP替换为Python
best_language = "     PHP is the best programming language in the world!      "
答：
'''
best_language = "     PHP is the best programming language in the world!      "
print(best_language.strip().replace('PHP', 'Python'))


'''
6.演练字符串操作
'''
my_hobby = "Never stop learning!"
# 答：
#     截取从 2 ~ 6位置 的字符串
print(my_hobby[2:7])

    # 截取从 2 ~ 末尾的字符串
print(my_hobby[2:])

    # 截取从 开始~ 6 位置 的字符串
print(my_hobby[:7])

    # 截取完整的字符串
print(my_hobby[:])

    # 从开始位置，每隔一个字符截取字符串
print(my_hobby[::2])

    # 从索引 3 开始，每隔2个取一个
print(my_hobby[3::3])

    # 截取从 2 ~ 末尾-1的字符串
print(my_hobby[2:-1])

    # 截取字符串末尾两个字符
print(my_hobby[-2:])

    # 字符串的逆序（拓展）
print(my_hobby[::-1])

'''
7.去生鲜超市买橘子
    收银员输入橘子的价格，单位：元／斤

    收银员输入用户购买橘子的重量，单位：斤

    计算并且 输出 付款金额
'''
# 答：

while 1:
    price = input('请输入橘子的单价>>')
    weight = input('请输入用户购买橘子的重量>>')
    if price.replace('.','').isdigit() and weight.replace('.','').isdigit():
        totalPrice = float(price) * float(weight)
        print('%s斤橘子的总价为%2s' % (weight, totalPrice))
    else:
        print('请重新输入数据')