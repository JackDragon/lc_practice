
# 14716104719,GET,/index.html,10.10.10.1

from collections import defaultdict


def top_ten_ips(file):
    with open(file, ‘r’) as f:
        lines = f.readlines()
    ip_freq = defaultdict(int)
    for line in lines:
        ip_freq[line.split(‘, ’)[-1]] += 1
    if not lines:
        return
    # Convert dict into list of k-v pairs
    # {1:2} -> [(1,2)]
    items = ip_freq.items()
    # sort items by second item in tuple
    # [(1,2), (2,1)] -> [(2,1),(1,2)]
    items = sort(items, lambda item: item[1])  # might have some syntax
    # [1,2,10] -> [(0, 1), (1, 2), (2,10)]
    x = min(10, len(items))
    for rank, item in enumerate(items[:x]):
    # (10.10.10.1, 20)
    print(“{}.ip:{} - count:{}”.format(rank, item[0], item[1]))


    N
    lines
    K
    size
    m
    charcters
    per
    line
    Time: N + N * m + NlogN
    Space: K + K + K + 10

    Node
    {
        int
    id; // unique
    id
    for each node, e.g: 27
    string
    value; // value
    of
    each
    node, e.g. ‘books’
    int
    parentId; // id
    of
    parent
    node, e.g.
    5, or -1 if no
    parent
    }

    P1
    C1
    GC1


C2
GC2
# naive way
# loop through the entire list to find root (doesn’t have parent)
# loop through the entire list to find nodes that have the root as parent
# loop through the…

level_dict  # what level the node is at, with root being 0 and incr.
child_dict  # parent: [childs]
loop
through
nodes
if node has no parent:
    level_dict[node] = 0
    # node has parent
    else:
    if parent in level_dict:
        add
        1
        to
        parent’s
        level
    else:
        look
        through
        child_dict: