> 做答页面：https://ks.wjx.com/vm/wEbs7Mk.aspx# 提交后将自动显示成绩和答案。

#### [单项选择题001]

- 下列程序的输出是（　　）

```python
for x in range(1,10):    
	if x % 2 !=0:        
		continue    
	print(x, end=' ')
```

- [x] A. 1 3 5 7 9
- [ ] B. 2 4 6 8 10
- [ ] C. 2 4 6 8
- [ ] D. 1 3 5 7

#### [单项选择题002]

- 给出如下代码 `TempStr ="Hello World"` ,可以输出World子串的是（　　）。

- [ ] A. print(TempStr[-5:])
- [ ] B. print(TempStr[-4:-1])
- [ ] C. print(TempStr[-5:0])
- [ ] D. print(TempStr[-5:-1])

#### [单项选择题003]
- 在Python中,正确的赋值语句为（　　）

- [ ] A. x+y=10
- [ ] B. x=2y
- [x] C. x=y=30
- [ ] D. 3y=x+1

#### [单项选择题004]
- 语句x=input()执行时,如果从键盘输入12并按回车键,则x的值是( )

- [x] A. '12'
- [ ] B. 12
- [ ] C. 12+空格
- [ ] D. "12.0"

#### [单项选择题005]
- 执行下列代码后,m,n的值分别是（　　）

```python
n = 123456789
m = 0
while n != 0:
    m = (10 * m) + (n % 10)
    n //= 10
```

- [ ] A. m = 0, n = 0
- [ ] B. m = 123456789, n = 1
- [x] C. m = 987654321, n = 0
- [ ] D. m = 1,n = 9

#### [单项选择题006]

- 下面代码的输出结果是（　　）

```python
x = 1
x *= 3+5**2
print(x)
```

- [x] A. 28
- [ ] B. 14
- [ ] C. 13
- [ ] D. 29

#### [单项选择题007]
- 拟在屏幕上打印输出“Hello World”,以下选项中正确的是（　　）

- [ ] A.  `print(Hello World)`
- [x] B.  `print('Hello World')`
- [ ] C.  `printf("Hello World")`  
- [ ] D.  `printf('Hello World')`

#### [单项选择题008]
- 将以下代码运行后输出的是（　　）。

```python
li = ['alex','eric','rain']
s = "_".join(li)
print(s)
```

- [ ] A.  ` _alex_eric_rain`
- [ ] B.   `_alex_eric_rain_`
- [ ] C.  `alex_eric_rain`
- [ ] D.   `alex_eric_rain_`

#### [单项选择题009]
- 设 `lt=['A','B','1','2']`,下列选项中（　　）可以实现将lt中各元素用'-'连接输出,即输出`A-B-1-2` 。

- [ ] A. print(lt[0:3])
- [ ] B. print(lt[0:3],'-')
- [ ] C. print('-'.join(lt))
- [ ] D. print('-'.split(lt))

#### [单项选择题010]
- 下列语句执行后的输出是（　　）。

```python
if 2:
    print(5)
else:
    print(6)
```

- [ ] A. 0
- [ ] B. 2
- [x] C. 5
- [ ] D. 6

#### [单项选择题011]
- 下述while循环执行的次数为（　　）

```python
k = 10
while k > 2:
	print(k)
	k = k-2
```

- [ ] A. 3
- [ ] B. 10
- [ ] C. 5
- [x] D. 4

#### [单项选择题012]
- 下面代码的输出结果是（　　）。

```python
sum = 1
for i in range(1,101):
	sum += i
print(sum)
```

- [ ] A. 5049
- [ ] B. 5052
- [ ] C. 5051
- [x] D. 5050

#### [单项选择题013]
- 下列程序输出的最后一个值是（　　）

```python
age = 23
start = 2
if age % 2 != 0:
	start = 1
for x in range(start, age + 2, 2):
	print(x)
```

- [x] A. 23
- [ ] B. 21
- [ ] C. 25
- [ ] D. 22

