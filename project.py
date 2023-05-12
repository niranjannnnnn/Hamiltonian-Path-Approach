data = "file.txt"
graphs = []
vertices = []
edges = []
with open(data, "r") as f:
    k = int(f.readline().strip())
    for line in f:
        if line.strip():
            vertice1, vertice2 = list(map(int, line.strip().split(" ")))
            graph[vertice1].append(vertice2)
        else:
            vertice, edge = map(int, f.readline().strip().split(" "))
            # print(edge)
            graph = {v: [] for v in range(1, vertice + 1)}
            graphs.append(graph)
            vertices.append(vertice)
            edges.append(edge)


def topologicalsortUtil(v, visited, stack):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            topologicalsortUtil(i, visited, stack)
    stack.insert(0, v)


def topologicalsort(graph, vertice):
    visited = [False] * (vertice + 1)
    stack = []

    for v in range(1, vertice + 1):
        if visited[v] == False:
            topologicalsortUtil(v, visited, stack)
    return (stack)


def check_consecutive(stack, graph):
    for i in range(len(stack) - 1):
        if stack[i + 1] not in graph[stack[i]]:
            return False
    return True


for n in range(k):
    graph = graphs[n]
    vertice = vertices[n]
    stack = topologicalsort(graph, vertice)
    if check_consecutive(stack, graph):
        print(1, end=" ")
        for i in stack:
            print(i, end=" ")
        print("")
    else:
        print(-1)
