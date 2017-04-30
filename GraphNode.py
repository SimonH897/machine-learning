class GraphNode:
	marked = False
	
	def __init__(self,pName):
		self.name = pName
		
	def mark(self):
		self.marked = True
	
	def unmark(self):
		self.marked = False
	
	def isMarked(self):
		return(self.marked)

	def getName(self):
		return self.name
		
	#def addEdge(self, neighbour, 
