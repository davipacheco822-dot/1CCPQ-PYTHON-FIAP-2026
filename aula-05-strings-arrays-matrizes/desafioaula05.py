nomes = ["Ana", "Maria", "Enzo", "Leo"]

for i in range(len(nomes)):
    for j in range(i+1,len(nomes)):
        if i != j:
            print(f"({nomes[i]}, {nomes[j]})")