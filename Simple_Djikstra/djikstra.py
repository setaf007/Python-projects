
from collections import defaultdict 


locationDict = {"Tuas":0, "Jurong":1, "Bukit Batok":2, "Chua Chu Kang":3, "Clementi":4, "Pasir Panjang":5,
"Sentosa":6, "Queenstown":7, "Bukit Timah":8, "Bukit Panjang":9, "Mandai":10, "Woodlands":11, "Sembawang":12,
"Nee Soon":13, "Ang Mo Kio":14, "Serangoon":15, "Upper Thomson":16, "Tanjong Pagar":17, "Marina Bay":18,
"Outram":19, "Punggol":20, "Changi":21, "Bedok":22, "Tampines":23}

class Graph: 

	def minDistance(self,dist,queue): 
		minimum = float("Inf") 
		min_index = -1
		
		for i in range(len(dist)): 
			if dist[i] < minimum and i in queue: 
				minimum = dist[i] 
				min_index = i 
		return min_index 

	def printPath(self, parent, j): 
		if parent[j] == -1: 
			print ("%s  " % list(locationDict.keys())[list(locationDict.values()).index(j)], end= " ")
			return
		self.printPath(parent , parent[j])
		print ("%s  " % list(locationDict.keys())[list(locationDict.values()).index(j)], end= " ") 
		
	def printSolution(self, dist, parent, src, end): 
		print("\nStart from: %s \nTo: %s \nTotal Distance: %d km\nPath:" % (list(locationDict.keys())[list(locationDict.values()).index(src)], list(locationDict.keys())[list(locationDict.values()).index(end)], dist[end]))
		self.printPath(parent,end) 

	def dijkstra(self, graph, src): 

		row = len(graph) 
		col = len(graph[0]) 
		dist = [float("Inf")] * row 
		parent = [-1] * row 
		dist[src] = 0
		queue = [] 
		for i in range(row): 
			queue.append(i) 
			 
		while queue: 
			u = self.minDistance(dist,queue) 
			queue.remove(u) 
			for i in range(col): 
				if graph[u][i] and i in queue: 
					if dist[u] + graph[u][i] < dist[i]: 
						dist[i] = dist[u] + graph[u][i] 
						parent[i] = u 

		self.printSolution(dist,parent, src, end) 

g= Graph() 

graph = [
    [0,19,16,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [19,0,19,22,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [16,19,0,6,7,0,0,0,5,7,0,0,0,0,18,0,0,0,0,0,0,0,0,0],
    [15,22,6,0,0,0,0,0,0,4,0,11,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,7,0,0,7,0,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,7,0,8,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,8,0,10,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0],
    [0,0,0,0,5,6,10,0,9,0,0,0,0,0,0,0,10,9,0,5,0,0,0,0],
    [0,25,5,0,5,0,0,9,0,6,0,0,0,0,0,0,11,10,0,0,0,0,22,0],
    [0,0,7,4,0,0,0,0,6,0,15,11,0,16,16,0,14,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,15,0,8,6,3,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,11,0,0,0,0,0,11,8,0,5,9,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,6,5,0,5,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,16,3,9,5,0,6,0,0,0,0,0,0,0,0,0],
    [0,0,18,0,0,0,0,0,0,16,0,0,0,6,0,6,5,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,8,6,0,0,8,16,0,12],
    [0,0,0,0,0,0,0,10,11,14,0,0,0,0,5,8,0,6,0,0,0,0,16,0],
    [0,0,0,0,0,0,0,9,10,0,0,0,0,0,0,6,6,0,10,8,0,18,13,15],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,0,2,0,0,16,0],
    [0,0,0,0,0,0,6,5,0,0,0,0,0,0,0,0,0,8,2,0,0,0,16,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,0,18,0,0,0,0,0,5],
    [0,0,0,0,0,0,0,0,22,0,0,0,0,0,0,0,16,13,16,16,0,0,0,5],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,12,0,15,0,0,0,5,5,0]]




src = input("Choose starting point: ")
if src in locationDict:
	src = locationDict[src]
	end = input("Choose target destination: ")
	if end in locationDict:
		end = locationDict[end]
	else:
		print("Invalid location")
		k=input("\nPress enter to exit")

else:
	print("Invalid location")
	k=input("\nPress enter to exit")

g.dijkstra(graph,src) 

k=input("\n\nPress enter to exit")