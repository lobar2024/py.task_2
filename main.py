def bellman_ford(vertices, edges, start):
    dist = {v: float('inf') for v in vertices}
    dist[start] = 0
    prev = {v: None for v in vertices}

    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u

    # Manfiy sikl tekshiruvi
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None, None  # manfiy sikl bor!

    return dist, prev

if __name__ == "__main__":
    vertices = ["A","B","C","D"]
    edges    = [
        ("A","B", 1), ("A","C", 4),
        ("B","C", 2), ("B","D", 5),
        ("C","D", 1)
    ]
    dist, prev = bellman_ford(vertices, edges, "A")
    print("Masofalar:", dist)
    # {'A':0, 'B':1, 'C':3, 'D':4}

    # Manfiy sikl
    edges2 = [("A","B",1),("B","C",-3),("C","A",1)]
    d, _ = bellman_ford(["A","B","C"], edges2, "A")
    print("Manfiy sikl:", d is None)  # True
