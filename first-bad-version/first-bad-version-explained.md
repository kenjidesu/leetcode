## [278. First Bad Version](https://leetcode.com/problems/first-bad-version/)

In this problem we have an API called `isBadVersion` which is a function that returns whether that version is a Bad Version (*returns False*, if not a Bad Version, otherwise *True*). So what we need to do is to find the **First Bad Version** of the product. *All the versions after a bad version are also bad*.

Let's do some visualization:

Supposed our first bad version is `4` and our `n = 5`. So if we passed all of the value in `isBadVersion` ranging from `1 - n` we will get `[False, False, False, True, True]`. The return value of the first three are `False` since they are not a Bad Version.

Basically, we just need to find the first `True`  of the return value of `isBadVersion`. It seems easy in small `n` but what if `n` is large, let's say millions. We can't just iterate to every number of range of `n`.

So In this problem we're going to use an Algorithm called **Binary Search**. It's an efficient algorithm for finding an item. It works by repeatedly dividing in half the portion of `n`, until you've narrowed down the possible locations to just one.

```python
low = 1   # leftmost value
high = n  # rightmost value
```

First, we need to get our leftmost value and rightmost value.

```python
mid = low + (high - low) // 2	# mid value of leftmost and rightmost value
```

And then, get the middle value of leftmost and rightmost value. Next, we need to know whether `mid` is higher or lower to the value we're finding.

```python
if isBadVersion(mid):	# this returns True if mid is too high for the first bad version
	res = mid		     # hold the mid as a result
	high = mid - 1     	 # we set high to mid - 1
else:	# if mid is too low to the first bad version
    low = mid + 1		# we set low as mid + 1
```

Basically, this If-else statement is just dividing the `n` to half repeatedly and tells whether `mid` is higher or lower to the First Bad Version. The loop is actually the one who can tell that the mid is the First Bad Version which is the reason why we have `res = mid` it is to save what is the last result that the If-else statement found inside the loop. If-else is just the worker of the loop. So how can the loop tell if `mid` is the First Bad Version?

```python
while low <= high:
```

This code tells us to stop if the `low` surpasses `high` which is not supposed to be happened. That's why we just return the `res` because that is the value that the if-else statement is pointing at.

In Conclusion, `mid` is just a guess and the `if-else` is a hint and the loop is the limited guesses which will lead you to the right value that your are trying to guess.





