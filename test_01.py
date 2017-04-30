import numpy as np
import ttt as t
from GraphNode import GraphNode
from List import List


#zahlen = [[0,15,-15],[15,0,-15],[15,0,-15]]
#np.savetxt("zahlen.txt",zahlen)

#zahlenIn = np.loadtxt("zahlen.txt")
#print(zahlenIn)


n = GraphNode("GraphNode1")
o = GraphNode("GraphNode2")

#n.test("test")
#print(n.getName())

l = List("testListe")
l.append("Object1")
l.append("Object2")
l.append("Object3")
l.toFirst()
l.gotoNext()

print("Empty: " + str(l.isEmpty()))
print("Access: " + str(l.hasAccess()))
print(str(l.getObject()))

