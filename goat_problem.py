# 2022-12-14
# https://www.inf-schule.de/imperative-programmierung/python/projekte/kontrollstrukturen/ziegenproblem/durchfuehrung

from random import seed, shuffle

seed(); door = [0,1,2]; shuffle(door)

guess = int(input('Which door will you choose? '))

print(f' In door {door.index(1)} is the goat!')

guess = int(input('Which door will you choose? '))


print('You won!') if guess == door.index(2) else print('You lost!')
