from tracemalloc import start


penguins = ["King", "Emperor", "Chinstrap", "Gentoo", "Little", "African", "Southern Rockhopper", "Macaroni"]
pHab = ["King penguins spend a lot of time in the ocean feeding,\n but their primary habitats are sparsely vegetated areas of islands in the southern oceans and sub-Antarctic\n""]
pDiet = [""]
pApp = ["asdsa"]
pConStat = ["hdhdsj"]
p = input("Hello! Welcome to Penguin Facts! What Penguin would you like to learn about?\n0. King\n1. Emperor\n2. Chinstrap\n3. Gentoo\n4. Little\n5. African\n6. Southern Rockhopper\n7. Macaroni\n")
i = input("What do you want to learn about the " + penguins[int(p)] + " Penguin?\n0. Habitat\n1. Diet\n2. Appearance\n3. Conservation Status\n")
if i == "0":
    print(pHab[int(p)])
elif i == "1":
    print(pDiet[int(p)])
elif i == "2":
    print(pApp[int(p)])
elif i == "3":
    print(pConStat[int(p)])
    

















