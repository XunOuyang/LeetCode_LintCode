# 动态规划
我们如何判断一道题是不是该用DP？
动态规划大体上分两种：
1. top down。通常我们还说，top down with memorization。其实这是一种自上而下，记住遍历过的值的递归算法。
2. bottom up。有些书上说，这个才是真正意义上递归。又叫bottom up with tablutation. 


总结了一下dynamic programming的formula:
如何写出通用表达式呢：
可以这么做拿到题，比如
Edit Distance这道题：
这种类型的题，建立的matrix一定是 (m+1)(n+1)大小的：

举例：

string1 : HEAT

string2: HIT

先手写出dp矩阵的值，然后反过来根据值来写通用表达式
```
       H    E    A   T      
   0   0    1    2    3
H  0   0    1    2    3
I  1   1    2    3    4
T  2   2    3    4    3
```
那么就不难得出通用表达式了：
```
if str1[i] == str2[j]:
	dp[j+1][i+1] = min(dp[j][i],dp[j][i+1]+1,dp[j+1][i]+1 )
else:      
    dp[j+1][i+1] = min(dp[j][i+1]+1, dp[j+1][i]+1, dp[j][i]+2)     
```

又比如Leetcode 44 wildcard matching：

一模一样的解法。

第一步，解决一部分corner case:
```
if s == p:
	return True
if s == "" and p !="" or p == "":
    return False
container = set(s)
if len(p) - p.count("*") > len(s):
	return False
```

第二步，建立好矩阵以后，永远都是先给两条边分配值：
```
# 0th row:    
 for i in xrange(m):
	if p[0] == "*":
		dp[0][i+1] = True
	else:
		dp[0][i+1] = False

# 0th column:

for j in xrange(n):
	if p[j] == "*" :
		dp[j+1][0] = dp[j][0]
	else:
		dp[j+1][0] = False
```
同时列出所需要解答的矩阵，这道题真正的难点在于，如何cover所有的corner case：
例如下面这个的case：
s = "ho"
p = "*ho"
首先需要生成以下的基础matrix:                  最终的matrix 应该如下

	 s:       h    o                      s:       h    o  
	 p:  T    T    T                      p:  T    T    T
	 *   T    F    F                      *   T    T    T
	 *   T    F    F                      *   T    T    T
	 h   F    F    F                      h   F    T    F
	 o   F    F    F                      o   F    F    T

特别需要注意的地方是，这道题跟上一题的边不太一样。只要不是“”边就是F，为什么这样呢，因为我们可以把边看做是第0个字母，你不能用第0个字母去比较其他字母，因为第0个字母永远都是不存在的，所以不相等，即为F，但是是“”，可以等于empty character。

写出最终矩阵的formula是第三步了：
```
for i in xrange(m)
	for j in xrange(n):
		if p[j] == "?" or p[j] == s[i]:
			dp[j+1][i+1] = dp[j][i]
		elif p[j] == ""
			dp[j+1][i+1] = dp[j][i]|dp[j][i+1]|dp[j+1][i]
		else:
			dp[j+1][i+1] = False
```

下面再来看另外一道题：

leetcode 10: Regular Expressing Matching:


又碰到一道新题：

DP真的可以包含很多元的问题。尤其是很多时候不能一根死脑筋，画出矩阵一定是要么从0 到n ，要么从n到0。比如下面这一题：


leetcode 516:

Longest Palindromic Subsequence

这么一道题，如果那么想，就怎么也想不出来的。因为不是从起点（0,0）到终点（n-1, n-1）的关系：

dp[i , j] 表示的是，字符串s中，s[i:j+1] 中的最长的palindromic subsequence。

然后就不难想到fomula其实会是

if s[i] == s[j]:

    dp[i, j] = 2+ dp[i+1][j-1]

然后这道题目还可以拓展，降低空间复杂度。这道题还有意思的一点是，必须要从后往前遍历。仔细看看fomula，就明白为什么了。



DP的问题，构造出来了一个DP矩阵，有的时候不一定是从前往后，也可能有从后往前的情况。比如下面这么一道题：

leetcode 174 Dungeon game:

这道题目写了很多次。很多个cornercase都不好过。尤其是，要倒着往前想，推算出fomula是不容易的。很容易把自己弄糊。这道题，建立的矩阵，也不容(m+1)*(n+1)那么大。m*n就行。

那么来看看题目给的已知每一关的需要耗费的HP：

2    -3     3
-5    -10   1
10    30    -5


先确定最终点血量：max(1, 1
dungeon[-1][-1])  = 6

类似之前的题目一样。我们需要先建立矩阵的两条边，与之前的不一样的地方在于，这两条边是矩阵的下边和右边：
0      0      2
0      0      5
1      1      6   

两条边的公式应该为： dp[i][-1] = max( dp[i+1][-1] - dungeon[i][j], 1 )
```
dp[-1][i] = max( dp[-1][i+1] - dugeon[i][j] , 1)
```
推算完了两条边，这下就可以来思考中间块的值了：
```
dp[i][j] = min(dp[i+1][j], dp[i][ j+1] ) - dungeon[i][j]
if dp[i][j] < 1:
	dp[i][j] = 1
```


Palindrome 系列：
1143. Longest Common Subsequence
这道题是这系列里三个题最基本的：就是找两个string的共同子序列
还是按照模板，通解的formula也非常简单
```
def longestCommonSubsequence(self, text1, text2):
"""
:type text1: str
:type text2: str
:rtype: int
"""
m, n = len(text1), len(text2)
dp = [[0 for j in range(n+1)] for i in range(m+1)]
for i in range(m):
    for j in range(n):
	if text1[i] == text2[j]:
	    dp[i+1][j+1] = dp[i][j]+1
	else:
	    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
return dp[-1][-1]
```
把这道题拓展一点，就成了516. Longest Palindromic Subsequence，最长parlindromic 子序列。
也就相当于1143，但是把两个子序列，用s和s[::-1]替换了。解题思路和代码一模一样。

再拓展一点呢？就成了1312. Minimum Insertion Steps to Make a String Palindrome
这道题是要我们找，如何在一个string里面，添加最少的字母让它成为palindrome。那么也就意味着
如果我本来可以找出来这部分的程序中，已有的palindrome，那么剩余的自然而然也就是需要添加的部分。
同理，这道题的程序和接待也与1143一模一样了。


Array 连续累加问题： （特别需要注意这类题型的写法）
Leetcode 560
Leetcode 974
leetcode 325

Leetcode 1074
Leetcode 363
Are follow-ups, basically they extend this problem from 1 dimension to 2 dimension.

