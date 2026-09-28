---
tags:
  - math
Category:
  - 笔记
---
## Peano Axiom

**Axiom 2.1**
0 is a natural number.

**Axiom 2.2**
If n is a natural number, then n++ is also a natural number.

**Axiom 2.3**
0 is not the succesor of any natural number.

**Axiom 2.4**
Diffrent natural numbers must have differrent successors; i.e., if n, m are natural numbers and n $\neq$ m, then n++ $\neq$ m++.

**Axiom 2.5**
Let P(n) be any property pertraining to a natural number n. Suppose that P(0) is true, and suppose that whenever P(n) is true, P(n++) is also true. Then P(n) is true for every natural number n.

## Addition

**Definition 2.2.1** 
Addition of natural numbers
- m is a natural number, define 0+m=m
- define (n++)+m=(n+m)++

<mark style="background: #FFB86CA6;">Lemma 2.2.2</mark>
For any natural number n, n+0=n

proof:
假设n+0=n，证明(n++)+0=n++
由于(n++)+0=(n+0)++=n++
即证

<mark style="background: #FFB86CA6;">Lemma 2.2.3</mark>
For any natural numbers n and m, n+(m++)=(n+m)++

proof:
对n使用归纳，当n=0时，0+(m++)=m++，0+m=m，所以0+(m++)=(0+m)++
假设n满足n+(m++)=(n+m)++，只需证(n++)+(m++)=((n++)+m)++
由于(n++)+(m++)=(n+(m++))++=((n+m)++)++=((n++)+m)++
即证

<mark style="background: #BBFABBA6;">Proposition 2.2.4</mark>
(Addition is commutative)
For any natural numbers n and m, n+m=m+n

proof:
对n使用归纳法，当n=0时，0+m=m=m+0
假设n+m=m+n
只需证(n++)+m=m+(n++)
由定义：(n++)+m=(n+m)++
由Lemma 2.2.3：m+(n++)=(m+n)++
由假设：(n+m)++=(m+n)++
即证

<mark style="background: #BBFABBA6;">Proposition 2.2.5</mark>
(Addition is associative)
For any natural numbers a, b, c, we have (a+b)+c=a+(b+c).

proof：
对a使用归纳法，当a=0时，(0+b)+c=b+c，0+(b+c)=b+c
假设(a+b)+c=a+(b+c)
证明((a++)+b)+c=(a++)+(b+c)
左=((a+b)++)+c=((a+b)+c)++
右=(a++)+(b+c)=(a+(b+c))++
又因为假设：(a+b)+c=a+(b+c)
即证

<mark style="background: #BBFABBA6;">Proposition 2.2.6</mark>
(Cancellation law)
Let a, b, c be natural numbers such that a+b=a+c. Then we have b=c.

proof:
对a使用归纳法，当a=0时，0+b=b=0+c=c，所以b=c
假设a+b=a+c可以推出b=c
只需证(a++)+b=(a++)+可以推出b=c
左=(a+b)++
右=(a+c)++
左=右可以推出a+b=a+c，进一步可以推出b=c
即证

**Definition 2.2.7**
(Positive natural numbers)
A natural number n is said to be positive iff it is not equal to 0.

<mark style="background: #BBFABBA6;">Proposition 2.2.8</mark>
If a is positive and b is a natural number, then a+b is positive (and hence b+a is also, by Proposition 2.2.4)

proof:
对b使用归纳法，当b=0时，a+0=a是正数
假设b=n时a+n是一个正数
只需证a+(n++)是一个正数
由于a+(n++)=(a+n)++，0不能是任何数的后继
所以(a+n)++不等于0
即证