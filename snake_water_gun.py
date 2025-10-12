import random
""""
Snake drinks water, water ruins the gun and gun shoots the snake. Playing with computer and printing whether I win or lose.
Results can be generated using a matrix.
"""
print("\t\tSnake Water Gun Game\n")
elements = {0: "Snake", 1: "Water", 2: "Gun"}
l = [["Draw", "Win", "Lose"],
    ["Lose", "Draw", "Win"],
    ["Win", "Lose", "Draw"]
    ]

x = int(input("Choose any one element (Snake-> 0, Water-> 1, Gun-> 2)\n"))
y = random.choice(range(0,3))
z = l[x][y]
print(f'You have chosen {elements[x]}')
print(f'Computer has chosen {elements[y]}')
print(f'Result: {z}')