A = []
G = {}
lung = int(input("Dati lungimea: "))
term = []
with open("gramatica.in", 'r') as f:
    x = f.readline().strip().split()
    while x:
        A.append(x[0])
        G[x[0]] = x[1:]
        x = f.readline().strip().split()
    print(G)
    for a in G.keys():
            for b in G[a]:
                if len(b) == 1 and a not in term:
                    term.append(a)
    print(term)

    cuv = []
    for lit in G['S']:
        cuv.append(lit)

    while len(cuv[len(cuv)-1]) < lung:
        cuvn = []
        for inc in cuv:
            noi = []
            for lit in range(len(inc)):
                if inc[lit] in A:
                    for e in G[inc[lit]]:
                        nou = inc[:lit] + e + inc[lit+1:]
                        if nou not in cuv:
                            cuvn.append(nou)
        cuv = cuvn

    for acc in cuv:
        if acc[len(acc)-1] in term:
            print(acc[:len(acc) - 1])
        if acc[len(acc)-1].islower() and acc[len(acc)-1] != '_':
            print(acc)