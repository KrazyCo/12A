global tree 
tree = [[4,  "Alex", 1],        # 0
        [2,  "Will", -1],       # 1
        [-1, "Andreas", 3],     # 2
        [5,  "Musashi", -1],    # 3
        [6,  "Alesandro", -1],  # 4
        [7,  "Matvey", -1],     # 5
        [-1, "Aiden", -1],      # 6
        [8,  "Luke", -1],       # 7
        [9,  "Felix", -1],      # 8 
        [10, "Conor", -1],      # 9
        [-1, "Arun", -1]]       # 10
startNode = 0

# procedural
# in-order proceduarl
def inOrderTraversalProcedural(currentNode):
    if tree[currentNode][0] != -1:
        inOrderTraversalProcedural(tree[currentNode][0])
    print(tree[currentNode][1])
    if tree[currentNode][2] != -1:
        inOrderTraversalProcedural(tree[currentNode][2])

# pre-order procedural
def preOrderTraversalProcedural(currentNode):
    print(tree[currentNode][1])
    if tree[currentNode][0] != -1:
        preOrderTraversalProcedural(tree[currentNode][0])
    if tree[currentNode][2] != -1:
        preOrderTraversalProcedural(tree[currentNode][2])

# post-order procedural
def postOrderTraversalProcedural(currentNode):
    if tree[currentNode][0] != -1:
        postOrderTraversalProcedural(tree[currentNode][0])
    if tree[currentNode][2] != -1:
        postOrderTraversalProcedural(tree[currentNode][2])
    print(tree[currentNode][1])

print("In-order procedural")
inOrderTraversalProcedural(0)

print("\nPre-order procedural")
preOrderTraversalProcedural(0)

print("\nPost-order procedural")
postOrderTraversalProcedural(0)
print("h")
# object oriented
class Node:
	def __init__(self, name):
		self.__name = name
	
	def setLeft(self, left):
		self.__left = left

	def setRight(self, right):
		self.__right = right

	def getLeft(self):
		return self.__left

	def getRight(self):
		return self.__right

	def getName(self):
		return self.__name

oopTree = []

for i in range(len(tree)):
	oopTree.append(Node(tree[i][1]))

for i in range(len(tree)):
	if tree[i][0] != -1:
		oopTree[i].setLeft(oopTree[tree[i][0]])
	if tree[i][2] != -1:
		oopTree[i].setRight(oopTree[tree[i][2]])

def inOrderOOP(currentNode):
	if currentNode.getLeft():
		inOrderOOP(currentNode.getLeft())
	print(currentNode.getName())
	if currentNode.getRight():
		inOrderOOP(currentNode.getRight())
# print("what")
# print(oopTree[0].getLeft().getName())
# print(oopTree[10].getLeft().getName())

inOrderOOP(oopTree[startNode])