#### [单项选择题014]
- 下列表达式的值为True的是 ( )。

- [x] A. 2!=5 or 0
- [ ] B. 3 > 2 > 2
- [ ] C. 5+4j > 2-3j
- [ ] D. 1 and 5==0

#### [单项选择题015]
- 下面代码的输出结果是（　　）。

```python
for a in 'mirror':
	print(a,end="")  
	if a == 'r':
		break
```

- [ ] A. mir
- [ ] B. mirror 
- [x] C. mi 
- [ ] D. mirr

#### [单项选择题016]
- 下列语句中,在Python中非法的是（　　）

- [ ] A. x=y=z=1  
- [ ] B. x,y=y,x  
- [x] C. x=(y=z+1)
- [ ] D. x+=y

#### [单项选择题017]
- 下面代码的输出结果是（　　）。

```python
a,b,c,d,e,f = 'Python'
print(b)
```

- [x] A. 'y'
- [ ] B. b 
- [ ] C. 1 
- [ ] D. 0

#### [单项选择题018]
- 下列代码执行结束后，j的值是（　　）

```python
j = 1
for i in range(0,10):
	j += j
```

- [ ] A. 55
- [ ] B. 48
- [x] C. 1024
- [ ] D. 18

#### [单项选择题019]
- 下列程序共输出（      ）个值:

```python
age = 23
start = 2
if age % 2 != 0:
	start = 1
for x in range(start, age + 2, 2):
	print(x)
```

- [ ] A. 16  
- [ ] B. 14 
- [ ] C. 12
- [ ] D. 10

#### [单项选择题020]
- 执行代码,其运行结果是（　　）

```python
x = "foo"
y = 2
print(x+y)
```

- [ ] A. foo   
- [ ] B. foofoo  
- [ ] C. foo2  
- [ ] D. TypeError

#### [单项选择题021]
- 下面代码的执行结果是（　　）。

```python
x = "Happy!"
print(x * 3)
```

- [ ] A. 系统报错   
- [ ] B. Happy!*3  
- [ ] C. HHHaaappppppyyy!!! 
- [ ] D. Happy!Happy!Happy!

#### [单项选择题022]
- 下面if语句统计“成绩(mark)优秀(>=90)的男生以及不及格(<60)的男生”的人数,正确的语句为（　　）

- [ ] A. if gender=="男" and mark<60 or mark>=90:
- [ ] B. if gender=="男" and mark<60 and mark>=90:
- [ ] C. if gender=="男" and (mark<60 or mark>=90):
- [ ] D. if gender=="男" or mark<60 or mark>=90:

#### [单项选择题023]
- 如下代码的输出结果是（　　）。

```python
s = 'Python is Open Source!'
print(s[0:].upper())
```

- [ ] A. PYTHON IS OPEN SOURCE!
- [ ] B. PYTHON IS OPEN SOURCE
- [ ] C. Python is Open Source!
- [ ] D. PYTHON

#### [单项选择题024]
- 如下代码的输出结果是（　　）

```python
s = "abcdefghijklmn"
print(s[1:10:3])
```

- [ ] A. beh
- [ ] B. behk  
- [ ] C. adg  
- [ ] D. adgj

#### [单项选择题025]
- 对于列表 `L=[1,2,'Python',[1,2,3,4,5]]` , `L[-3]` 是（　　）。

- [ ] A. 1
- [ ] B. 2
- [ ] C. 'Python'  
- [ ] D. [1,2,3,4,5]

#### [单项选择题026]
- 在Python函数中,用于获取用户输入的是（　　）。

- [ ] A. get()  
- [ ] B. print()  
- [ ] C. input()
- [ ] D. eval()

#### [单项选择题027]
- 下面代码的输出结果是（　　）。

```python
for i in range(1,6):
	if i/3 == 0:
		break
	else:
		print(i,end=",")
```

- [ ] A. 1,2,  
- [ ] B. 1,2,3,4,5,
- [ ] C. 1,2,3,4,  
- [ ] D. 1,2,3,

