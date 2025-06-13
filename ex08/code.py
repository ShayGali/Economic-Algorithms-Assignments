import networkx as nx
import math
from typing import Dict, Tuple, List, Any

def vcg_cheapest_path(
        G: nx.Graph,
        source: Any,
        target: Any,
) -> Tuple[List[Any], float, Dict[Tuple[Any, Any], float]]:
    """
    Compute the shortest path from `source` to `target` (by `weight_attr`)
    and the VCG payment owed by every edge on that path.

    Parameters
    ----------
    G : nx.Graph or nx.Graph
        Weighted graph whose edge weights are stored in the `weight_attr`
        edge attribute.
    source, target : hashable
        Start and goal vertices.
    weight_attr : str, optional
        Name of the edge attribute that stores the cost/weight (default "weight").

    Returns
    -------
    path : list
        The sequence of vertices on the minimum-cost path.
    total_cost : float
        Sum of edge weights along `path`.
    payments : dict
        Mapping {(u, v): p_e} giving each edge's VCG payment.
        Keys use the same orientation as the path (for undirected graphs you
        may wish to sort each tuple yourself).

    Raises
    ------
    networkx.NetworkXNoPath
        If no path exists between `source` and `target`.

        Examples
    --------
    >>> import networkx as nx
    >>> G1 = nx.Graph()
    >>> G1.add_edge("a", "b", weight=3)
    >>> G1.add_edge("a", "c", weight=5)
    >>> G1.add_edge("a", "d", weight=10)
    >>> G1.add_edge("b", "c", weight=1)
    >>> G1.add_edge("b", "d", weight=4)
    >>> G1.add_edge("c", "d", weight=1)
    >>> path, cost, payments = vcg_shortest_path_payments(G1, "a", "d")
    >>> path
    ['a', 'b', 'c', 'd']
    >>> cost
    5
    >>> payments == {('a', 'b'): 4, ('b', 'c'): 2, ('c', 'd'): 3}
    True

    Another example with a directed graph:
    >>> G2 = nx.DiGraph()
    >>> G2.add_edge("s", "v", weight=2)
    >>> G2.add_edge("v", "t", weight=3)
    >>> G2.add_edge("s", "t", weight=6)
    >>> path, cost, pay = vcg_shortest_path_payments(G2, "s", "t")
    >>> path
    ['s', 'v', 't']
    >>> cost
    5
    >>> pay == {('s', 'v'): 3, ('v', 't'): 4}
    True
    """
    # Define the weight attribute
    weight_attr = "weight"

    # --- 1) shortest path & its cost ----------------------------------------
    path: List[Any] = nx.shortest_path(G, source, target, weight=weight_attr)
    total_cost: float = nx.path_weight(G, path, weight=weight_attr)


    # Pre-compute the cost contributed by "all other edges" once
    # (we’ll reuse it inside the loop).
    payments: Dict[Tuple[Any, Any], float] = {}

    # Helper to fetch weight of a single edge
    def edge_weight(u, v):
        return G[u][v][weight_attr]

    # Build list of edges (u, v) in the path, with the chosen orientation
    path_edges = list(zip(path[:-1], path[1:])) # ['s', 'v', 't'] -> [('s', 'v'), ('v', 't')]

    # --- 2) VCG payment for each edge in the path ---------------------------
    for u, v in path_edges:
        # Cost of the other edges in the chosen path
        cost_others = total_cost - edge_weight(u, v)

        # Save the edge weight before removing
        saved_edge = G.get_edge_data(u, v).copy()

        # Remove edge (u, v) temporarily
        G.remove_edge(u, v)
        try:
            # If another s-t path exists, get its cost; otherwise Infinity
            alt_cost = nx.shortest_path_length(G, source, target, weight=weight_attr)
        except nx.NetworkXNoPath:
            alt_cost = math.inf
        finally:
            # Put the edge back exactly as it was
            G.add_edge(u, v, **saved_edge)

        # VCG payment formula
        payments[(u, v)] = alt_cost - cost_others

    return path, total_cost, payments


if __name__ == "__main__":
    G2 = nx.Graph()
    G2 = nx.DiGraph()
    G2.add_edge("s", "v", weight=2)
    G2.add_edge("v", "t", weight=3)
    G2.add_edge("s", "t", weight=6)
    path, cost, pay = vcg_shortest_path_payments(G2, "s", "t")
    print("Shortest path:", path)
    print("Total cost:   ", cost)
    total_pay = sum(pay.values())
    print("Payments:")
    for e, p in pay.items():
        print(f"  {e} pay: {p}")
    print("For the rest of the edges, e pay 0")
    print("Total payments:", total_pay)

# run the doctest command
# python -m doctest -v h8.py
