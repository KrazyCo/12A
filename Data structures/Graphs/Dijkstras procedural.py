edges = [["A", "B", 2], ["A", "C", 9], ["A", "D", 3],  ["B", "E", 2], ["C", "A", 9], 
         ["D", "A", 3], ["D", "B", 6], ["D", "C", 7], ["D", "E", 1], ["D", "F", 5], ["E", "F", 8]]
nodes = {"A":[0, "", False], "B":[0, "", False], "C":[0, "", False], "D":[0, "", False], "E":[0, "", False], "F":[0, "", False]}

nextNodes = ["A"]
endNode = "F"

allVisitied = False

while not allVisitied:
    tempNodes = nextNodes
    print(f"{nextNodes = }")
    nextNodes = []
    for node in tempNodes:
        if not nodes[node][2]:
            nodes[node][2] = True
            print(f"{node = }")
            print(f"{nodes = }")
            for edge in edges:
                # print(f"{edge[0] = }")
                # print(f"{node = }")
                if edge[0] == node:
                    if nodes[edge[1]][0] < (nodes[node][0] + edge[2]):
                        nodes[edge[1]][0] = nodes[node][0] + edge[2]
                        nodes[edge[1]][1] = node
                        # print(f"{nodes[edge[1]][2] = }")
                        # if not nodes[edge[1]][2]:
                        nextNodes.append(edge[1])

    if len(nextNodes) == 0:
        allVisitied = True

print(nodes)