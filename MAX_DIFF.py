# Code By D3vil

# PROBLEM CODE :- MAX_DIFF

'''
Chef prepared two dishes yesterday. Chef had assigned the tastiness T1 and T2 to the first and to the second dish respectively. The tastiness of the dishes can be any integer between 0 and N (both inclusive).

Unfortunately, Chef has forgotten the values of T1 and T2 that he had assigned to the dishes. However, he remembers the sum of the tastiness of both the dishes - denoted by S.

Chef wonders, what can be the maximum possible absolute difference between the tastiness of the two dishes. Can you help the Chef in finding the maximum absolute difference?

It is guaranteed that at least one pair {T1,T2} exist such that T1+T2=S,0≤T1,T2≤N.

Input Format
The first line of input contains a single integer T, denoting the number of testcases. The description of the T testcases follows.
The first and only line of each test case contains two space-separated integers N, S, denoting the maximum tastiness and the sum of tastiness of the two dishes, respectively.
Output Format
For each testcase, output a single line containing the maximum absolute difference between the tastiness of the two dishes.

Constraints
1≤T≤103
1≤N≤105
1≤S≤2⋅105
Sample Input 1 
3
3 1
4 4
2 3
Sample Output 1 
1
4
1
Explanation
Test Case 1: The possible pairs of {T1,T2} are {0,1} and {1,0}. Difference in both the cases is 1, hence the maximum possible absolute difference is 1.

Test Case 2: The possible pairs of {T1,T2} are {0,4}, {1,3}, {2,2}, {3,1} and {4,0}. The maximum possible absolute difference is 4.

Test Case 3: The possible pairs of {T1,T2} are {1,2} and {2,1}. Difference in both the cases is 1, and hence the maximum possible absolute difference is 1.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

# Code in Python


t=int(input())
i=1
for i in range(t):
    n,s=map(int,input().split())
    if(s<=n):
        # take {0,s}
        print(s)
    else:
        print(2*n-s)


# Code in CPP

#include <iostream>
'''
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int n,s;
	    cin>>n>>s;
	    if(s<=n){
	        // take {0,s}
	        cout<<s<<endl;
	    }
	    else{
	        // n = 7, S = 10
	        // take {s-n,n}
	        // take {s-n+1, n-1}
	        cout<<n * 2 - s<<endl;
	    }
	}
	return 0;
}
'''