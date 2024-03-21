# Problem Name = Greater Average
# Problem ID = AVGPROBLEM
# Problem Link = https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/AVGPROBLEM

# Author = Shubham Raj
# Date = 21/03/202
# Time = 17:50

# Solution

t = int(input())
for i in range(t):
    a,b,c = map(int, input().split())
    if (a+b)/2 > c:
        print("YES")
    else:
        print("NO")