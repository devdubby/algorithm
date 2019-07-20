#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

#define MAX 1000

using namespace std;

vector<int> a[MAX];
bool visit1[MAX];
bool visit2[MAX];

void bfs(int start) {
	queue<int> q;
	q.push(start);
	visit1[start] = true;

	while (!q.empty()) {
		int x = q.front();
		q.pop();
		cout << x << " ";

		for (int i = 0; i < a[x].size(); i++) {
			int y = a[x][i];
			if (visit1[y] == false) {
				q.push(y);
				visit1[y] = true;
			}
		}
	}
}

void dfs(int start) {
	visit2[start] = true;
	cout << start << " ";

	for (int i = 0; i < a[start].size(); i++) {
		int next = a[start][i];
		if (visit2[next] == false) {
			dfs(next);
		}
	}
}

int main() {
	int node, line, start, n, m;
	cin >> node >> line >> start;

	for (int i = 0; i < line; i++) {
		cin >> n >> m;
		a[n].push_back(m);
		a[m].push_back(n);
	}

	//인접리스트 오름차순 sort하여 작은것부터 방문하도록
	for (int i = 1; i <= node; i++) {
		sort(a[i].begin(), a[i].end());
	}

	dfs(start);
	cout << "\n";
	bfs(start);

	return 0;
}