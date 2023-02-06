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
