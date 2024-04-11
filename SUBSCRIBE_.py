# Code By D3vil

# PROBLEM CODE :- SUBSCRIBE_
'''
A new TV streaming service was recently started in Chefland called the Chef-TV.

A group of 
�
N friends in Chefland want to buy Chef-TV subscriptions. We know that 
6
6 people can share one Chef-TV subscription. Also, the cost of one Chef-TV subscription is 
�
X rupees. Determine the minimum total cost that the group of 
�
N friends will incur so that everyone in the group is able to use Chef-TV.

Input Format
The first line contains a single integer 
�
T — the number of test cases. Then the test cases follow.
The first and only line of each test case contains two integers 
�
N and 
�
X — the size of the group of friends and the cost of one subscription.
Output Format
For each test case, output the minimum total cost that the group will incur so that everyone in the group is able to use Chef-TV.

Constraints
1
≤
�
≤
1000
1≤T≤1000
1
≤
�
≤
100
1≤N≤100
1
≤
�
≤
1000
1≤X≤1000
Sample 1:
Input
Output
3
1 100
12 250
16 135
100
500
405
Explanation:
Test case 1: There is only one person in the group. Therefore he will have to buy 
1
1 subscription. Therefore the total cost incurred is 
100
100.
Test case 2: There are 
12
12 people in the group. Therefore they will have to buy 
2
2 subscriptions. Therefore the total cost incurred is 
500
500.
Test case 3: There are 
16
16 people in the group. Therefore they will have to buy 
3
3 subscriptions. Therefore the total cost incurred is 
405
405
'''
# cook your dish here
t = int(input())
for i in range(t):
    n,x = map(int, input().split())
    r = n // 6
    if ( n % 6 != 0):
        t = ( r + 1 ) * x
        print(t)
    else:
        t = r * x
        print(t)