#include <iostream>
#include <vector>

using namespace std;

const int MAX = 1e+9;
int dp[1001][1001];
vector<int> qStart;
vector<int> qEnd;

int solve(int m, int n){

	for(int q = 2; q <= n; q++){
		for(int c = 1; c <= m; c++){
			dp[q][c] = MAX;
		}
	}

	for(int c = 1; c <= m; c++){
		dp[1][c] = abs(qStart[0] - qEnd[0]);
	}

	for(int q = 2; q <= n; q++){
		for(int c = 1; c <= m; c++){
			dp[q][qEnd[q-2]] = min(dp[q][qEnd[q-2]], dp[q-1][c] + abs(c - qStart[q-1])+abs(qEnd[q-1] - qStart[q-1]));
			dp[q][c] = min(dp[q][c], dp[q-1][c] + abs(qEnd[q-2] - qStart[q-1]) + abs(qEnd[q-1] - qStart[q-1]));

		}
		if(q == n){
			int sol = MAX;
			for(int c = 1; c <= m; c++){
				if(sol > dp[q][c]){
					sol = dp[q][c];
				}
			}
			return sol;
		}
	}
	return abs(qStart[0] - qEnd[0]);
}

int main() {
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		int m, n;
		cin >> m >> n;
		for(int j = 0; j < n; j++){
			int start, end;
			cin >> start >> end;
			qStart.push_back(start);
			qEnd.push_back(end);
		}
		cout << solve(m, n) << endl;
		qStart.clear();
		qEnd.clear();
	}
}
