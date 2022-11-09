

young = 6
old = 9
elderly = 12

young1 = 0
old1 = 0
elderly1 = 0

iterations = int(input("iterations>"))



for i in range(0, iterations):
    print("|==========| " + str(i + 1) + " |==========|")
    young1 = old * 4 + elderly * 2

    old1 = young / 2

    elderly1 = old / 3

    young = young1
    old = old1
    elderly = elderly1

    print(young)
    print(old)
    print(elderly)




