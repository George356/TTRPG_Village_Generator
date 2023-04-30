import random
import math
import numpy as np

rng = np.random.default_rng(2021)
pop = 50
# give a value between 0-3 
bighouse = math.floor(rng.random()*3)
# 0 1 2-8
def genHouseNum():
    return math.floor(pop/(2.5+(rng.random()*6)))
houses = []*genHouseNum()
house = []
i = pop
y = bighouse
count = 0
while i> 0:
    while y>0:
        z =math.floor(4+(rng.random()*8))
        print(count)
        if z>i:
            house.append(i)
            i=0
        else:
            house.append(z)
            i=i-z
        y=y-1
    z =math.floor(0.9+(rng.random()*6))
    if z>i:
        house.append(i)
        i=0
    else:
        house.append(z)
        i=i-z
    count = count+1
    print(count)
    if (count>50):break
    

