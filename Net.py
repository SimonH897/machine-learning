class Net:
	
	def __init__(self, name):
		self.name = name 
	
	def addNode(self, GraphNode, pNode):
		node = GraphNode(pNode)