#### [单项选择题028]
- 下面代码的输出结果是（　　）。

```python
str1 = "mysqlsqlserverPostgresQL"
str2 = "sql"
ncount = str1.count(str2,10)
print(ncount)
```

- [ ] A. 3
- [ ] B. 0
- [ ] C. 4  
- [ ] D. 2

#### [单项选择题029]
- 下面代码的输出结果是（　　）。

```python
x = 10
y = 3
print(x%y,x**y)
```

- [ ] A. 1 1000
- [ ] B. 3 30  
- [ ] C. 1 30  
- [ ] D. 3 1000

#### [单项选择题030]
- 下列for循环执行后,输出结果的最后一行是（　　）。

```python
for i in range(1,3):
	for j in range(2,5):
		print(i*j)
```

- [ ] A. 2 
- [ ] B. 6
- [ ] C. 8
- [ ] D. 15

#### [单项选择题031]
- 下面代码的输出结果是（　　）。

```python
for i in range(1,10,2):
	print(i,end=',')
```

- [ ] A. 1,3,5,7,9,
- [ ] B. 1,4,7,  
- [ ] C. 1,4,  
- [ ] D. 1,3,

#### [单项选择题032]
- 下面代码的输出结果是（　　）。

```python
z = 12.12 + 34j
print(z.real)
```

- [ ] A. 12.12
- [ ] B. 34.0  
- [ ] C. 12  
- [ ] D. 34

#### [单项选择题033]

- 在Python中，如何复制一个列表？

- [ ] A. new_list = old_list
- [ ] B. new_list = old_list.clone()
- [ ] C. new_list = copy(old_list)
- [ ] D. new_list = old_list.copy()

#### [单项选择题034]
- 下面代码的输出结果是（　　）

```python
ls = list(range(1,4))
print(ls)
```

- [ ] A. [0,1,2,3]  
- [ ] B. {0,1,2,3}   
- [ ] C. [1,2,3]
- [ ] D. {1,2,3}

#### [单项选择题035]
- 下面代码段的的执行后x的值是（　　）

```python
x = 0
if x == 1:
	x = x + 1
print(x)
```

- [ ] A. 0
- [ ] B. 1  
- [ ] C. 2  
- [ ] D. 出错

#### [单项选择题036]
- 下列程序的输出是（　　）

```python
for x in (1,10):
	if x%2 == 0:
		break
	print(x,'',end='')
```

- [ ] A. 2 4 6 8  
- [ ] B. 什么也不会输出  
- [ ] C. 1
- [ ] D. 2

#### [单项选择题037]
- 下面代码的输出结果是（　　）。

```python
sum = 0
for i in range(2,101):
	if i % 2 == 0:
		sum += i
	else:
		sum -= i
print(sum)
```

- [ ] A. 51
- [ ] B. -50  
- [ ] C. 49  
- [ ] D. 50

#### [单项选择题038]
- 下面代码的执行结果是（　　）。

``` 
print(pow(3,0.5)*pow(3,0.5)==3)
```

- [ ] A. True   
- [ ] B. pow(3,0.5)*pow(3,0.5)==3   
- [ ] C. 3   
- [ ] D. False

#### [单项选择题039]
-  下面代码的输出结果是（　　）。

```python
a = "ac"
b = "bd"
c = a + b
print(c)
```

- [ ] A. acbd
- [ ] B. dbac  
- [ ] C. bdac
- [ ] D. abcd

#### [单项选择题040]
- 下面代码的输出结果是（　　）。

```python
sum = 0
for i in range(0,100):
	if i%2 == 0:
		sum -= i
	else:
		sum += i
print(sum)
```

- [ ] A. -49  
- [ ] B. -50  
- [ ] C. 49
- [ ] D. 50  

#### [单项选择题041]
- 下面代码的输出结果是（　　）。

