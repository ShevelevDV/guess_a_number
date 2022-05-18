import numpy as np
import time

number = np.random.randint(1, 101) # загадываем число
tries=[]
predict_number = np.random.randint(1, 101) # первая попытка угадать
tries.append(predict_number)
predict_number = np.random.randint(1, 101) # вторая попытка угадать
tries.append(predict_number)
count = 0
print(number)

lower=1
higher=101

while True:
    count += 1
    
    for i in tries:
        if lower<i<number:
            lower=i
        elif higher>i>number:
            higher=i 
    
    predict_number = np.random.randint(lower, higher)
    tries.append(predict_number)
    
    if predict_number==number:
        break
    
    lower=1
    higher=101
    
print(tries)
print(count)