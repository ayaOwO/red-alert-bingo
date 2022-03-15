import random

HEIGHT = 3
WIDTH = 3

with open("cities.txt", 'r', encoding='utf-8') as cities:
    data = cities.read().split("\n")

nums = []
for i in range(HEIGHT * WIDTH):
    num = random.randrange(len(data))
    while (num in nums): 
        num = random.randrange(len(data))
    nums += [num]
board = [[] for i in range(HEIGHT)]
file = open("board.txt", 'w', encoding='utf-8')
for i in range(HEIGHT):
    for j in range(WIDTH):
        board[i] += [data[nums[i*HEIGHT + j]]]
for i in board:
    file.write('#'.join(i) + "\n")
file.write("\n000" * HEIGHT)
file.close()
