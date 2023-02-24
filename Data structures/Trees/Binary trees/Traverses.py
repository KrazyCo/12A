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
class Node: # class definition - no inheritance - capatilised
	def __init__(self, name): # constructor method - automatticly run at object instantiation/moment of creation - public
		# __init__ is the identifier
		# self is the object itself - name is the parameter
		self.__name = name # data is variable
		# = is assignment 
		# __name is private attribute 
	
    # all examples of encapsulation - using public methods to access private attributes
	def setLeft(self, left): # setter method
		self.__left = left

	def setRight(self, right): # setter method
		self.__right = right

	def getLeft(self): # getter method 
		return self.__left

	def getRight(self): # getter method
		return self.__right

	def getName(self): # getter method
		return self.__name

# from nodeClass import Node (example of importing node from nodeClass.py)
# nodeClass is libary - Node is class

# tree is 2d list - as has different data types
# "tree" is identifier

oopTree = [] # oopTree is identifier to which an empty list is assigned - will be list of objects

for i in range(len(tree)): # for loop - counter controlled iteration - i is counter - in range means start at 0 and go up to but length of tree -1
	oopTree.append(Node(tree[i][1])) # append is list method
	# Node(tree[i][1]) is object instantiation, setting name to tree[i][1] - tree[i][1] is the name of the node

for i in range(len(tree)):
    oopTree[i].setLeft(oopTree[tree[i][0]] if tree[i][0] != -1 else None) # if is selection - branching based on condition 
    # setLeft is setter method - oopTree is list, index is tree[i][0] which is left pointer 
    # takes appropriate left hand pointer from the 2d list tree and assigns the left pointer of the object to the correct object in oopTree
    oopTree[i].setRight(oopTree[tree[i][2]] if tree[i][2] != -1 else None)

def inOrderOOP(currentNode): # defines a procedure - inOrderOOP is identifier - currentNode is parameter
	if currentNode.getLeft(): inOrderOOP(currentNode.getLeft()) # recursive call - condition is if currentNode has a left pointer - condition must evaluate to true or false
	print(currentNode.getName()) # getName is getter method - currentNode is object
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

print("\nIn-order object oriented") # outputs to the user - "" is string
inOrderOOP(oopTree[startNode]) # procedure call - inOrderOOP is identifier - oopTree[startNode] is argument - root node is oopTree[0] - startNode is 0

print("\nPre-order object oriented")
preOrderOOP(oopTree[startNode])

print("\nPost-order object oriented")
postOrderOOP(oopTree[startNode])