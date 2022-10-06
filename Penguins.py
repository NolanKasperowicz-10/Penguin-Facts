penguins = ["King", "Emperor", "Chinstrap", "Gentoo", "Little", "African", "Southern Rockhopper", "Macaroni"]
pHab = ["King penguins spend a lot of time in the ocean feeding,\n but their primary habitats are sparsely vegetated areas of islands in the southern oceans and sub-Antarctic\n", "Wild Emperor penguins are only found in Antarctica. They breed and raise their young mostly on 'fast ice', a floating platform of frozen ocean which is connected to the land or to ice shelves.", "Chinstrap penguins breed mainly on the Antarctic Peninsula and on islands in the South Atlantic Ocean. There is a small breeding population on the Balleny Islands, south of New Zealand.", "Gentoo penguins have a large geographic range. They breed on many sub-Antarctic islands and on the Antarctic Peninsula. They generally occupy their islands all year round. The largest populations of gentoo penguins are in the Falkland Islands (South Georgia), and on the Antarctic Peninsula.", "The Little Penguin occurs only in Australia and New Zealand. They are found right along the southern edge of Australia and Tasmania. Most colonies exist on islands such as Kangaroo Island and Phillip Island. The breeding season runs from August to February.", "African penguins are found along coastal areas and offshore islands. Their preferred habitats are flat sandy areas with sparse oThese penguins live on rocky shorelines and make burrows and nests in high grasses called tussocks, they live among the craggy, windswept shorelines of the islands north of Antarctica, from Chile to New Zealand.", "Macaroni penguins live in rocky, water-bound areas, on rocks and cliffs above the ocean, and can be found on sub–Antarctic Islands and, occasionally, on the northwestern Antarctic Peninsula and its adjacent islands"]
pDiet = ["King penguins are quite specialised in their prey. They mainly eat lantern fish (myctophids), especially during the breeding season. Over winter, the percentage of squid in their diet increases.", "Emperors feed mostly on Antarctic silverfish as well as other species of fish, krill and some squid. An adult penguin eats about 2-3 kg per day, but on a good day they can eat twice this much to build up their store of body fat for the long winter, or for feeding their chicks.", ""]
pApp = [""]
pConStat = [""]
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
    

















