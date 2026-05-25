'''
Bellman-Ford — Shortest Path with Negative-Weight Detection
Graph from the homework (slide 57), directed, source = vertex 0.

Edges:
    0 -> 1 (w=5)
    0 -> 2 (w=1)
    1 -> 2 (w=1)
    1 -> 3 (w=2)
    2 -> 4 (w=1)
    4 -> 3 (w=-1)

Complexity: O(V * E)
    V = number of vertices
    E = number of edges
'''

from __future__ import annotations

INF = float('inf')
Edge = tuple[int, int, int]

def bellman_ford(
    vertices: int,
    edges: list[Edge],
    source: int,
) -> tuple[list[float], list[int | None], bool]:
    '''
    Runs Bellman-Ford from source and checks for negative cycles.

    Args:
        vertices: Total number of vertices in the graph.
        edges: List of directed edges as (u, v, weight).
        source: Starting vertex (distance set to 0).

    Returns:
        dist: Shortest distance from source to each vertex.
        predecessor: Previous vertex on the shortest path (None if unreachable).
        has_neg_cycle: True if a negative-weight cycle is reachable from source.

    Complexity: O(V * E).
    '''
    # Phase 1 — Initialization
    dist: list[float] = [INF] * vertices
    predecessor: list[int | None] = [None] * vertices
    dist[source] = 0

    # Phase 2 — Iterative relaxation (V-1 times)
    _print_table(0, dist, predecessor, vertices)

    for iteration in range(1, vertices):
        updated = False

        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                predecessor[v] = u
                updated = True

        _print_table(iteration, dist, predecessor, vertices)

        if not updated:
            break

    # Phase 3 — Negative-cycle detection (one extra pass)
    has_neg_cycle = any(
        dist[u] != INF and dist[u] + w < dist[v]
        for u, v, w in edges
    )

    return dist, predecessor, has_neg_cycle

def _fmt(value: float | None, is_pred: bool = False) -> str:
    '''
    Formats a single table cell.

    Args:
        value: Distance or predecessor value.
        is_pred: True when formatting a predecessor cell.

    Returns:
        Right-aligned string of width 6.
    '''
    if is_pred:
        return f'{'–':>6}' if value is None else f'{value:>6}'

    return f'{'∞':>6}' if value == INF else f'{value:>6}'

def _print_table(iteration: int, dist: list[float], pred: list[int | None], v: int) -> None:
    '''
    Prints one row of the relaxation table.

    Args:
        iteration: Current iteration number (0 = initial state).
        dist: Distance array.
        pred: Predecessor array.
        v: Number of vertices.
    '''
    col_w = 6
    vertices = list(range(v))

    if iteration == 0:
        sep   = '+' + '+'.join('-' * (col_w + 2) for _ in range(v + 1)) + '+'
        header = '|' + f'{'Iter':^{col_w + 2}}' + '|'

        for i in vertices:
            header += f'{'V' + str(i):^{col_w + 2}}' + '|'

        print(sep)
        print(header)
        print(sep)

    sep = '+' + '+'.join('-' * (col_w + 2) for _ in range(v + 1)) + '+'
    label = 'Init' if iteration == 0 else f'It. {iteration}'

    dist_row = '|' + f'{label:^{col_w + 2}}|'
    pred_row = '|' + f'{'pred':^{col_w + 2}}|'

    for i in vertices:
        dist_row += f'{_fmt(dist[i]):^{col_w + 2}}|'
        pred_row += f'{_fmt(pred[i], is_pred=True):^{col_w + 2}}|'

    print(dist_row)
    print(pred_row)
    print(sep)

def reconstruct_path(predecessor: list[int | None], source: int, target: int) -> list[int]:
    '''
    Traces back the shortest path from source to target via predecessors.

    Args:
        predecessor: Array where predecessor[v] is the vertex before v on the path.
        source: Starting vertex.
        target: Destination vertex.

    Returns:
        Ordered list of vertices forming the path, or empty list if unreachable.
    '''
    path: list[int] = []
    current: int | None = target

    while current is not None:
        path.append(current)

        if current == source:
            break

        current = predecessor[current]

    if not path or path[-1] != source:
        return []
    
    return list(reversed(path))

def main() -> None:
    # Runs Bellman-Ford on the homework graph and prints all results.
    V = 5
    edges: list[Edge] = [
        (0, 1,  5),
        (0, 2,  1),
        (1, 2,  1),
        (1, 3,  2),
        (2, 4,  1),
        (4, 3, -1),
    ]
    source = 0

    print('BELLMAN-FORD  |  source = vertex 0\n')
    print('Edges:')

    for u, v, w in edges:
        print(f'  {u} -> {v}  (w={w:+})')

    print()
    dist, pred, neg_cycle = bellman_ford(V, edges, source)

    print('\nShortest paths:')
    for v in range(V):
        d = '∞' if dist[v] == INF else int(dist[v])
        path = reconstruct_path(pred, source, v)

        path_str = ' -> '.join(str(x) for x in path) if path else 'unreachable'
        print(f'  V{v}  dist={d}   {path_str}')

    print()

    if neg_cycle:
        print('Negative cycle detected — no valid shortest path exists.')
    else:
        print('No negative cycle detected.')

if __name__ == '__main__':
    main()