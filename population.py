# 9.11.2022
# Edit 16.11.2022

young,old,elderly = 6,9,12

for i in range(0, int(input("iterations> "))):
    print(f'|==========| {i + 1} |==========|')
    
    young, old, elderly = old * 4 + elderly * 2, young // 2, old // 3

    print(f'{young}\n{old}\n{elderly}\nTotal = {young + old + elderly}')

print(f'Loop finished, final Population : [Young = {young}, Old = {old}, Elderly = {elderly}, Total = {young + old + elderly}]')