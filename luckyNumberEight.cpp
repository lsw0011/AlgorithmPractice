//============================================================================
// Name        : luckyNumberEight.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string.h>

using namespace std;
const int MAX = 200000;
char test[MAX] = {};
int dp[MAX][8];
bool traveled[MAX][8];
int len;
int mod = 1e+9 + 7;
void solve(int pos, int rem){
	int nextRem = (rem * 10 + test[pos]) % 8;
	if(nextRem == 0){
		dp[pos][rem]++;
	}
	if(pos == len - 1){
		return;
	}
	if(!traveled[pos + 1][nextRem]){
		traveled[pos + 1][nextRem] = true;
		solve(pos + 1, nextRem);
	}
	dp[pos][rem]%=mod;
	dp[pos + 1][nextRem]%=mod;
	dp[pos][rem] += dp[pos + 1][nextRem];
	if(!traveled[pos+1][rem]){
		traveled[pos+1][rem] = true;
		solve(pos + 1, rem);
	}
	dp[pos][rem]%=mod;
	dp[pos + 1][rem]%=mod;
	dp[pos][rem] += dp[pos + 1][rem];
}


int main() {
	cin >> len;
	cin >> test;
	memset(traveled, false, MAX*8);
	memset(dp, 0, MAX*8);
	solve(0,0);
	cout << dp[0][0] << endl;
	return 0;
}