```python
for n in range(100,200):
	i = n // 100
	j = n // 10 % 10
	k = n % 10
	if n == i**3 + j**3 + k**3:
		print(n)
```

- [ ] A. 152  
- [ ] B. 159  
- [ ] C. 157 
- [ ] D. 153

#### [单项选择题042]
- 以下选项中,输出结果为 False 的是（　　）。

- [ ] A. 'python123' > 'python'  
- [ ] B. 'ABCD' == 'abcd'.upper()   
- [ ] C. ''<'a'   
- [ ] D. 'python' < 'pypi'

#### [单项选择题043]
-  下列代码段执行后, j 的值是（　　）

```python
j = 1
for i in range(0,10):
	j += i
```

- [ ] A. 36  
- [ ] B. 46
- [ ] C. 11  
- [ ] D. 10

#### [单项选择题044]
- 下面代码: print( 0.1 + 0.2 == 0.3) 的输出结果是（　　）

- [ ] A. while  
- [ ] B. 0  
- [ ] C. -1
- [ ] D. False

#### [单项选择题045]
- 下列说法中正确的是（ ）。

- [ ] A. break用在for语句中,而continue用在while语句中
- [ ] B. break用在while语句中,而continue用在for语句中
- [ ] C. continue能结束循环,而break只能结束本次循环
- [ ] D. break能结束循环,而continue只能结束本次循环

#### [单项选择题046]
- 下列哪个关键字用于定义函数？（ ）

- [ ] A. define
- [ ] B. function
- [ ] C. func
- [ ] D. def

#### [单项选择题047]
- 以下关于Python语句的叙述中,正确的是（ ）

- [ ] A. 同一层次的Python语句必须对齐
- [ ] B. Python语句可以从一行的任意一列开始
- [ ] C. 在执行Python语句时,可发现注释中的拼写错误
- [ ] D. Python程序的每行只能写一条语句

#### [单项选择题048]
- 在Python中，如何获取列表list的长度？（   ）

- [ ] A. len(list)
- [ ] B. length(list)
- [ ] C. list.size()
- [ ] D. sizeOf(list)

#### [单项选择题049]
- 以下叙述正确的是（ ）

- [ ] A. continue语句的作用是结束整个循环的执行
- [ ] B. 在循环体内使用break语句或continue语句的作用相同
- [ ] C. 只能在循环体内使用break语句
- [ ] D. 从多层循环嵌套中退出时，只能使用goto语句

#### [单项选择题050]
- Python程序通过（ ）来区分代码块的级别

- [ ] A. 缩进
- [ ] B. begin 和 end
- [ ] C. 大括号 { }
- [ ] D. 中括号 [ ]

#### [单项选择题051]
- 下列Python数据中其元素可以改变的是(   )

- [ ] A. 列表
- [ ] B. 元组
- [ ] C. 字符串
- [ ] D. 数组

#### [单项选择题052]
- 关于break语句与continue语句的说法中,以下选项中不正确的是（ ）。

- [ ] A. 当多个循环语句嵌套时,break语句只适用于最里层的语句
- [ ] B. break语句结束循环,继续执行循环语句的后续语句
- [ ] C. continue语句结束循环,继续执行循环语句的后续语句
- [ ] D. continue语句类似于break语句,也必须在for、while循环中使用

#### [单项选择题053]
- 以下选项中,不属于Python保留字的是（ ）。

- [ ] A. def  
- [ ] B. import
- [ ] C. type
- [ ] D. elif

#### [单项选择题054]
- 以下选项中,不是Python数据类型的是（ ）。

- [ ] A. 实数
- [ ] B. 列表  
- [ ] C. 字符串  
- [ ] D. 整数

#### [单项选择题055]
- 以下选项中,不是Python语言保留字的是（ ）。

- [ ] A. try  
- [ ] B. del  
- [ ] C. int
- [ ] D. None

#### [单项选择题056]
- 以下选项中,关于Python字符串的描述错误的是（ ）。

