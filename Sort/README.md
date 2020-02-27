# Insertion sort:
It has the same time complexity as Bubble sort. The difference is, the first element is considered to be the sorted one. We take start to take the element from the second one to compare with all the elements which are ahead of the second one, if the second one is greater than that, then it find it spot, if not, it will be moved to forward. See the GIF below:
<img src="image/Insertion-sort-example-300px.gif" width="400" height="248" />

# Topological sort:
从 DAG 图中选择一个 没有前驱（即入度为0）的顶点并输出。
从图中删除该顶点和所有以它为起点的有向边。
重复 1 和 2 直到当前的 DAG 图为空或当前图中不存在无前驱的顶点为止。后一种情况说明有向图中必然存在环。

![topological_sort](https://github.com/XunOuyang/LeetCode/blob/master/Sort/image/topological_sort.jpg)

C++ implementation
graph is stored by adjacent table
```
#include<iostream>
#include <list>
#include <queue>
using namespace std;

/************************类声明************************/
class Graph
{
	int V;             // 顶点个数
	list<int> *adj;    // 邻接表
	queue<int> q;      // 维护一个入度为0的顶点的集合
	int* indegree;     // 记录每个顶点的入度
public:
	Graph(int V);                   // 构造函数
	~Graph();                       // 析构函数
	void addEdge(int v, int w);     // 添加边
	bool topological_sort();        // 拓扑排序
};

/************************类定义************************/
Graph::Graph(int V)
{
	this->V = V;
	adj = new list<int>[V];

	indegree = new int[V];  // 入度全部初始化为0
	for(int i=0; i<V; ++i)
		indegree[i] = 0;
}

Graph::~Graph()
{
	delete [] adj;
	delete [] indegree;
}

void Graph::addEdge(int v, int w)
{
	adj[v].push_back(w); 
	++indegree[w];
}

bool Graph::topological_sort()
{
	for(int i=0; i<V; ++i)
		if(indegree[i] == 0)
			q.push(i);         // 将所有入度为0的顶点入队

	int count = 0;             // 计数，记录当前已经输出的顶点数 
	while(!q.empty())
	{
		int v = q.front();      // 从队列中取出一个顶点
		q.pop();

		cout << v << " ";      // 输出该顶点
		++count;
		// 将所有v指向的顶点的入度减1，并将入度减为0的顶点入栈
		list<int>::iterator beg = adj[v].begin();
		for( ; beg!=adj[v].end(); ++beg)
			if(!(--indegree[*beg]))
				q.push(*beg);   // 若入度为0，则入栈
	}

	if(count < V)
		return false;           // 没有输出全部顶点，有向图中有回路
	else
		return true;            // 拓扑排序成功
}
```
