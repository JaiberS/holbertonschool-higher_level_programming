#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    pt = []
    pp = []
    pp.append(1)
    pt.append(pp)
    for i in range(n - 1):
        pp = []
        pt2 = pt[-1]
        i = 0
        while i < len(pt2):
            if i != 0:
                pp.append(pt2[i] + pt2[i-1])
            else:
                pp.append(1)
            i += 1
        pp.append(1)
        pt.append(pp)
    return pt
