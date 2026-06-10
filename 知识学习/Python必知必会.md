---
tags:
  - Python
Category:
  - 课内/讲义
  - 总结
---

# 一、基础知识和流程控制

1、 输入输出函数：print( end=, sep= ), input()

2、 合法标识符（变量名、函数名等）：只能含有数字, 字母以及下划线，不能以数字开头

3、 基本数据类型：int, float, string, bool

4、 数值型的四则运算符：+, -, *, /, //, %, **

5、 常用内置数学函数：abs(), max(), min(), pow(), round()

6、 比较运算符（用于数值型或字符串）：==, !=, <, <=, >, >= 

7、 逻辑运算符：not, and, or

8、 类型转换函数：int(), float(), str(), bool()

9、 赋值运算符：=, 复合赋值运算符，如 += 

10、 注释的写法：单行#，多行使用三引号

11、 if ... elif ... else 语句

12、 条件表达式：... if ... else ...

13、 while ... 语句

14、 for ... in ... 语句

15、 break, continue, 用于循环中的 else 语句

16、 range() 函数：range(n), range(a,b), range(a,b,k)

17、 random库：random(), randint(a,b), randrange(a,b,k)

18、 math库：pi, fabs(), ceil(), floor(), sqrt()

19、 time库：time()

# 二、序列：字符串、元组与列表（通用部分）

1、 理解索引、切片的概念，使用它们读取序列中的元素

2、 加法运算符（序列+序列），乘法运算符（序列*整数），成员运算符（in, not in），比较运算符（==, !=, <, <=, >, >=）

3、 函数：len(), max(), min(), sorted(), reversed(), sum() （除len()外，其它函数要求元素类型相同，sum()仅适合于数值型元素）

4、 内置函数：index(), count()

# 三、字符串

1、 函数： str(), ord(), chr()

2、 内置函数：lower(), upper(), split(), join()

# 四、元组

1、 函数：tuple()

# 五、列表

1、 使用索引和切片替换列表中的元素

2、 函数：list(), sorted(), reversed()

3、 内置函数：append(), insert(), extend(), pop(), remove(), clear(), reverse(), sort()

4、 使用 del 删除列表中的一个元素

5、 列表生成式（简单情况：一重循环，带条件 ）

6、 列表、字典、集合的可变性

# 六、字典

1、 函数：dict(), len(), max(), min(), sum()

2、 成员运算符（in, not in）

3、 使用 dict[key] 新增、取得、修改字典中的值

4、 使用 del 删除字典中的一个元素

5、 内置函数：get(), pop(), clear(), keys(), values(), items()

# 七、集合

1、 函数：set(), len(), max(), min(), sum()

2、 成员运算符（in, not in）

3、 内置函数：add(), remove()

# 八、函数

1、 函数的定义与调用

2、 函数返回值

3、 函数传参：形参与实参

4、 位置参数、关键字参数、默认值参数、变长参数

5、 变量作用域：全局变量global、局部变量、非局部变量nonlocal

6、 递归函数

7、 匿名函数 lambda 表达式

8、 高阶函数：map(), filter(), sorted()

# 九、异常

1、 try ... except ... else ... finally 语句

2、 raise 语句

3、 断言 assert 

# 十、模块与包

1、 import ... as ... 语句

2、 from ... import ... as ... 语句

# 十一、面向对象

1、基本概念：类、对象

2、私有方法与公有方法，私有属性与公有属性，self对象

3、特殊方法：`__init__()`，`__str__()`、`__repr__()`等

4、运算符重载：`__add__()`等四则运算符，`__eq__()`、`__lt__()`等比较运算符

5、了解继承、多态的基本概念

# 十二、文件处理

1、了解什么是文本文件，掌握文本文件的打开、读写、关闭：`open(), read(), write(), close()`

2、with语句和上下文管理

3、使用csv模块，可以对CSV格式文件进行读取和写入。