- [ ] A. Python语言中,字符串是用一对双引号""或者一对单引号 '' 括起来的零个或者多个字符
- [ ] B. Python字符串提供区间访问方式,采用[N:M]格式,表示字符串中从N到M的索引子字符串(包含N和M)
- [ ] C. 字符串包括两种序号体系:正向递增和反向递减
- [ ] D. 字符串是字符的序列,可以按照单个字符或者字符片段进行索引

#### [单项选择题057]
- 下面不属于程序的基本控制结构的是

- [ ] A. 顺序结构   
- [ ] B. 选择结构   
- [ ] C. 循环结构  
- [ ] D. 输入输出结构

#### [单项选择题058]
- Python序列类型包括:字符串、列表和（ ）

- [ ] A. 元组
- [ ] B. 整数  
- [ ] C. 字典  
- [ ] D. 集合

#### [单项选择题059]
- 关于Python的元组类型,以下选项中描述错误的是（ ）。

- [ ] A. 元组一旦创建就不能被修改
- [ ] B. 一个元组可以作为另一个元组的元素,可以采用多级索引获取信息
- [ ] C. 元组中元素不可以是不同类型
- [ ] D. Python中元组采用逗号和圆括号(可选)来表示

#### [单项选择题060]
- 下面哪个不是Python合法的标识符（ ）


- [ ] A. int32
- [ ] B. 40X
- [ ] C. `__name__`
- [ ] D. tt
#### [单项选择题061]

- 以下选项中，不符合 Python 语言变量命名规则的是(    )。
- [ ] A. scoreList
- [ ] B. score_list
- [ ] C. -scoreList
- [ ] D. _scoreList

#### [单项选择题062]

- 下面有关 print( a , b , sep = "," , end = "#")语句的说法，不正确的
  是（    ）。
- [ ] A. print( a , b , end = "#" , sep = ",")与题干语句写法等效
- [ ] B. print( end = "#" , sep = "," , a , b)与题干语句写法等效
- [ ] C. 题干语句中 a 和 b 之间的间隔符为英文逗号
- [ ] D. 题干语句执行后最后一个字符是#

#### [单项选择题063]

- 下面 Python 执行后的输出结果是(    )。

  ```python
  for i in range(1,10):
      continue
  print(i,end='#')
  ```

- [ ] A. 1#2#3#4#5#6#7#8#9#10

- [ ] B. 1#2#3#4#5#6#7#8#9#

- [ ] C. 9#

- [ ] D. 9

#### [单项选择题064]

- 以下 Python 代码执行后输出结果是(    )。

```python
loopCount = 0 #存储循环次数
for i in range(10):
    loopCount += 1
    i *= 2
print(loopCount)
```

- [ ] A. 4
- [ ] B. 5
- [ ] C. 9
- [ ] D. 10

#### [单项选择题065]

- 下面 Python 代码的功能是统计非小写字母的数量，在横线之间应填入代码是(    )。

```python
myStr = "The Great Wall is famous in the world."

notLowerCount = 0
for c in myStr:
    if ________:
        notLowerCount += 1
print(notLowerCount)
```

- [ ] A. not ("a"<=c<="z")
- [ ] B. "a"<=c<="z"
- [ ] C. c<"a" and c>"z"
- [ ] D. not (c<"a" and c>"z")

#### [单项选择题066]

- 下面 Python 代码执行后输出是 ( ) 。

```python
Sum = 0
for i in range(1,10,3):
    if i%2 == 0:
        Sum += i
    else:
        continue
print(Sum)
```

- [ ] A. 0
- [ ] B. 1
- [ ] C. 4
- [ ] D. 20

#### [单项选择题067]

- 执行以下 Python 代码后，数据结果是(   )。

```python
x, y = 10, 20
z = x
x = y
y = z
print(x, y, z, sep=",")
```

- [ ] A. 10,10,20
- [ ] B. 10,20,20
- [ ] C. 20,20,10
- [ ] D. 20,10,10

#### [单项选择题068]

