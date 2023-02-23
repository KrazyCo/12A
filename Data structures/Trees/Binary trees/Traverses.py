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
    oopTree[i].setLeft(oopTree[tree[i][0]] if tree[i][0] != -1 else None)
    oopTree[i].setRight(oopTree[tree[i][2]] if tree[i][2] != -1 else None)

def inOrderOOP(currentNode):
	if currentNode.getLeft(): inOrderOOP(currentNode.getLeft())
	print(currentNode.getName())
	if currentNode.getRight(): inOrderOOP(currentNode.getRight())
        
def preOrderOOP(currentNode):
	print(currentNode.getName())
	if currentNode.getLeft(): preOrderOOP(currentNode.getLeft())
	if currentNode.getRight(): preOrderOOP(currentNode.getRight())
        
def postOrderOOP(currentNode):
	if currentNode.getLeft(): postOrderOOP(currentNode.getLeft())
	if currentNode.getRight(): postOrderOOP(currentNode.getRight())
	print(currentNode.getName())

# for i in range(len(tree)):
#     print(f"{i}: {oopTree[i].getName()}")
#     print(f"Left: {oopTree[i].getLeft().getName() if oopTree[i].getLeft() else None}")
#     print(f"Right: {oopTree[i].getRight().getName() if oopTree[i].getRight() else None}")
#     print()

print("\nIn-order object oriented")
inOrderOOP(oopTree[startNode])

print("\nPre-order object oriented")
preOrderOOP(oopTree[startNode])

print("\nPost-order object oriented")
postOrderOOP(oopTree[startNode])