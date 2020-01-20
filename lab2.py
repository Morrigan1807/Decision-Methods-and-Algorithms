def Dijkstra(N, S, matrix):
	valid = [True]*N        
	weight = [1000000]*N
	weight[S] = 0
	for i in range(N):
		min_weight = 1000001
		ID_min_weight = -1
		for i in range(len(weight)):
			if valid[i] and weight[i] < min_weight:
				min_weight = weight[i]
				ID_min_weight = i
		for i in range(N):
			if weight[ID_min_weight] + matrix[ID_min_weight][i] < weight[i]:
				weight[i] = weight[ID_min_weight] + matrix[ID_min_weight][i]
		valid[ID_min_weight] = False
	return weight


dist =[[1000000 for i in range(9)] for i in range(9)]
dist[0][1] = 6
dist[0][4] = 11
dist[0][5] = 10
dist[0][7] = 14
dist[1][2] = 3
dist[1][4] = 6
dist[5][4] = 10
dist[5][6] = 16
dist[5][7] = 2
dist[2][3] = 16
dist[2][4] = 8
dist[3][8] = 6
dist[4][3] = 12
dist[4][6] = 10
dist[6][3] = 12
dist[6][8] = 6
dist[7][6] = 16
dist[7][8] = 20
print("Array of distances: ", dist)
result = []
result = Dijkstra(9, 0, dist)
        
print("Solution: ", result)