- 下面 Python 代码，执行后输出是( )。

```python
c = "*"
for i in range(1, 5):
    c *= i
print( len(c) )
```

- [ ] A. 0
- [ ] B. 1
- [ ] C. 24
- [ ] D. 120

#### [单项选择题069]

- 假设某程序代码中有 print = 10，下列有关说法中正确的是（ ）。

- [ ] A. 该行代码错误，因为 print 是关键字，不能作为变量名称；
- [ ] B. 该行代码错误，因为 print 是内置函数名，不能作为变量名称；
- [ ] C. 该行代码没有错误，print 可以作为变量名称，虽然非常不可取；
- [ ] D. 该行代码没有错误，虽然 print 是关键字，但也可以作为变量名称，虽然非常不可取；

#### [单项选择题070]

- Python 表达式 10 % 2 or 2 + 1 的值为（ ）。

- [ ] A. 0

- [ ] B. 1

- [ ] C. 2

- [ ] D. 3


#### [单项选择题071]

- 以下 Python 用于输出 3 的平方根并四舍五入到两位小数，应在横线处填写代码是（ ）。

```python
from math import sqrt
print(________)
```

- [ ] A. round(math.sqrt(3),2)
- [ ] B. round(2,math.sqrt(3))
- [ ] C. round(sqrt(3),2)
- [ ] D. round(2,sqrt(3))

#### [单项选择题072]

- 执行如下代码，其输出是(   )。选择项中的□表示空格

```python
print(123,"XYZ",end="")
print()
print("ABC")
```

- [ ] A. 

  ```
  123□XYZ
  
  ABC
  ```
  
- [ ] B. 

  ```
  123□XYZ
  ABC
  ```
  
- [ ] C. 

  ```
  123XYZ
  
  ABC
  ```

- [ ] D. 

  ```
  123□XYZ□ABC
  ```

#### [单项选择题073]

- 下面有关 Python 中 if 语句的说法，错误的是。

- [ ] A. 一个 if 语句可以有 0 个或多个 elif 子句；
- [ ] B. 一个 if 语句最多只能有一个 else 子句；
- [ ] C. elif 是 Python 关键字，不可用作变量名；
- [ ] D. 在一个 if 语句中，满足条件的被控制语句都会被执行；

#### [单项选择题074]

- 下述代码用于随机输出 1 个小写英文字母，横线处应填写代码是（ ）。

```python
import random
print(________)
```

- [ ] A. chr(ord("a") + int(random.random() * 1000) % 26)
- [ ] B. chr('a' + int(random.random() * 1000) % 26)
- [ ] C. ord('a' + int(random.random() * 1000) % 26)
- [ ] D. chr(65 + int(random.random() * 1000) % 26)

#### [单项选择题075]

- 以下程序输出 OK 次数为（ ）。

```python
for i in range(8,2,-2):
    for j in range(i):
        print("OK")
```

- [ ] A. 0
- [ ] B. 12
- [ ] C. 18
- [ ] D. 20

#### [单项选择题076]

- 有关下面 Python 代码执行后的描述，正确的是（ ）。

```python
N = 100
for i in range(N):
    SUM += i
else:
    print(SUM)
```

- [ ] A. 程序执行结束后，将输出 1-100 之和
- [ ] B. 程序执行结束后，将输出 0-99 之和
- [ ] C. 程序执行结束后，将输出 99
- [ ] D. 代码执行过程中将报错

#### [单项选择题077]

- 下面程序执行后其输出是（ ）。

```python
N = 10
for i in range(1, N):
    if i % 2:
        continue
    print(i, end="")
```

- [ ] A. 1357
- [ ] B. 13579
- [ ] C. 2468
- [ ] D. 246810

#### [单项选择题078]

- 下面程序代码执行后输出是（ ）。

```python
for i in range(10):
    continue
else:
    print(i)
```

- [ ] A. 没有输出
- [ ] B. 9
- [ ] C. 10
- [ ] D. 11

