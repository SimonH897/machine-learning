class Node:
	def __init__(self, pObject):
		self.content = pObject
		self.neighbour = None
		
	def setContent(self, pObject):
		self.content = pObject
		
	def setNext(self, pNext):
		self.neighbour = pNext
	
	def getNeighbour(self):
		return self.neighbour
	
	def getContent(self):
		return self.content
