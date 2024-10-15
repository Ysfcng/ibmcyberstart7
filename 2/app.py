import math
points=[[2,1],[3,5]]
def euclideanDistance(arr):
	sol=0
	for x in arr:
		print(x,x[1]-x[0])	
		sol+=math.pow(x[1]-x[0],2)
	return math.sqrt(sol)
print(euclideanDistance(points))
