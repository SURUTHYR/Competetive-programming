items=["ab","abc","ba","bca"]

d = {}
for i in items:
    temp = "".join(sorted(i))
    print(temp)
    if temp in d:
        d[temp].append(i)
    else:
        d[temp] = [i]

for i in d:
    for j in d[i]:
        print(j, end=" ")
    print()