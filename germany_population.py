# 2022-11-30
# calculates the population changes of germany based on the population data from 2005 for n years

p0_14, p15_49, p50_64, p65 = 12.3*(10**6), 39.1*(10**6), 15.5*(10**6), 16.3*(10**6)

for i in range(0, int(input('Iterations> '))):
    print(f'|==========| {i + 1} |==========|')
   
    p0_14, p15_49, p50_64, p65 = int(p0_14*0.93 + p15_49*0.02), int(p15_49 * 0.97 + p0_14 * 0.066), int(p50_64 * 0.925 + p15_49 + 0.029), int(p65 * 0.972 + p50_64 * 0.066) 
    
    print(f'0-14 = {p0_14}\n15-49 = {p15_49}\n50-64 = {p50_64}\n65+ = {p65}\nTotal = {p0_14 + p15_49 + p50_64 + p65}')

print(f'\n\nLoop Finished\nFinal Population\n----------------\n0-14 = {p0_14}\n15-49 = {p15_49}\n50-64 = {p50_64}\n65+ = {p65}\nTotal = {p0_14 + p15_49 + p50_64 + p65}')
