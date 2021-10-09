## [292.Nim Game](https://leetcode.com/problems/nim-game/)

In this problem we are playing a Nim game with a friend. You and your friend will alternate taking turns, and we go first. On each turn, the person whose turn will remove 1 to 3 stones from the heap. The one who removes the last stone is the winner.

```python
return n % 4 != 0
```

 Now why does this work? Well, our max of getting stones is 3 and basically if *n* is less than or equal to 3 we will always win. But what about 4? If `n = 4` there's no way we can win the game since the max stone is 3 and we are the one who needs to go first. If we get 1 stone, our friend will get 3 stones and wins the game, same if we get 2 or 3 stones, our friend is still gonna win. 

So in the description, it says there that `return True` if we can win the game. So that means if there's a 1% percent chance of winning to that game we will `return True` but if there's no way we can win the game, we will `return False`. And we saw that if `n = 4` there's no way we can win the game.

The trick on winning this game is putting your friend in the place of *n* that is divisible by 4. So we will have the chance of winning that game. Now we know that if *n* is divisible by 4, we will lose the game. So we can just check if *n* is divisible by 4 that means we can't win and we will return `False`, otherwise `True`.

```
1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20
W	W	W	L	W	W	W	L	W	W	W	L	W	W	W	L	W	W	W	L
```



