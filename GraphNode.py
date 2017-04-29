class GraphNode:
	marked = False
	
	def __init__(self,pName):
		self.name = pName
		
	def mark(self):
		marked = True
	
	def unmark(self):
		marked = False
	
	def ismarked(self):
		return(marked)

	def getName(self):
		return self.name
		
	#def addEdge(self, neighbour, 
