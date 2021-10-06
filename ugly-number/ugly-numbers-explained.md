## 263. [Ugly Number](https://leetcode.com/problems/ugly-number/)

`if n < 1: return False`

In the Description, it says there that the **Ugly number** is a **POSITIVE INTEGER**. So, In order for us to know whether the *n* is positive, we need to check if it's less than to 1, why not `n < 0`? Well, that would work too since **zero is neither positive nor negative**, it's a neutral number.

And In this problem, it also says there that the **Ugly number's** prime factors are limited to `2`, `3`, and `5`. So how can we know if the *n*'s prime factors are limited to `2`, `3`, `5`?.

We are going to use the **Modulo Operation (%)**. The *Modulo Operation* gets the remainder of the *n*. So why do we need to get the remainder of *n*? Well, to find the prime numbers we need to know whether the result of *n* divided by the prime numbers is a whole number. So if we try dividing *n* by the prime factors `2`, `3`, and `5` and we got a whole number that means *n* is divisible by that prime factor if we got the result of 1.

```python
while n % 2 == 0: n /= 2
while n % 3 == 0: n /= 3
while n % 5 == 0: n /= 5
```

In this code, we are checking if *n* is divisible by the prime factors `2`, `3`, and `5`. But why do we update *n*?. We update *n* to get the lowest value of *n* divided by the given prime factors. How can we know if it's divisible by this prime factors? Well, If we divided the lowest value of *n* by the prime factors that is divisible to it, we will get the value of 1. And if the value is not 1, that means *n* is not divisible by this given prime factors.

![263uglynumber](/img/263uglynumber.PNG)

To finish things up, we just need to know if *n* is equal to 1. And if it's 1 then it's an Ugly Number because It is divisible by this all given prime factors, otherwise it's not an Ugly number.

`return n == 1`



