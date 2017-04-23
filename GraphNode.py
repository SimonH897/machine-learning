class GraphNode:
	marked = False
	
	
	def init(self,pName):
		name = pName
		
	def mark(self):
		marked = True
	
	def unmark(self):
		marked = False
	
	def ismarked(self):
		return(marked)

	def getName():
		return name

n = GraphNode.init("tst")
