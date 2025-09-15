def advance_mul():
    for i in range(0, 11):
        print(f"Table de {i} : {i * 0}",end=" ")
        for j in range(1, 11):
            print(f"{i * j}", end=" ")
        print()
advance_mul()