for i in range(7):
    for j in range(7):
        if j == 0 or j ==7-1 or i == 7 // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
