# https://qiita.com/drken/items/4a7869c5e304883f539b

def dfs(seen:list, g:list, v:int):
    seen[v] = True
    for next_v in g[v]:
        if seen[next_v]: continue
        seen = dfs(seen, g, next_v)
    return seen

if __name__ == "__main__":
    g = [
        [1,4,11],
        [2,3],
        [],
        [],
        [5,8],
        [6,7],
        [],
        [],
        [9,10],
        [],
        [],
        [12,13],
        [],
        [14],
        []
    ]
    seen = [False] * len(g)
    print(seen)
    seen = dfs(seen,g,0)
    print(seen)

    from graphviz import Digraph
    G = Digraph(format="png")
    G.attr("node",shape="circle")
    edge = []
    for v in range(len(g)):
        next_vs = g[v]
        for next_v in next_vs:
            G.edge(str(v), str(next_v))
    G.render("tree")