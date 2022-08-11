
def inter(intvals):
    l = {}
    for a, b in intvals:
        l[a] = l.get(a, 0) + 1
        l[b] = l.get(b, 0) - 1
    s = sorted(l)
    maximum, current = 0, 0
    for x in s:
        current += l[x]
        maximum = max(maximum, current)

    return maximum

print(inter([(3,8),(2,4),(4,5),(0,5),(2,7),(1,8),(4.1,4.8)])) #6
print(inter([(1,2)])) #1
print(inter([(3,6),(2,5),(2,3)])) #2
print(inter([(2,4),(4,6),(6,9), (1,10)])) #2
print(inter([])) #0
