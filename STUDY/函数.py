# encoding:utf-8
range()  # 生成一个可迭代的对象，通过list()可将其转成列表
# range(start, stop=None, step=1)

# ===============================================================
f'str'
money = 20000
robbers = 5
print(f'{robbers}劫匪每人分到了{(money/robbers):.0f}元')
# 格式转换  使用:.0f控制小数位

# ===============================================================
uper()  # 转成大写字母
lower()  # 转成小写字母

# ===============================================================
a = [5, 0, 3]
b = [5, 0, 3]
a.pop()  # ()指定移除一个元素
b.remove(5)  # 移除列表中首个值为5的元素
print(b)

# ===============================================================
repr()  # 函数可以转义字符串中的特殊字符
# 如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
s = ['hello\n']
s1 = repr(s)
a = 100
b = 200
x = a * b
z = b - a
print(s1)
print(repr((x, s, z)))  # repr中的元素必须加()

# ===============================================================
'''创建文本并写入文字'''
f = open('c:/text.txt', 'w')
f.write('Python是个非常好用的语言')
f.close()
'''读取文件'''
f = open('c:/text.txt', 'r')
aa = f.read()
print(aa)
f.close()

# open(filename, mode)
# filename：包含了你要访问的文件名称的字符串值。
# mode：决定了打开文件的模式：只读，写入，追加等，默认文件访问模式为只读(r)
# r   以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb  以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。
# r+  打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+ 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# w   打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb  以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# w+  打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb+ 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# a   打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab  以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# a+  打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# ab+ 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

# ===============================================================