#### [单项选择题079]

- 在 Python 中，表达式 `int("123")*2` 的值为（ ）。

- [ ] A. 123
- [ ] B. 246
- [ ] C. 246.0
- [ ] D. 123123

#### [单项选择题080]

- 求解鸡兔同笼。下列选择错误的是（ ）。

```python
# 假设输入均为正整数，排除其他输入情况
Head = int(input()) # 输入头的数量
Foot = int(input()) # 输入脚的数量
# rHead为兔头，cHead为鸡头
for rHead in range(0,Head+1):
    cHead= Head - rHead
    if (rHead * 4 + cHead * 2) == Foot:
        break
else:
    print(rHead, cHead) # 输出兔和鸡的数量
```

- [ ] A. 如果有解，不会有输出
- [ ] B. 如果无解，输出值是错误
- [ ] C. 程序没有语法错误
- [ ] D. 输出语句不会被执行，因为有 break 存在；
#### [单项选择题081]

- 在 Python 中，表达式 list(range(5))的值是 (   )

- [ ] A. [0,1,2,3,4]
- [ ] B. [0,1,2,3,4,5]
- [ ] C. [1,2,3,4]
- [ ] D. [1,2,3,4,5]

#### [单项选择题082]

- 表达式 `[1,3,5,7][::-1]` 的值是 (    )

- [ ] A.[7,5,3,1]
- [ ] B.[1,3,5,7]
- [ ] C.[7]
- [ ] D.[]

#### [单项选择题083]

- Python 表达式[1,2,3]+[4,5,6]的值为（    ）

- [ ] A. 21
- [ ] B. [5, 7, 9]
- [ ] C. [1, 2, 3, 4, 5, 6]
- [ ] D.错误，两个 list 不可相加。

#### [单项选择题084]

- 有关下面 Python 代码说法错误的是（    ）

```python
a=(1,2)
a=(a[0]*2,a[1]*2)
```

- [ ] A. 第 2 行代码错误，tuple 类型不可被修改；
- [ ] B. 第 1 行代码如果没有外层圆括号，其效果相同；
- [ ] C. 第 2 行代码如果没有外层圆括号，其效果相同；
- [ ] D. 第 2 行代码没有语法错误。

#### [单项选择题085]

- 有关下面 Python 代码，说法正确的是（    ）。

```python
dictA = {"Apple": "苹果", "Cherry":"车厘子"}
dictA["Cherry"] = "樱桃"
```

- [ ] A. 第 2 行代码方括号内不能用字符串，必须为整数
- [ ] B. 第 2 行代码执行后，将新增一个成员，形如：`{"Apple": "苹果", "Cherry":"车厘子", "Cherry":"樱桃"}`
- [ ] C. 第 2 行代码执行后，车厘子将被修改为樱桃
- [ ] D. 第 2 行代码有语法错误

#### [单项选择题086]

- Python 表达式 divmod(8,6)的值是（   ）

- [ ] A.1
- [ ] B.2
- [ ] C.(1, 2)
- [ ] D.[1, 2]

#### [单项选择题087]

- 以下 Python 代码执行后的输出是（    ）

```python
poet=["李白","杜甫","王维"]
for i,v in enumerate(poet):
	print(i,v,sep=":",end="#")
```

- [ ] A．0:李白#1:杜甫#2:王维#
- [ ] B．0:李白:1:杜甫:2:王维#
- [ ] C．1:李白#2:杜甫#3:王维#
- [ ] D．1:李白:2:杜甫:3:王维#

#### [单项选择题088]

- 以下代码执行后的输出是（   ）

```python
lstA = [1,2,7,4,5]
lstA.sort(key = lambda x: x%2==0)
print(lstA)
```

- [ ] A．None
- [ ] B．[2, 4, 1, 7, 5]
- [ ] C．[1, 7, 5, 2, 4]
- [ ] D．[1, 2, 7, 4, 5]

#### [单项选择题089]

- 以下代码执行后的输出是（    ）

