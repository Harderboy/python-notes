# 给定一个字符串，然后判断该字符串的长度。

# 方法1：使用内置方法 len()
str1 = "runoob"
print(len(str1))


# 方法2：循环、切片
def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter


str2 = "runoob"
print(str2[5:])  # b
print(str2[6:])  # （空）
print(str2[7:])  # （空）
print(type(str2[6:]))   # <class 'str'>
print(findLen(str2))

'''
知识总结：
  字符串[开始索引：结束索引：步长]


lang = 'python'
4.截取完整的字符串,浅拷贝
d=num_str[:]
print(d)

当头索引没有给出的时候默认从字符串开头开始截取
lang[:3]
# pyt

# 5.从开始位置，每隔一个字符截取字符串
e=num_str[::2]
print(e)
# 6.从索引1开始，每隔一个取一个,不给出尾索引才是最佳实践
f=num_str[1::2]
print(f)
# 7.截取从2-末尾-1的字符串
g=num_str[2:-1]
print(g)
# 8.截取字符串末尾的两个字符
h=num_str[-2::]
print(h)
当头索引为负数时，则是指从字符串的尾部开始计数，最末尾的字符记为-1，以此类推，因此此时应该注意尾索引的值，尾索引同样可以为负数，如果尾索引的值指明的字符串位置小于或等于头索引，此时返回的就是空字符串
lang[-2:]
# on
lang[-2,2]  都指向n
# ''
str = "runoob"
print(str[-2:3])  3 代表第一个o 用负数（逆序）表示为-3 就转换为[-2:-3] 尾索引小于头索引 返回空字符串
print(str[-3:-2])
# 9.字符串的逆序
i=num_str[-1::-1]
num_str[::-1]
print(i)
'''

# 以及
def length(src):
    # 字符串长度
    count = 0
    all_str = src[count:]

    for x in all_str:
        count += 1

    print("字符串长度为: %s" % count)

src = "Runoob"
length(src)