import random
import folder
print(random.randint(1,3))
print(folder.my_name)

rand_num_0_to_1 = random.random()*10
print(rand_num_0_to_1)

#include upperbound

rand_incl_upp = random.uniform(0,10)
print(rand_incl_upp)

#HEAD OR TAIL GENERATOR

coin_value = random.randint(0,1)
if coin_value == 0:
    print("HEADS!!!!")

else:
    print("TAILS!!!")