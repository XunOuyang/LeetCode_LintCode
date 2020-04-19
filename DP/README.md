# 动态规划

动态规划的题型很多。其解题思想，就是利用历史记录，来避免重复计算。而历史记录，我们则可以用一维或者二维甚至三维的数组来保存。（迄今还没有碰到过四维动态规划的题目）。
不管是维度是多少，终究逃不过解决问题的三个步骤：
1. 定义DP，究竟是选择一维呢，还是二维呢还是三维呢？如果是一维，那么DP里面的每一个元素又分别代表什么含义呢？
2. 找出递推式，也就是formula，我们需要知道dp[i]  与 dp[i-1] 的关系，或者 dp[i][j] 与 dp[i-1][j-1]的关系。这也是动态规划里面最难的一个步骤。
3. 初始化DP, 几乎任何时候，在我们能够用循环嵌套第二步骤里面的公式来推算出所有的dp 矩阵里面的值的时候，我们需要先对dp矩阵里面某一个或者某一些值进行初始化。这一点的思想，跟数学里面的数学归纳法是一样的。

来看一个例子：
The rod-cutting problem（分杆问题）是动态规划问题的一个典例。

给出一根长度为n（n为整数）的杆，可以将杆切割为任意份长短不同的杆（其中包含完全不进行切割的情况），每一份的长度都为整数。给出一个整数数组nums，nums[i]表示长度为i的杆的价格，问如何对杆进行切割可以使利润最大。
数组的一个示例如下：

![road_cutting](https://github.com/XunOuyang/LeetCode/blob/master/DP/image/road_cutting.png)

在长度为n的杆上进行整数切割，共有2n-1种情况，因为有n-1个点可以选择是否切割。
将这些可以切割的点编号为1,2,3, ..., n-1，如果先试着在1处切割，则杆变成了长度为1和n-1的两段；如果试着在2处切割，则杆变为了长度为2和n-2的两段，以此类推，共有n种切法（包含完全不作切割）。这样，我们迈出了递归的第一步，即把长为n的杆的最优切割分成两个子问题：长为i的杆的最优切割和长为n-i的杆的最优切割（i = 1,2,...,n）。最终的利润为两个子杆的利润和。
如果用fn表示长度为n的杆切割后能得到的最大利润，经过以上分析，我们求取两个子杆的利润和的最大值即可。即
fn = max(pn, f1 + fn-1, f2 + fn-2, ..., fn-1 + f1).
这种思路是正确的，但不是太好，有心人可以注意到子问题之间有较大的重叠之处，比如计算fn-1时会需要查看f1 + fn-2，即f1 + fn-1这个子问题需要查看f1 + f1 + fn-2这个切法；而计算f2时又需要查看f1 + f1，即f2 + fn-2这个子问题也会查看到f1 + f1 + fn-2这个切法，相当于把一些可能性重复查看了多遍。
一个更简洁合理的思路是：设定左边这个长为ｉ的杆不可再切割，只有右边长为n-i的杆可以再切割。则问题变为
fn = max(pi + fn-i), i = 1,2,...,n
这题用递归就能解
```
def cutroad(n, nums):
    if n == 0:
        return 0
    res = 0
    for i in range(1, n+1):
        res = max(res, nums[i]+cutroad(n-i, nums))
    return res
```
时间复杂度则为O(2^n)
在节点n，算法的时间复杂度为
Tn = 1 + ∑ Ti (i = 0,1, ..., n-1)
(其中的1是在节点处做加法和max运算的常数复杂度)
这个式子很好推算，只要将Ti的值以此从后往前代入即可：

Tn = 1+T0+T1+ ... +Tn-1 　　　　 　 = 1+T0+T1+ ... +Tn-2+(1+T0+T1+ ... +Tn-2)

　　 = 2 (1+T0+T1+ ... +Tn-2)　 　=  2 (1+T0+T1+ ... +Tn-3+(1+T0+T1+ ... +Tn-3))

　　 = 22 (1+T0+T1+ ... +Tn-3)　  =  ... （总结规律） = 2n-1 (1 + T0)

　　 = 2n

即传统递归算法的时间复杂度为O(2^n)，为指数级别。
优化
以n = 4为例，画出递归树结构（节点包含的数字为n的值）

![recursion_tree](https://github.com/XunOuyang/LeetCode/blob/master/DP/image/recursion_tree.png)

## top-down with memoization
top-down方法比较容易理解，就是在传统递归的基础上加入memoization（注意与memorization的区别。memoization来自memo，有备忘的意思），即用数组或表等结构缓存计算结果。在每次递归运算时，先判断想要的结果是否在缓存中，如果没有才进行运算并存入缓存。
```
class Solution:
    def cutroad(self, n, nums):
        self.dp = [-1]*(len(nums)+1)
        self.dp[0] = 0
        self.run(n, nums, self.dp)
        print(self.dp)
        return self.dp[n]
        
    def run(self, n, nums, dp):
        if dp[n] != -1:
            return dp[n]
        if n == 0:
            return 0 
        res = 0
        for i in range(1, len(nums)+1):
            res = max(res, nums[i]+self.run(n-i, nums, self.dp))
        self.dp[n] = res
        return res
```
## bottom up with tabulation
bottom-up with tabulation
相比于top-down，bottom-up的特点是使用循环而非递归，先解决子问题，再利用子问题的答案解决父问题。tabulation也很好理解，即用一个表格存放子问题的答案，然后查表获得父问题需要的所有信息去解决父问题，解决后也填在表中，直至把表填满。

事实上，dynamic programming这个令人费解的名字即来源于此。programming在数学界有“列表法”(tabular method)的意思，指的是为了求某函数的最大/最小值，将函数的所有变量的所有可能值列在表中并对表进行某些操作来获得结果。在这里，表格是“静态”的，每个格子中的信息是独立的；而在动态规划中，表格是“动态”的，一些格子中的信息依赖于另一些格子中的计算答案。所以，dynamic programming也可以理解为“动态列表法”，也即此处的tabulation。有些书上说，这个才是真正意义上递归。

动态规划是一种“以空间换时间”的思想，适用于子问题之间存在重叠情况的优化问题。它的基本思想是将计算过的子问题的答案记录下来，从而达到每个子问题只计算一次的目的。

动态规划的实现方法分为top-down和bottom-up两种，可以理解为前者从递归树的根节点向下递归调用，而后者从树的叶结点开始不停地向上循环。

所以呢？
总结就一句话，dyanmic programming里面，用recursive方法的，就是top down，用iterative方法做的，就是bottom up。
最后，其实上述例子一直是有问题的，当n > len(nums)，就报错了。也不知道为何书上都喜欢用这个例子。


# 模板
## 二维数组系列
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
if word1[i] == word2[j]:
    dp[i+1][j+1] = dp[i][j]
else:
    # dp[i+1][j] -- remove a letter from word2
    # dp[i][j+1] -- remove a ltter from word1
    # dp[i][j] -- replace the letter
    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1
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


## Palindrome 系列：
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


## Array 连续累加问题： （特别需要注意这类题型的写法）
Leetcode 560
Leetcode 974
leetcode 325

Leetcode 1074
Leetcode 363
523. Continuous Subarray Sum
Are follow-ups, basically they extend this problem from 1 dimension to 2 dimension.

## 两个string字母重复问题：
1143. Longest Common Subsequence
1035. Uncrossed Lines
583. Delete Operation for Two Strings
712. Minimum ASCII Delete Sum for Two Strings
718. Maximum Length of Repeated Subarray