```python
lstA = [1,2,7,4,5]
sorted(lstA, key = lambda x: x%2==0)
print(lstA)
```

- [ ] A．None
- [ ] B．[2, 4, 1, 7, 5]
- [ ] C．[1, 7, 5, 2, 4]
- [ ] D．[1, 2, 7, 4, 5]

#### [单项选择题090]

- print(reversed([1,5,7,2]))的输出是（    ）

- [ ] A．[1,2,5,7]
- [ ] B．[7,5,2,1]
- [ ] C．[2,7,5,1]
- [ ] D．以上说法都不正确

#### [单项选择题091]

- 以下程序片段中 dictScore 是学生成绩，含有姓名及其对应的两科成绩，要实现按总计成绩升序，在横线处应填入代码是（    ）

```python
dictScore={"张三": (99, 88), "李思": (60, 99), "王武": (70, 70)}
sortedData = sorted(________)
print(sortedData)
```
- [ ] A. `dictScore`
- [ ] B. `dictScore,key=lambda x:x.value`
- [ ] C. `dictScore.items(),key=lambda x:x[1]`
- [ ] D. `dictScore.items(),key=lambda x:x[1][0]+x[1][1]`

#### [单项选择题092]

- 执行以下代码后，其输出是（    ）。

```python
lstA=[(100,90),(85,99),(85,90),(100,85)]
lstA.sort(key = lambda x:sum(x))
print(lstA)
```

- [ ] A. [(100, 90), (85, 99), (85, 90), (100, 85)]
- [ ] B. [(100, 90), (100, 85), (85, 99), (85, 90)]
- [ ] C. [(85, 90), (85, 99), (100, 85), (100, 90)]
- [ ] D.代码不能执行
#### [单项选择题093]

- 执行代码 `a, b = 5, 6; print(a or b)`打印出的结果是（    ）

- [ ] A．5
- [ ] B．6
- [ ] C．True
- [ ] D．False

#### [单项选择题094]

- 下面 Python 代码执行后输出是 (    )。

```python
lstA = [1, 2, 5, 6, 3, 7]
print(lstA.sort())
```

- [ ] A. [1, 2, 3, 5, 6, 7]
- [ ] B. [7, 6, 5, 3, 2, 1]
- [ ] C. [1, 2, 5, 6, 3, 7]
- [ ] D. None

#### [单项选择题095]

- 运行如下 Python 代码，其输出是（ ）

```python
a = (1, 2)
b = (3, 4)
a = a + b
print(a)
```

- [ ] A．1, 2
- [ ] B．(1, 2)
- [ ] C．(1, 2, 3, 4)
- [ ] D．1, 2, 3, 4

#### [单项选择题096]

- 运行如下 Python 代码，其输出是（    ）。

```python
a = [1, 2]
b = a
a.append(3)
print(a,b)
```

- [ ] A. [1, 2] [1, 2]
- [ ] B. [1, 2] [1, 2, 3]
- [ ] C. [1, 2, 3] [1, 2]
- [ ] D. [1, 2, 3] [1, 2, 3]

#### [单项选择题097]

- 如何删除列表list中的第一个元素？（    ）。

- [ ] A. list.remove(0)
- [ ] B. list.pop(0)
- [ ] C. list.delete(0)
- [ ] D. list.del(0)


#### [单项选择题098]

- 在Python中，如何创建一个空集合？（    ）

- [ ] A. new set()
- [ ] B. {}
- [ ] C. set()
- [ ] D. emptySet()

#### [单项选择题099]

- 下列哪个选项用于向列表list开头添加元素x？（    ）

- [ ] A. list.add(x)
- [ ] B. list.append(x)
- [ ] C. list.insert(0,x)
- [ ] D. list.extend(x)

#### [单项选择题100]

- Python是哪一类语言？（　　）

- [ ] A. 编译型语言
- [ ] B. 解释型语言
- [ ] C. 汇编语言
- [ ] D. 机器语言
