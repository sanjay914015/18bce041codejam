
t = int(input()) #total number of squre
for j in range(t):
    n = int(input()) #size of square
    lst1 = []
    for i in range(n):
        l = list(map(int,input().split()))
        lst1.append(l)
    a=0
    for i in range(n):
        #print(lst[i][i])
        a = a + lst1[i][i]
    r=0
    for i in range(n):
        s = set(lst1[i])
        if len(s) != n:
            r = r+1
    c=0
    for i in range(n):
        s = set()
        for x in range(n):
            s.add(lst1[x][i])
        if(len(s)!=n):
            c = c + 1
    print("Case #{}:".format(j+1),a,r,c)