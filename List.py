from Node import Node
class List:
	
	current = None
	def __init__(self, pName):
		self.name = pName
		self.tail = Node(None)
		self.first = self.tail
		self.tail.setNext(self.tail)
		self.current = self.first
		
	def isEmpty(self):
		return (self.first == self.tail)
	
	def hasAccess(self):
		return ((not self.isEmpty()) and self.current != self.tail)
	
	def gotoNext(self):
		if(self.hasAccess()):
			self.current = (self.current).getNeighbour()
			
	def toFirst(self):
		if(not self.isEmpty()):
			self.current = self.first

	def toLast(self):
		if(not self.isEmpty()):
			self.current = self.tail.getNeighbour()
			
	def getObject(self):
		if(self.hasAccess()):
			return (self.current).getContent()
		else:
			return None
			
	def setObject(self, pObject):
		if(pObject != None and self.hasAccess()):
			current.setContent(pObject)

	def append(self, pObject):
		if(pObject != None):
			lNewNode = Node(pObject)
			lPos0 = self.current 
			lNewNode.setNext(self.tail)
			if(self.isEmpty()):
				self.first = lNewNode
			else:
				lPrevious = self.tail.getNeighbour()
				lPrevious.setNext(lNewNode)
			self.tail.setNext(lNewNode)
			self.current = lPos0    

	def insert(self, pObject):
		if(pObject != None):
			
			if(self.isEmpty()):
				self.append(pObject)
			else:
				if(self.hasAccess()):
					lPos = self.current
					lNewNode = Node(pObject)
					lNewNode.setNext(self.current)
					if(lPos == self.first):
						first = lNewNode
					else:
						self.toFirst()
						lFront = self.current
						while(self.hasAccess() and not(self.current == lPos)):
							lFront = self.current
							self.gotoNext()
						lFront.setNext(lNewNode)
				self.current = lPos

	#def concat
	
	def remove(self):
		if(self.hasAccess()):
			if(self.current == self.first):
				self.first = self.current.getNeighbour()
				if(self.current.getNeighbour() == self.tail):
					self.tail.setNext(self.first)
				self.current = self.first
			else:
				lPos = self.current
				self.toFirst()
				lFront = self.current
				while(self.hasAccess() and not(self.current == lPos)):
					lFront = self.current
					self.gotoNext()
				lFront.setNext(lPos.getNeighbour())
				self.current = lFront.getNeighbour()
				if(self.current == self.tail):
					self.tail.setNext(lFront)


			
