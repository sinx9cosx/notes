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

**Definition 2.2.1** Addition of natural numbers
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
由于(n++)+(m++)=(n+(m++))++=((n+m)++)++