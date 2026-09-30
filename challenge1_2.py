# Kate Macias
# Software engineering 1
# Fall 2026
#
# python3 challenge1_2.py - terminal run statement
#
#

from collections import deque

#this function builds a list of links from the pairs of nodes

def build_links(pairs):
    links = {}
    for a, b in pairs:
        links.setdefault(a, set()).add(b)
        links.setdefault(b, set()).add(a)
    return links


#this function pops nodes off and puts it back

def sweep(links, start, seen):
    group = []
    pending = deque([start])
    seen.add(start)
    while pending:
        n = pending.popleft()
        group.append(n)
        for m in links[n]:
            if m not in seen:
                seen.add(m)
                pending.append(m)
    return group

#this function groups nodes into clusters of matched pairs

def clusters(pairs):
    links = build_links(pairs)
    seen = set()
    groups = []
    for n in links:
        if n not in seen:
            groups.append(sweep(links, n, seen))
    return groups

# finds the biggest clusters
def biggest(pairs):
    groups = clusters(pairs)
    return max(groups, key=len)

def main():
    pairs = [
        ("a", "b"), ("b", "c"), ("c", "a"),
        ("d", "e"),
        ("f", "g"), ("g", "h"), ("h", "i"), ("i", "f"),
        ("j", "j"),
    ]
    groups = clusters(pairs)
    for g in groups:
        print(sorted(g))
    print(sorted(biggest(pairs)))

if __name__ == "__main__":
    main()
